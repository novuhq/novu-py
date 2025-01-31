# SubscribersV1ControllerGetSubscriberRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `subscriber_id`                                    | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `include_topics`                                   | *Optional[bool]*                                   | :heavy_minus_sign:                                 | Includes the topics associated with the subscriber |
| `idempotency_key`                                  | *Optional[str]*                                    | :heavy_minus_sign:                                 | A header for idempotency purposes                  |