# TopicsControllerRenameTopicRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `topic_key`                                                        | *str*                                                              | :heavy_check_mark:                                                 | The topic key                                                      |
| `rename_topic_request_dto`                                         | [models.RenameTopicRequestDto](../models/renametopicrequestdto.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `idempotency_key`                                                  | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | A header for idempotency purposes                                  |