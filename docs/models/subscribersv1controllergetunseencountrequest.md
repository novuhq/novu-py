# SubscribersV1ControllerGetUnseenCountRequest


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `subscriber_id`                                | *str*                                          | :heavy_check_mark:                             | N/A                                            |
| `seen`                                         | *Optional[bool]*                               | :heavy_minus_sign:                             | Indicates whether to count seen notifications. |
| `limit`                                        | *Optional[float]*                              | :heavy_minus_sign:                             | The maximum number of notifications to return. |
| `idempotency_key`                              | *Optional[str]*                                | :heavy_minus_sign:                             | A header for idempotency purposes              |