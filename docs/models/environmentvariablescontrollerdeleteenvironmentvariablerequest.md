# EnvironmentVariablesControllerDeleteEnvironmentVariableRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `variable_key`                                             | *str*                                                      | :heavy_check_mark:                                         | The unique key of the environment variable (e.g. BASE_URL) | BASE_URL                                                   |
| `idempotency_key`                                          | *Optional[str]*                                            | :heavy_minus_sign:                                         | A header for idempotency purposes                          |                                                            |