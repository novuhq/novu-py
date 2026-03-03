# DiffEnvironmentResponseDto


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `source_environment_id`                                                    | *str*                                                                      | :heavy_check_mark:                                                         | Source environment ID                                                      |
| `target_environment_id`                                                    | *str*                                                                      | :heavy_check_mark:                                                         | Target environment ID                                                      |
| `resources`                                                                | List[[models.ResourceDiffResultDto](../models/resourcediffresultdto.md)]   | :heavy_check_mark:                                                         | Diff resources by resource type                                            |
| `summary`                                                                  | [models.EnvironmentDiffSummaryDto](../models/environmentdiffsummarydto.md) | :heavy_check_mark:                                                         | Overall summary                                                            |