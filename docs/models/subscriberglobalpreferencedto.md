# SubscriberGlobalPreferenceDto


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `enabled`                                                                        | *bool*                                                                           | :heavy_check_mark:                                                               | Whether notifications are enabled globally                                       |
| `channels`                                                                       | [models.SubscriberPreferenceChannels](../models/subscriberpreferencechannels.md) | :heavy_check_mark:                                                               | Channel-specific preference settings                                             |