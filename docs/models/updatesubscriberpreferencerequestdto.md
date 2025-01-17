# UpdateSubscriberPreferenceRequestDto


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `channel`                                                                            | [Optional[models.ChannelPreference]](../models/channelpreference.md)                 | :heavy_minus_sign:                                                                   | Optional preferences for each channel type in the assigned workflow.                 |
| `enabled`                                                                            | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | Indicates whether the workflow is fully enabled for all channels for the subscriber. |