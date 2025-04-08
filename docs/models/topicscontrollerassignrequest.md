# TopicsControllerAssignRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `topic_key`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | The topic key                                                            |
| `idempotency_key`                                                        | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | A header for idempotency purposes                                        |
| `add_subscribers_request_dto`                                            | [models.AddSubscribersRequestDto](../models/addsubscribersrequestdto.md) | :heavy_check_mark:                                                       | N/A                                                                      |