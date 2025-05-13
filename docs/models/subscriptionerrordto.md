# SubscriptionErrorDto


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `subscriber_id`                                             | *str*                                                       | :heavy_check_mark:                                          | The subscriber ID that failed                               | invalid-subscriber-id                                       |
| `code`                                                      | *str*                                                       | :heavy_check_mark:                                          | The error code                                              | SUBSCRIBER_NOT_FOUND                                        |
| `message`                                                   | *str*                                                       | :heavy_check_mark:                                          | The error message                                           | Subscriber with ID invalid-subscriber-id could not be found |