# ResourceDependencyDto


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `resource_type`                                                  | [models.ResourceTypeEnum](../models/resourcetypeenum.md)         | :heavy_check_mark:                                               | Type of the layout                                               |
| `resource_id`                                                    | *str*                                                            | :heavy_check_mark:                                               | ID of the dependent resource                                     |
| `resource_name`                                                  | *str*                                                            | :heavy_check_mark:                                               | Name of the dependent resource                                   |
| `is_blocking`                                                    | *bool*                                                           | :heavy_check_mark:                                               | Whether this dependency blocks the operation                     |
| `reason`                                                         | [models.DependencyReasonEnum](../models/dependencyreasonenum.md) | :heavy_check_mark:                                               | Reason for the dependency                                        |