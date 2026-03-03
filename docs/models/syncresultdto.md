# SyncResultDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `resource_type`                                                    | [models.ResourceTypeEnum](../models/resourcetypeenum.md)           | :heavy_check_mark:                                                 | Type of the layout                                                 |
| `successful`                                                       | List[[models.SyncedWorkflowDto](../models/syncedworkflowdto.md)]   | :heavy_check_mark:                                                 | Successfully synced resources                                      |
| `failed`                                                           | List[[models.FailedWorkflowDto](../models/failedworkflowdto.md)]   | :heavy_check_mark:                                                 | Failed resource syncs                                              |
| `skipped`                                                          | List[[models.SkippedWorkflowDto](../models/skippedworkflowdto.md)] | :heavy_check_mark:                                                 | Skipped resources                                                  |
| `total_processed`                                                  | *float*                                                            | :heavy_check_mark:                                                 | Total number of resources processed                                |