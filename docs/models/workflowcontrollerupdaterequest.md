# WorkflowControllerUpdateRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `workflow_id`                                              | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `idempotency_key`                                          | *Optional[str]*                                            | :heavy_minus_sign:                                         | A header for idempotency purposes                          |
| `update_workflow_dto`                                      | [models.UpdateWorkflowDto](../models/updateworkflowdto.md) | :heavy_check_mark:                                         | Workflow update details                                    |