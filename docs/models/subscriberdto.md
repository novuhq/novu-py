# SubscriberDto


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | The identifier of the subscriber          | 64da692e9a94fb2e6449ad07                  |
| `subscriber_id`                           | *str*                                     | :heavy_check_mark:                        | The external identifier of the subscriber | user-123                                  |
| `avatar`                                  | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | The avatar URL of the subscriber          | https://example.com/avatar.png            |
| `first_name`                              | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | The first name of the subscriber          | John                                      |
| `last_name`                               | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | The last name of the subscriber           | Doe                                       |
| `email`                                   | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | The email of the subscriber               | john@example.com                          |