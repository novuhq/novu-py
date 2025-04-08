# MessageCTA


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [Optional[models.ChannelCTATypeEnum]](../models/channelctatypeenum.md) | :heavy_minus_sign:                                                     | Type of call to action                                                 |
| `data`                                                                 | [models.MessageCTAData](../models/messagectadata.md)                   | :heavy_check_mark:                                                     | Data associated with the call to action                                |
| `action`                                                               | [Optional[models.MessageAction]](../models/messageaction.md)           | :heavy_minus_sign:                                                     | Action associated with the call to action                              |