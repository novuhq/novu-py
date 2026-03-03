# FailedWorkflowDto


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `resource_type`                                          | [models.ResourceTypeEnum](../models/resourcetypeenum.md) | :heavy_check_mark:                                       | Type of the layout                                       |
| `resource_id`                                            | *str*                                                    | :heavy_check_mark:                                       | Resource ID                                              |
| `resource_name`                                          | *str*                                                    | :heavy_check_mark:                                       | Resource name                                            |
| `error`                                                  | *str*                                                    | :heavy_check_mark:                                       | Error message                                            |
| `stack`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | Error stack trace                                        |