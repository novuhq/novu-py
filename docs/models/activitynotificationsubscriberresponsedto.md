# ActivityNotificationSubscriberResponseDto


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `first_name`                                         | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | First name of the subscriber                         |
| `subscriber_id`                                      | *str*                                                | :heavy_check_mark:                                   | External unique identifier of the subscriber         |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | Internal to Novu unique identifier of the subscriber |
| `last_name`                                          | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Last name of the subscriber                          |
| `email`                                              | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Email address of the subscriber                      |
| `phone`                                              | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Phone number of the subscriber                       |