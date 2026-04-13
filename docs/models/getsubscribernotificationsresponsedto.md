# GetSubscriberNotificationsResponseDto


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `data`                                                                 | List[[models.InboxNotificationDto](../models/inboxnotificationdto.md)] | :heavy_check_mark:                                                     | Array of notifications                                                 |
| `has_more`                                                             | *bool*                                                                 | :heavy_check_mark:                                                     | Indicates if there are more notifications available                    |
| `filter_`                                                              | [models.Filter](../models/filter_.md)                                  | :heavy_check_mark:                                                     | The filter applied to the notifications                                |