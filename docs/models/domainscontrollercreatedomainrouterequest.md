# DomainsControllerCreateDomainRouteRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `domain`                                             | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `idempotency_key`                                    | *Optional[str]*                                      | :heavy_minus_sign:                                   | A header for idempotency purposes                    |
| `domain_route_dto`                                   | [models.DomainRouteDto](../models/domainroutedto.md) | :heavy_check_mark:                                   | N/A                                                  |