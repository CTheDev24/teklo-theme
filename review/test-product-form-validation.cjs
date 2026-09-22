const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { resolve } = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');
let ProductForm;
vm.runInNewContext(readFileSync(resolve(__dirname, '../assets/product-form.js'), 'utf8'), {
  HTMLElement: class {},
  customElements: { get() {}, define(name, definition) { ProductForm = definition; } },
});

for (const [name, trace, valid, disabled, proceeds] of [
  ['empty piece reference', true, false, false, false],
  ['invalid piece reference', true, false, false, false],
  ['valid piece reference', true, true, false, true],
  ['ordinary product retains native behavior', false, false, false, true],
  ['unavailable product cannot submit', true, true, true, false],
]) {
  test(name, () => {
    let reported = 0;
    let proceeded = false;
    let prevented = false;
    const stopBeforeNetwork = new Error('stop before cart mutation');
    const instance = {
      submitButton: { getAttribute: () => disabled ? 'true' : null },
      form: {
        querySelector: () => trace ? {} : null,
        reportValidity: () => { reported++; return valid; },
      },
      handleErrorMessage: () => { proceeded = true; throw stopBeforeNetwork; },
    };
    try {
      ProductForm.prototype.onSubmitHandler.call(instance, { preventDefault() { prevented = true; } });
    } catch (error) { assert.equal(error, stopBeforeNetwork); }
    assert.equal(prevented, true);
    assert.equal(proceeded, proceeds);
    assert.equal(reported, trace && !disabled ? 1 : 0);
  });
}
