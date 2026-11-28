# GetWorkflowRunsResponseDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `data`                                                             | List[[models.GetWorkflowRunsDto](../models/getworkflowrunsdto.md)] | :heavy_check_mark:                                                 | Workflow runs data                                                 |
| `next`                                                             | [OptionalNullable[models.Next]](../models/next.md)                 | :heavy_minus_sign:                                                 | Next cursor for pagination                                         |
| `previous`                                                         | [OptionalNullable[models.Previous]](../models/previous.md)         | :heavy_minus_sign:                                                 | Previous cursor for pagination                                     |