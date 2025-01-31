# SubscribersV1ControllerChatOauthCallbackRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `subscriber_id`                                              | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `provider_id`                                                | *Any*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `hmac_hash`                                                  | *str*                                                        | :heavy_check_mark:                                           | HMAC hash for the request                                    |
| `environment_id`                                             | *str*                                                        | :heavy_check_mark:                                           | The ID of the environment, must be a valid MongoDB ID        |
| `code`                                                       | *str*                                                        | :heavy_check_mark:                                           | Optional authorization code returned from the OAuth provider |
| `integration_identifier`                                     | *Optional[str]*                                              | :heavy_minus_sign:                                           | Optional integration identifier                              |
| `idempotency_key`                                            | *Optional[str]*                                              | :heavy_minus_sign:                                           | A header for idempotency purposes                            |