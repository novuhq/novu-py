# CreateDomainDto


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `name`                                                                                  | *str*                                                                                   | :heavy_check_mark:                                                                      | The domain name (e.g. "recent.dev")                                                     |
| `data`                                                                                  | Dict[str, *str*]                                                                        | :heavy_minus_sign:                                                                      | Optional string key-value metadata (max 10 keys, 500 characters total for keys+values). |