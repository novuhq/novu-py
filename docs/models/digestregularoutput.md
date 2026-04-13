# DigestRegularOutput


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `amount`                                                       | *float*                                                        | :heavy_check_mark:                                             | Amount of time units                                           |
| `unit`                                                         | [models.TimeUnitEnum](../models/timeunitenum.md)               | :heavy_check_mark:                                             | Time unit                                                      |
| `digest_key`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | Optional digest key                                            |
| `look_back_window`                                             | [Optional[models.LookBackWindow]](../models/lookbackwindow.md) | :heavy_minus_sign:                                             | Look back window configuration                                 |