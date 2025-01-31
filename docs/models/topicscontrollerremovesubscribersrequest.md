# TopicsControllerRemoveSubscribersRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `topic_key`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | The topic key                                                                  |
| `remove_subscribers_request_dto`                                               | [models.RemoveSubscribersRequestDto](../models/removesubscribersrequestdto.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `idempotency_key`                                                              | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A header for idempotency purposes                                              |