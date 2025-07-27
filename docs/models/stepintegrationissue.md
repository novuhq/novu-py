# StepIntegrationIssue


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `issue_type`                                                     | [models.IntegrationIssueEnum](../models/integrationissueenum.md) | :heavy_check_mark:                                               | Type of integration issue                                        |
| `variable_name`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Name of the variable related to the issue                        |
| `message`                                                        | *str*                                                            | :heavy_check_mark:                                               | Detailed message describing the issue                            |