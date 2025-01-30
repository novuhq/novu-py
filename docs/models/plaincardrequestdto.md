# PlainCardRequestDto


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `timestamp`                                                | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `card_keys`                                                | List[*str*]                                                | :heavy_minus_sign:                                         | N/A                                                        |
| `customer`                                                 | [OptionalNullable[models.Customer]](../models/customer.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `tenant`                                                   | [OptionalNullable[models.Tenant]](../models/tenant.md)     | :heavy_minus_sign:                                         | N/A                                                        |
| `thread`                                                   | [OptionalNullable[models.Thread]](../models/thread.md)     | :heavy_minus_sign:                                         | N/A                                                        |