# EnvironmentResponseDto


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `id`                                             | *str*                                            | :heavy_check_mark:                               | Unique identifier of the environment             | 60d5ecb8b3b3a30015f3e1a1                         |
| `name`                                           | *str*                                            | :heavy_check_mark:                               | Name of the environment                          | Production Environment                           |
| `organization_id`                                | *str*                                            | :heavy_check_mark:                               | Organization ID associated with the environment  | 60d5ecb8b3b3a30015f3e1a2                         |
| `identifier`                                     | *str*                                            | :heavy_check_mark:                               | Unique identifier for the environment            | prod-env-01                                      |
| `api_keys`                                       | List[[models.APIKeyDto](../models/apikeydto.md)] | :heavy_minus_sign:                               | List of API keys associated with the environment |                                                  |
| `parent_id`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Parent environment ID                            | 60d5ecb8b3b3a30015f3e1a3                         |
| `slug`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | URL-friendly slug for the environment            | production                                       |