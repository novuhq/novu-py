# GenerateLayoutPreviewResponseDto


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `preview_payload_example`                                                | [models.LayoutPreviewPayloadDto](../models/layoutpreviewpayloaddto.md)   | :heavy_check_mark:                                                       | Preview payload example                                                  |
| `schema_`                                                                | Dict[str, *Any*]                                                         | :heavy_minus_sign:                                                       | The payload schema that was used to generate the preview payload example |
| `result`                                                                 | [models.Result](../models/result.md)                                     | :heavy_check_mark:                                                       | Preview result                                                           |