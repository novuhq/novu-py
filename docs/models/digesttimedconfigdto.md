# DigestTimedConfigDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `at_time`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Time at which the digest is triggered                              |
| `week_days`                                                        | List[[models.WeekDays](../models/weekdays.md)]                     | :heavy_minus_sign:                                                 | Days of the week for the digest                                    |
| `month_days`                                                       | List[*float*]                                                      | :heavy_minus_sign:                                                 | Specific days of the month for the digest                          |
| `ordinal`                                                          | [Optional[models.OrdinalEnum]](../models/ordinalenum.md)           | :heavy_minus_sign:                                                 | Ordinal position for the digest                                    |
| `ordinal_value`                                                    | [Optional[models.OrdinalValueEnum]](../models/ordinalvalueenum.md) | :heavy_minus_sign:                                                 | Value of the ordinal                                               |
| `monthly_type`                                                     | [Optional[models.MonthlyTypeEnum]](../models/monthlytypeenum.md)   | :heavy_minus_sign:                                                 | Type of monthly schedule                                           |
| `cron_expression`                                                  | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Cron expression for scheduling                                     |