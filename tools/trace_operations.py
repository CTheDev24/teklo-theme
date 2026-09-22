"""Private local Trace ledger; no network, sending, payments or manufacturing."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from tools.trace_workflow import new_piece, transition


def private_root(value):
    root = Path(value).resolve()
    if any((p / '.git').exists() for p in (root, *root.parents) if p.parent != p):
        raise ValueError('Keep order data outside Git repositories')
    return root


def piece_id(key):
    return hashlib.sha256(json.dumps(key, separators=(',', ':')).encode()).hexdigest()


def atomic_json(path, value):
    handle, temporary = tempfile.mkstemp(prefix='.trace-', dir=path.parent)
    try:
        with os.fdopen(handle, 'w', encoding='utf-8') as stream:
            json.dump(value, stream, indent=2)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


class Ledger:
    def __init__(self, root):
        self.root = private_root(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def path(self, identifier):
        if len(identifier) != 64 or any(c not in '0123456789abcdef' for c in identifier):
            raise ValueError('Invalid piece ID')
        return self.root / (identifier + '.json')

    def read(self, identifier):
        return json.loads(self.path(identifier).read_text(encoding='utf-8'))

    def mutate(self, identifier, operation):
        path = self.path(identifier)
        lock = path.with_suffix('.lock')
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError as exc:
            raise ValueError('Ledger locked; do not retry until active writer finishes') from exc
        try:
            os.close(descriptor)
            result = operation(json.loads(path.read_text(encoding='utf-8')) if path.exists() else None)
            atomic_json(path, result)
            return result
        finally:
            lock.unlink()

    def create(self, shop, order, line, unit, quantity):
        piece = new_piece(shop, order, line, unit, quantity)
        identifier = piece_id(piece['key'])
        def operation(current):
            if current is not None:
                raise ValueError('Piece already exists; use show/apply')
            return {'schema': 1, 'piece': piece, 'receipts': []}
        self.mutate(identifier, operation)
        return identifier

    def apply(self, identifier, event, expected_revision):
        event = dict(event)
        token = event.get('id')
        if not isinstance(token, str) or not token.strip():
            raise ValueError('Unique event id required for safe retries')
        # Hash actual artifact bytes, not just a mutable filename.
        for field, target in (('gpx_file', 'gpx'), ('proof_file', 'file')):
            if field in event:
                artifact = Path(event.pop(field)).resolve()
                if artifact.stat().st_size > 20_000_000:
                    raise ValueError('Artifact exceeds 20 MB local validation limit')
                event[target] = artifact.read_bytes()
        serial = {k: ({'sha256': hashlib.sha256(v).hexdigest()} if isinstance(v, bytes) else v)
                  for k, v in event.items()}
        digest = hashlib.sha256(json.dumps(serial, sort_keys=True).encode()).hexdigest()
        def operation(current):
            if current is None:
                raise ValueError('Unknown piece')
            for receipt in current['receipts']:
                if receipt['id'] == token:
                    if receipt['sha256'] != digest:
                        raise ValueError('Event id reused for different evidence')
                    return current
            if current['piece']['revision'] != expected_revision:
                raise ValueError('Stale revision; reread before applying')
            result = transition(current['piece'], event)
            current['piece'] = result
            current['receipts'].append({'id': token, 'sha256': digest, 'revision': result['revision'], 'event': serial})
            return current
        return self.mutate(identifier, operation)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, help='Private folder outside any Git checkout')
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('init')
    for key in ('shop', 'order', 'line'):
        create.add_argument('--' + key, required=True)
    create.add_argument('--unit', type=int, required=True)
    create.add_argument('--quantity', type=int, required=True)
    show = commands.add_parser('show')
    show.add_argument('piece')
    apply = commands.add_parser('apply')
    apply.add_argument('piece')
    apply.add_argument('--event', required=True, help='Private JSON event file')
    apply.add_argument('--expected-revision', type=int, required=True)
    commands.add_parser('queue')
    args = parser.parse_args(argv)
    try:
        ledger = Ledger(args.root)
        if args.command == 'init':
            result = {'piece_id': ledger.create(args.shop, args.order, args.line, args.unit, args.quantity)}
        elif args.command == 'show':
            result = ledger.read(args.piece)
        elif args.command == 'apply':
            event = json.loads(Path(args.event).read_text(encoding='utf-8-sig'))
            result = ledger.apply(args.piece, event, args.expected_revision)
        else:
            result = [{'piece_id': p.stem, 'key': item['key'], 'state': item['state'], 'revision': item['revision']}
                      for p in sorted(ledger.root.glob('*.json'))
                      for item in [json.loads(p.read_text(encoding='utf-8'))['piece']]
                      if item['state'] != 'APPROVED']
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
