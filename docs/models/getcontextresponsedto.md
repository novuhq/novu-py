# GetContextResponseDto


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `type`                                      | *str*                                       | :heavy_check_mark:                          | Context type (e.g., tenant, app, workspace) |
| `id`                                        | *str*                                       | :heavy_check_mark:                          | Unique identifier for this context          |
| `data`                                      | Dict[str, *Any*]                            | :heavy_check_mark:                          | Custom data associated with this context    |
| `created_at`                                | *str*                                       | :heavy_check_mark:                          | Creation timestamp                          |
| `updated_at`                                | *str*                                       | :heavy_check_mark:                          | Last update timestamp                       |