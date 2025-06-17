# WorkflowControllerSyncRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `workflow_id`                                          | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `idempotency_key`                                      | *Optional[str]*                                        | :heavy_minus_sign:                                     | A header for idempotency purposes                      |
| `sync_workflow_dto`                                    | [models.SyncWorkflowDto](../models/syncworkflowdto.md) | :heavy_check_mark:                                     | Sync workflow details                                  |