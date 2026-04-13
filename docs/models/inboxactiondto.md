# InboxActionDto


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `label`                                                  | *str*                                                    | :heavy_check_mark:                                       | Label of the action button                               |
| `is_completed`                                           | *bool*                                                   | :heavy_check_mark:                                       | Whether the action has been completed                    |
| `redirect`                                               | [Optional[models.RedirectDto]](../models/redirectdto.md) | :heavy_minus_sign:                                       | Redirect configuration for the action                    |