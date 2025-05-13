# TopicsV1ControllerGetTopicSubscriberRequest


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `external_subscriber_id`          | *str*                             | :heavy_check_mark:                | The external subscriber id        |
| `topic_key`                       | *str*                             | :heavy_check_mark:                | The topic key                     |
| `idempotency_key`                 | *Optional[str]*                   | :heavy_minus_sign:                | A header for idempotency purposes |