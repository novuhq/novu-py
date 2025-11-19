# SubscribersControllerGetSubscriberPreferencesRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `subscriber_id`                                          | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `criticality`                                            | [Optional[models.Criticality]](../models/criticality.md) | :heavy_minus_sign:                                       | N/A                                                      |
| `idempotency_key`                                        | *Optional[str]*                                          | :heavy_minus_sign:                                       | A header for idempotency purposes                        |