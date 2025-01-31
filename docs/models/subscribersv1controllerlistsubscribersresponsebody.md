# SubscribersV1ControllerListSubscribersResponseBody


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `page`                                                                   | *float*                                                                  | :heavy_check_mark:                                                       | The current page of the paginated response                               |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | Does the list have more items to fetch                                   |
| `page_size`                                                              | *float*                                                                  | :heavy_check_mark:                                                       | Number of items on each page                                             |
| `data`                                                                   | List[[models.SubscriberResponseDto](../models/subscriberresponsedto.md)] | :heavy_check_mark:                                                       | N/A                                                                      |