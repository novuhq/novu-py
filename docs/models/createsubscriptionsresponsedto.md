# CreateSubscriptionsResponseDto


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `data`                                                                       | List[[models.SubscriptionResponseDto](../models/subscriptionresponsedto.md)] | :heavy_check_mark:                                                           | The list of successfully created subscriptions                               |
| `meta`                                                                       | [models.MetaDto](../models/metadto.md)                                       | :heavy_check_mark:                                                           | Metadata about the operation                                                 |
| `errors`                                                                     | List[[models.SubscriptionErrorDto](../models/subscriptionerrordto.md)]       | :heavy_minus_sign:                                                           | The list of errors for failed subscription attempts                          |