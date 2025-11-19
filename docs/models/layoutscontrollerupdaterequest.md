# LayoutsControllerUpdateRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `layout_id`                                            | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `idempotency_key`                                      | *Optional[str]*                                        | :heavy_minus_sign:                                     | A header for idempotency purposes                      |
| `update_layout_dto`                                    | [models.UpdateLayoutDto](../models/updatelayoutdto.md) | :heavy_check_mark:                                     | Layout update details                                  |