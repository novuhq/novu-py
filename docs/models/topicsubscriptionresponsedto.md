# TopicSubscriptionResponseDto


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | The identifier of the subscription                       | 64da692e9a94fb2e6449ad08                                 |
| `created_at`                                             | *str*                                                    | :heavy_check_mark:                                       | The date and time the subscription was created           | 2021-01-01T00:00:00.000Z                                 |
| `topic`                                                  | [models.TopicResponseDto](../models/topicresponsedto.md) | :heavy_check_mark:                                       | Topic information                                        |                                                          |
| `subscriber`                                             | [models.SubscriberDto](../models/subscriberdto.md)       | :heavy_check_mark:                                       | Subscriber information                                   |                                                          |