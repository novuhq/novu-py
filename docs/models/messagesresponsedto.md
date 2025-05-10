# MessagesResponseDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `total_count`                                                      | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | Total number of messages available                                 |
| `has_more`                                                         | *bool*                                                             | :heavy_check_mark:                                                 | Indicates if there are more messages available                     |
| `data`                                                             | List[[models.MessageResponseDto](../models/messageresponsedto.md)] | :heavy_check_mark:                                                 | List of messages                                                   |
| `page_size`                                                        | *float*                                                            | :heavy_check_mark:                                                 | Number of messages per page                                        |
| `page`                                                             | *float*                                                            | :heavy_check_mark:                                                 | Current page number                                                |