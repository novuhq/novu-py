# InAppRenderOutput


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `subject`                                                | *Optional[str]*                                          | :heavy_minus_sign:                                       | Subject of the in-app notification                       |
| `body`                                                   | *str*                                                    | :heavy_check_mark:                                       | Body of the in-app notification                          |
| `avatar`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | Avatar for the in-app notification                       |
| `primary_action`                                         | [Optional[models.ActionDto]](../models/actiondto.md)     | :heavy_minus_sign:                                       | Primary action details                                   |
| `secondary_action`                                       | [Optional[models.ActionDto]](../models/actiondto.md)     | :heavy_minus_sign:                                       | Secondary action details                                 |
| `data`                                                   | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | Additional data                                          |
| `redirect`                                               | [Optional[models.RedirectDto]](../models/redirectdto.md) | :heavy_minus_sign:                                       | Redirect details                                         |