# APIKeyDto


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `key`                                | *str*                                | :heavy_check_mark:                   | API key                              | sk_test_1234567890abcdef             |
| `user_id`                            | *str*                                | :heavy_check_mark:                   | User ID associated with the API key  | 60d5ecb8b3b3a30015f3e1a4             |
| `hash`                               | *Optional[str]*                      | :heavy_minus_sign:                   | Hashed representation of the API key | hash_value_here                      |