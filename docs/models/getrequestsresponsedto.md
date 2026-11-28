# GetRequestsResponseDto


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `data`                                                                   | List[[models.RequestLogResponseDto](../models/requestlogresponsedto.md)] | :heavy_check_mark:                                                       | Request log data                                                         |
| `total`                                                                  | *float*                                                                  | :heavy_check_mark:                                                       | Total number of requests                                                 |
| `page_size`                                                              | *Optional[float]*                                                        | :heavy_minus_sign:                                                       | Page size                                                                |
| `page`                                                                   | *Optional[float]*                                                        | :heavy_minus_sign:                                                       | Current page number                                                      |