# ConfigureTelegramWebhookResponseDto


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `webhook_url`                                          | *str*                                                  | :heavy_check_mark:                                     | URL Novu registered with Telegram for incoming updates |
| `configured_at`                                        | *str*                                                  | :heavy_check_mark:                                     | ISO-8601 timestamp the webhook was configured at       |
| `bot_username`                                         | *str*                                                  | :heavy_check_mark:                                     | Resolved bot username from getMe                       |