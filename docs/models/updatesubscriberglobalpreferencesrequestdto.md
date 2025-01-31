# UpdateSubscriberGlobalPreferencesRequestDto


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `enabled`                                                        | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Enable or disable the subscriber global preferences.             |
| `preferences`                                                    | List[[models.ChannelPreference](../models/channelpreference.md)] | :heavy_minus_sign:                                               | The subscriber global preferences for every ChannelTypeEnum.     |