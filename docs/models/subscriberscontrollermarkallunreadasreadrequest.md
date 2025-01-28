# SubscribersControllerMarkAllUnreadAsReadRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `subscriber_id`                                                              | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `mark_all_message_as_request_dto`                                            | [models.MarkAllMessageAsRequestDto](../models/markallmessageasrequestdto.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `idempotency_key`                                                            | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | A header for idempotency purposes                                            |