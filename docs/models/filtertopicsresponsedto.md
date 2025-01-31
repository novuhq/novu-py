# FilterTopicsResponseDto


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `data`                                         | List[[models.TopicDto](../models/topicdto.md)] | :heavy_check_mark:                             | The list of topics                             | []                                             |
| `page`                                         | *float*                                        | :heavy_check_mark:                             | The current page number                        | 1                                              |
| `page_size`                                    | *float*                                        | :heavy_check_mark:                             | The number of items per page                   | 10                                             |
| `total_count`                                  | *float*                                        | :heavy_check_mark:                             | The total number of items                      | 10                                             |