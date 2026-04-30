# Domains.Routes

## Overview

### Available Operations

* [list](#list) - List routes for a domain
* [create](#create) - Create a route
* [retrieve](#retrieve) - Retrieve a route by address
* [update](#update) - Update a route
* [delete](#delete) - Delete a route
* [test](#test) - Test an inbound route

## list

Returns a paginated list of routes attached to the domain. Optionally filter by an agent identifier to find routes pointing to a specific agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_listDomainRoutes" method="get" path="/v1/domains/{domain}/routes" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.routes.list(request={
        "domain": "fearless-fishery.com",
        "limit": 10,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.DomainsControllerListDomainRoutesRequest](../../models/domainscontrollerlistdomainroutesrequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.DomainsControllerListDomainRoutesResponse](../../models/domainscontrollerlistdomainroutesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Creates a route on the domain that forwards inbound mail addressed to `<address>@<domain>` to either a webhook or an agent. Each address on a domain may only have a single route.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_createDomainRoute" method="post" path="/v1/domains/{domain}/routes" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.routes.create(domain="radiant-solvency.net", domain_route_dto={
        "address": "6581 Birch Road",
        "type": novu_py.DomainRouteDtoType.WEBHOOK,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `domain_route_dto`                                                  | [models.DomainRouteDto](../../models/domainroutedto.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DomainsControllerCreateDomainRouteResponse](../../models/domainscontrollercreatedomainrouteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Returns the route bound to `<address>@<domain>`. Use `*` as the address to retrieve the wildcard route for the domain.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_getDomainRoute" method="get" path="/v1/domains/{domain}/routes/{address}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.routes.retrieve(domain="adolescent-petal.net", address="42531 Green Lane")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `address`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DomainsControllerGetDomainRouteResponse](../../models/domainscontrollergetdomainrouteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Updates the destination of the route bound to `<address>@<domain>`. The address itself is the resource identity and cannot be changed; delete and recreate the route to rename it.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_updateDomainRoute" method="patch" path="/v1/domains/{domain}/routes/{address}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.routes.update(domain="cavernous-cycle.com", address="70213 Gerlach Rue", update_domain_route_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `address`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `update_domain_route_dto`                                           | [models.UpdateDomainRouteDto](../../models/updatedomainroutedto.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DomainsControllerUpdateDomainRouteResponse](../../models/domainscontrollerupdatedomainrouteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Removes the route bound to `<address>@<domain>`. Inbound mail for that address will no longer be processed.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_deleteDomainRoute" method="delete" path="/v1/domains/{domain}/routes/{address}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.routes.delete(domain="corrupt-avalanche.biz", address="753 W 4th Avenue")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `address`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DomainsControllerDeleteDomainRouteResponse](../../models/domainscontrollerdeletedomainrouteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## test

Sends a synthetic inbound email through the same delivery path as production (outbound webhooks for webhook routes, signed HTTP to the agent for agent routes). Use `dryRun: true` to preview the payload without delivering.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_testDomainRoute" method="post" path="/v1/domains/{domain}/routes/{address}/test" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.routes.test(domain="exalted-bonfire.com", address="90499 Rowan Close", test_domain_route_dto={
        "from_": {
            "address": "58851 Konopelski Overpass",
        },
        "subject": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `address`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `test_domain_route_dto`                                             | [models.TestDomainRouteDto](../../models/testdomainroutedto.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DomainsControllerTestDomainRouteResponse](../../models/domainscontrollertestdomainrouteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |