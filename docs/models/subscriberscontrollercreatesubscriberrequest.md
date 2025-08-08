# SubscribersControllerCreateSubscriberRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `fail_if_exists`                                                             | *bool*                                                                       | :heavy_check_mark:                                                           | N/A                                                                          |
| `idempotency_key`                                                            | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | A header for idempotency purposes                                            |
| `create_subscriber_request_dto`                                              | [models.CreateSubscriberRequestDto](../models/createsubscriberrequestdto.md) | :heavy_check_mark:                                                           | N/A                                                                          |