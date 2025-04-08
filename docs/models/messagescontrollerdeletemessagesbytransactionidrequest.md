# MessagesControllerDeleteMessagesByTransactionIDRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `channel`                                                            | [Optional[models.QueryParamChannel]](../models/queryparamchannel.md) | :heavy_minus_sign:                                                   | The channel of the message to be deleted                             |
| `transaction_id`                                                     | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `idempotency_key`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | A header for idempotency purposes                                    |