# MessageCTA


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `data`                                                                 | [models.MessageCTAData](../models/messagectadata.md)                   | :heavy_check_mark:                                                     | Data associated with the call to action                                |
| `type`                                                                 | [Optional[models.ChannelCTATypeEnum]](../models/channelctatypeenum.md) | :heavy_minus_sign:                                                     | Type of call to action                                                 |
| `action`                                                               | [Optional[models.MessageAction]](../models/messageaction.md)           | :heavy_minus_sign:                                                     | Action associated with the call to action                              |