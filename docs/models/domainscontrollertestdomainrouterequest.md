# DomainsControllerTestDomainRouteRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `domain`                                                     | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `address`                                                    | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `idempotency_key`                                            | *Optional[str]*                                              | :heavy_minus_sign:                                           | A header for idempotency purposes                            |
| `test_domain_route_dto`                                      | [models.TestDomainRouteDto](../models/testdomainroutedto.md) | :heavy_check_mark:                                           | N/A                                                          |