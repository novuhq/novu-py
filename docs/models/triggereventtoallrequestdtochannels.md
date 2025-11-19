# TriggerEventToAllRequestDtoChannels

Channel-specific overrides that apply to all steps of a particular channel type. Step-level overrides take precedence over channel-level overrides.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `email`                                                                      | [Optional[models.EmailChannelOverrides]](../models/emailchanneloverrides.md) | :heavy_minus_sign:                                                           | Email channel specific overrides                                             |