# NotificationWorkflowDto


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | Unique identifier of the workflow                          |
| `identifier`                                               | *str*                                                      | :heavy_check_mark:                                         | Workflow identifier used for triggering                    |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | Human-readable name of the workflow                        |
| `critical`                                                 | *bool*                                                     | :heavy_check_mark:                                         | Whether this workflow is marked as critical                |
| `tags`                                                     | List[*str*]                                                | :heavy_minus_sign:                                         | Tags associated with the workflow                          |
| `data`                                                     | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | Custom data associated with the workflow                   |
| `severity`                                                 | [models.SeverityLevelEnum](../models/severitylevelenum.md) | :heavy_check_mark:                                         | Severity of the workflow                                   |