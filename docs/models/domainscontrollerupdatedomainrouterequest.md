# DomainsControllerUpdateDomainRouteRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `domain`                                                         | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `address`                                                        | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `idempotency_key`                                                | *Optional[str]*                                                  | :heavy_minus_sign:                                               | A header for idempotency purposes                                |
| `update_domain_route_dto`                                        | [models.UpdateDomainRouteDto](../models/updatedomainroutedto.md) | :heavy_check_mark:                                               | N/A                                                              |