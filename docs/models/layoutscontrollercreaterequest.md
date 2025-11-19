# LayoutsControllerCreateRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `idempotency_key`                                      | *Optional[str]*                                        | :heavy_minus_sign:                                     | A header for idempotency purposes                      |
| `create_layout_dto`                                    | [models.CreateLayoutDto](../models/createlayoutdto.md) | :heavy_check_mark:                                     | Layout creation details                                |