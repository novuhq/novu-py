# SubscriptionDto


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | The unique identifier of the subscription              | 64f5e95d3d7946d80d0cb679                               |
| `topic`                                                | [models.TopicDto](../models/topicdto.md)               | :heavy_check_mark:                                     | The topic information                                  |                                                        |
| `subscriber`                                           | [Nullable[models.Subscriber]](../models/subscriber.md) | :heavy_check_mark:                                     | The subscriber information                             |                                                        |
| `created_at`                                           | *str*                                                  | :heavy_check_mark:                                     | The creation date of the subscription                  | 2025-04-24T05:40:21Z                                   |
| `updated_at`                                           | *str*                                                  | :heavy_check_mark:                                     | The last update date of the subscription               | 2025-04-24T05:40:21Z                                   |