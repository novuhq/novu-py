# TopicsControllerUpsertTopicRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `fail_if_exists`                                                               | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | If true, the request will fail if a topic with the same key already exists     |
| `idempotency_key`                                                              | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A header for idempotency purposes                                              |
| `create_update_topic_request_dto`                                              | [models.CreateUpdateTopicRequestDto](../models/createupdatetopicrequestdto.md) | :heavy_check_mark:                                                             | N/A                                                                            |