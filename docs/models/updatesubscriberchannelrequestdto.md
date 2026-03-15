# UpdateSubscriberChannelRequestDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `provider_id`                                                        | [models.ChatOrPushProviderEnum](../models/chatorpushproviderenum.md) | :heavy_check_mark:                                                   | The provider identifier for the credentials                          |
| `integration_identifier`                                             | *str*                                                                | :heavy_check_mark:                                                   | The integration identifier                                           |
| `credentials`                                                        | [models.ChannelCredentials](../models/channelcredentials.md)         | :heavy_check_mark:                                                   | Credentials payload for the specified provider                       |