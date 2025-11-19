# LayoutsControllerDuplicateRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `layout_id`                                                  | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `idempotency_key`                                            | *Optional[str]*                                              | :heavy_minus_sign:                                           | A header for idempotency purposes                            |
| `duplicate_layout_dto`                                       | [models.DuplicateLayoutDto](../models/duplicatelayoutdto.md) | :heavy_check_mark:                                           | N/A                                                          |