# UpdateSubscriberChannelRequestDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `provider_id`                                                        | [models.ChatOrPushProviderEnum](../models/chatorpushproviderenum.md) | :heavy_check_mark:                                                   | The provider identifier for the credentials                          |
| `integration_identifier`                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The integration identifier                                           |
| `credentials`                                                        | [models.ChannelCredentials](../models/channelcredentials.md)         | :heavy_check_mark:                                                   | Credentials payload for the specified provider                       |