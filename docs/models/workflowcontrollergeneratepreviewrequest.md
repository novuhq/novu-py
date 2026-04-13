# WorkflowControllerGeneratePreviewRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `workflow_id`                                                              | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `step_id`                                                                  | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `idempotency_key`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | A header for idempotency purposes                                          |
| `generate_preview_request_dto`                                             | [models.GeneratePreviewRequestDto](../models/generatepreviewrequestdto.md) | :heavy_check_mark:                                                         | Preview generation details                                                 |