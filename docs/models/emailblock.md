# EmailBlock


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `type`                                                             | [models.EmailBlockTypeEnum](../models/emailblocktypeenum.md)       | :heavy_check_mark:                                                 | Type of the email block                                            |
| `content`                                                          | *str*                                                              | :heavy_check_mark:                                                 | Content of the email block                                         |
| `url`                                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | URL associated with the email block, if any                        |
| `styles`                                                           | [Optional[models.EmailBlockStyles]](../models/emailblockstyles.md) | :heavy_minus_sign:                                                 | Styles applied to the email block                                  |