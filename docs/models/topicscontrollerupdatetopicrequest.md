# TopicsControllerUpdateTopicRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `topic_key`                                                        | *str*                                                              | :heavy_check_mark:                                                 | The key identifier of the topic                                    |
| `idempotency_key`                                                  | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | A header for idempotency purposes                                  |
| `update_topic_request_dto`                                         | [models.UpdateTopicRequestDto](../models/updatetopicrequestdto.md) | :heavy_check_mark:                                                 | N/A                                                                |