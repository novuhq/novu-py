# MessagesControllerGetMessagesRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `channel`                                                        | [Optional[models.ChannelTypeEnum]](../models/channeltypeenum.md) | :heavy_minus_sign:                                               | Channel type through which the message is sent                   |
| `subscriber_id`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `transaction_id`                                                 | List[*str*]                                                      | :heavy_minus_sign:                                               | N/A                                                              |
| `page`                                                           | *Optional[float]*                                                | :heavy_minus_sign:                                               | N/A                                                              |
| `limit`                                                          | *Optional[float]*                                                | :heavy_minus_sign:                                               | N/A                                                              |
| `idempotency_key`                                                | *Optional[str]*                                                  | :heavy_minus_sign:                                               | A header for idempotency purposes                                |