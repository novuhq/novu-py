# CreateSubscriberRequestDto


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `subscriber_id`                           | *str*                                     | :heavy_check_mark:                        | Unique identifier of the subscriber       |
| `first_name`                              | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | First name of the subscriber              |
| `last_name`                               | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | Last name of the subscriber               |
| `email`                                   | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | Email address of the subscriber           |
| `phone`                                   | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | Phone number of the subscriber            |
| `avatar`                                  | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | Avatar URL or identifier                  |
| `timezone`                                | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | Timezone of the subscriber                |
| `locale`                                  | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | Locale of the subscriber                  |
| `data`                                    | Dict[str, *Any*]                          | :heavy_minus_sign:                        | Additional custom data for the subscriber |