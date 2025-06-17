# WorkflowListResponseDto


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `name`                                                       | *str*                                                        | :heavy_check_mark:                                           | Name of the workflow                                         |
| `tags`                                                       | List[*str*]                                                  | :heavy_minus_sign:                                           | Tags associated with the workflow                            |
| `updated_at`                                                 | *str*                                                        | :heavy_check_mark:                                           | Last updated timestamp                                       |
| `created_at`                                                 | *str*                                                        | :heavy_check_mark:                                           | Creation timestamp                                           |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | Unique database identifier                                   |
| `workflow_id`                                                | *str*                                                        | :heavy_check_mark:                                           | Workflow identifier                                          |
| `slug`                                                       | *str*                                                        | :heavy_check_mark:                                           | Workflow slug                                                |
| `status`                                                     | [models.WorkflowStatusEnum](../models/workflowstatusenum.md) | :heavy_check_mark:                                           | Status of the workflow                                       |
| `origin`                                                     | [models.WorkflowOriginEnum](../models/workfloworiginenum.md) | :heavy_check_mark:                                           | Origin of the workflow                                       |
| `last_triggered_at`                                          | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | Timestamp of the last workflow trigger                       |
| `step_type_overviews`                                        | List[[models.StepTypeEnum](../models/steptypeenum.md)]       | :heavy_check_mark:                                           | Overview of step types in the workflow                       |