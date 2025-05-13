# DeleteTopicSubscriptionsResponseDto


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `data`                                                                               | List[[models.SubscriptionDto](../models/subscriptiondto.md)]                         | :heavy_check_mark:                                                                   | The list of successfully deleted subscriptions                                       |
| `meta`                                                                               | [models.MetaDto](../models/metadto.md)                                               | :heavy_check_mark:                                                                   | Metadata about the operation                                                         |
| `errors`                                                                             | List[[models.SubscriptionsDeleteErrorDto](../models/subscriptionsdeleteerrordto.md)] | :heavy_minus_sign:                                                                   | The list of errors for failed deletion attempts                                      |