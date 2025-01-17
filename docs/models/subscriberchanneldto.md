# SubscriberChannelDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `provider_id`                                                      | [models.ProviderID](../models/providerid.md)                       | :heavy_check_mark:                                                 | The ID of the chat or push provider.                               |
| `credentials`                                                      | [models.ChannelCredentialsDto](../models/channelcredentialsdto.md) | :heavy_check_mark:                                                 | Credentials for the channel.                                       |
| `integration_identifier`                                           | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | An optional identifier for the integration.                        |