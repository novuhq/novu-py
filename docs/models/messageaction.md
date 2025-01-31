# MessageAction


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `status`                                                                         | [Optional[models.MessageActionStatusEnum]](../models/messageactionstatusenum.md) | :heavy_minus_sign:                                                               | Status of the message action                                                     |
| `buttons`                                                                        | List[[models.MessageButton](../models/messagebutton.md)]                         | :heavy_minus_sign:                                                               | List of buttons associated with the message action                               |
| `result`                                                                         | [Optional[models.MessageActionResult]](../models/messageactionresult.md)         | :heavy_minus_sign:                                                               | Result of the message action                                                     |