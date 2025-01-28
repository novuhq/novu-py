# MessagesControllerDeleteMessagesByTransactionIDRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `transaction_id`                                                     | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `channel`                                                            | [Optional[models.QueryParamChannel]](../models/queryparamchannel.md) | :heavy_minus_sign:                                                   | The channel of the message to be deleted                             |
| `idempotency_key`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | A header for idempotency purposes                                    |