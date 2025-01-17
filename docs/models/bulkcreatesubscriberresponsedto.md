# BulkCreateSubscriberResponseDto


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `updated`                                                                      | List[[models.UpdatedSubscriberDto](../models/updatedsubscriberdto.md)]         | :heavy_check_mark:                                                             | An array of subscribers that were successfully updated.                        |
| `created`                                                                      | List[[models.CreatedSubscriberDto](../models/createdsubscriberdto.md)]         | :heavy_check_mark:                                                             | An array of subscribers that were successfully created.                        |
| `failed`                                                                       | List[[models.FailedOperationDto](../models/failedoperationdto.md)]             | :heavy_check_mark:                                                             | An array of failed operations with error messages and optional subscriber IDs. |