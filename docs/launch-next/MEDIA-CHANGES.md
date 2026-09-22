# Trace media alt-text changes

Shopify product: `gid://shopify/Product/15807121490086`.

Applied alt-only updates to all 13 visually inspected images in batches of 11 and 2. Initial and immediate pre-mutation reads showed empty alt text. Both mutations returned zero userErrors; separate final query readback matches all 13 exact descriptions. Backup: `trace-product-before.json`.

No image sources, gallery associations, descriptions, prices or policies were changed. These are Shopify-hosted file metadata changes, not theme changes; file metadata can affect any product referencing the same image.

## Exact applied operation and variables

```json
{
  "query": "mutation TraceMediaAlt($files: [FileUpdateInput!]!) { fileUpdate(files: $files) { files { id alt } userErrors { field message } } }",
  "variables": {
    "files": [
      {
        "id": "gid://shopify/MediaImage/70401314619558",
        "alt": "Framed Gallery Trace sample with raised city buildings, orange route and personalized race poster."
      },
      {
        "id": "gid://shopify/MediaImage/70401314652326",
        "alt": "Assembled Trace with black glazed shadow-box frame, custom race poster and mounted 3D race map."
      },
      {
        "id": "gid://shopify/MediaImage/70401314685094",
        "alt": "Gallery light finish and Nocturne dark finish shown side by side with orange routes."
      },
      {
        "id": "gid://shopify/MediaImage/70404128309414",
        "alt": "Route accent samples labeled Signal Orange, Pulse Pink, Volt Lime and Graphite/Stone on a Gallery map."
      },
      {
        "id": "gid://shopify/MediaImage/70401314848934",
        "alt": "Close-up of raised light-colored city buildings and an orange race route in a Trace frame."
      },
      {
        "id": "gid://shopify/MediaImage/70401314586790",
        "alt": "Low-angle view of the raised city, elevated orange route and race poster inside a black frame."
      },
      {
        "id": "gid://shopify/MediaImage/70401314881702",
        "alt": "Ordering graphic illustrating option selection, route submission, proof review, production approval and displaying Trace."
      },
      {
        "id": "gid://shopify/MediaImage/70401314783398",
        "alt": "Route-input guide illustrating GPX files, public activity links and official race-course maps."
      },
      {
        "id": "gid://shopify/MediaImage/70401314816166",
        "alt": "Proof-review graphic illustrating design preparation, checking the route and custom details, and approval before production."
      },
      {
        "id": "gid://shopify/MediaImage/70401314750630",
        "alt": "Diagram of a framed Nocturne Trace with frame and map measurement annotations and material descriptions."
      },
      {
        "id": "gid://shopify/MediaImage/70401314717862",
        "alt": "Questions graphic about routes, GPX, customization and race courses; directs customers to Etsy Messages."
      }
    ]
  }
}
```

## Rollback

Revalidate the mutation and confirm no later edits, then execute this alt-only payload. It restores the original blank values and leaves all media attached.

```json
{
  "query": "mutation TraceMediaAlt($files: [FileUpdateInput!]!) { fileUpdate(files: $files) { files { id alt } userErrors { field message } } }",
  "variables": {
    "files": [
      {
        "id": "gid://shopify/MediaImage/70401314619558",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314652326",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314685094",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70404128309414",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314848934",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314586790",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314881702",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314783398",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314816166",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314750630",
        "alt": ""
      },
      {
        "id": "gid://shopify/MediaImage/70401314717862",
        "alt": ""
      }
    ]
  }
}
```

## Remaining graphic issues

Visual verification found Graphite/Stone in the accent image although it is not a current variant, 8–10 production days in the ordering graphic, unverified dimension annotations, and Etsy Messages in the questions graphic. These images still require correction/review; adding alt text does not fix their underlying promises. The descriptions avoid asserting unverified measurements or operational commitments.

## Validation

Discovered Mutation.fileUpdate, FileUpdateInput, FileUpdatePayload, QueryRoot.nodes and MediaImage through the Shopify schema connector. Both mutation and independent readback query passed GraphQL schema validation; the Admin skill validator also passed. The skill search helper failed network access. [Shopify fileUpdate documentation](https://shopify.dev/docs/api/admin-graphql/latest/mutations/fileUpdate).


## Additional visually verified images

The second batch covers images 3 and 13 using the same validated operation. Both batches are verified by the final independent readback.

Exact additional applied variables:

```json
{
  "files": [
    {
      "id": "gid://shopify/MediaImage/70305865203878",
      "alt": "Nocturne Houston 5K and Gallery Pennant 10K Trace samples displayed side by side in black frames."
    },
    {
      "id": "gid://shopify/MediaImage/70401315012774",
      "alt": "Framed Gallery Pennant 10K Trace with raised city map and orange route displayed beside a plant."
    }
  ]
}
```

Additional rollback variables (same mutation):

```json
{
  "files": [
    {
      "id": "gid://shopify/MediaImage/70305865203878",
      "alt": ""
    },
    {
      "id": "gid://shopify/MediaImage/70401315012774",
      "alt": ""
    }
  ]
}
```
