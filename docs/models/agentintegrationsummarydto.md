# AgentIntegrationSummaryDto


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `integration_id`                                                 | *str*                                                            | :heavy_check_mark:                                               | Integration document id.                                         |
| `provider_id`                                                    | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `identifier`                                                     | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `channel`                                                        | [Optional[models.ChannelTypeEnum]](../models/channeltypeenum.md) | :heavy_minus_sign:                                               | Channel type through which the message is sent                   |
| `active`                                                         | *bool*                                                           | :heavy_check_mark:                                               | N/A                                                              |