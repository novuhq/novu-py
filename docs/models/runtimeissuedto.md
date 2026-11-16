# RuntimeIssueDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `issue_type`                                                       | [models.WorkflowIssueTypeEnum](../models/workflowissuetypeenum.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `variable_name`                                                    | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Variable associated with the issue                                 |
| `message`                                                          | *str*                                                              | :heavy_check_mark:                                                 | Human-readable issue message                                       |