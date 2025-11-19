# LayoutsControllerGeneratePreviewRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `layout_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `idempotency_key`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | A header for idempotency purposes                                      |
| `layout_preview_request_dto`                                           | [models.LayoutPreviewRequestDto](../models/layoutpreviewrequestdto.md) | :heavy_check_mark:                                                     | Layout preview generation details                                      |