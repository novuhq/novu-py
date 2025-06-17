# WorkflowControllerCreateRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `idempotency_key`                                          | *Optional[str]*                                            | :heavy_minus_sign:                                         | A header for idempotency purposes                          |
| `create_workflow_dto`                                      | [models.CreateWorkflowDto](../models/createworkflowdto.md) | :heavy_check_mark:                                         | Workflow creation details                                  |