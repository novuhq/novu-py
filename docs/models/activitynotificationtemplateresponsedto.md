# ActivityNotificationTemplateResponseDto


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Unique identifier of the template                                          |
| `name`                                                                     | *str*                                                                      | :heavy_check_mark:                                                         | Name of the template                                                       |
| `origin`                                                                   | [Optional[models.ResourceOriginEnum]](../models/resourceoriginenum.md)     | :heavy_minus_sign:                                                         | Origin of the layout                                                       |
| `triggers`                                                                 | List[[models.NotificationTriggerDto](../models/notificationtriggerdto.md)] | :heavy_check_mark:                                                         | Triggers of the template                                                   |