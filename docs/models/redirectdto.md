# RedirectDto


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `url`                                                                       | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | URL for redirection. Must be a valid URL or start with / or {{ variable }}. |
| `target`                                                                    | [Optional[models.Target]](../models/target.md)                              | :heavy_minus_sign:                                                          | Target window for the redirection.                                          |