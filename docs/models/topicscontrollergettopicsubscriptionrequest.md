# TopicsControllerGetTopicSubscriptionRequest


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `topic_key`                               | *str*                                     | :heavy_check_mark:                        | The key identifier of the topic           |
| `identifier`                              | *str*                                     | :heavy_check_mark:                        | The unique identifier of the subscription |
| `idempotency_key`                         | *Optional[str]*                           | :heavy_minus_sign:                        | A header for idempotency purposes         |