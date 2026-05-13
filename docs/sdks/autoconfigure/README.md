# Domains.AutoConfigure

## Overview

### Available Operations

* [retrieve](#retrieve) - Retrieve auto-configuration availability
* [start](#start) - Start DNS auto-configuration

## retrieve

Returns whether DNS auto-configuration (Domain Connect) is available for this domain. When `available` is `false`, `manualRecords` lists the DNS records the customer must add manually.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_getDomainAutoConfigure" method="get" path="/v1/domains/{domain}/auto-configure" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.auto_configure.retrieve(domain="hidden-subsidy.info")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `domain`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DomainsControllerGetDomainAutoConfigureResponse](../../models/domainscontrollergetdomainautoconfigureresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## start

Generates a signed redirect URL the customer can follow to apply Novu DNS records at their DNS provider. After the provider completes the flow, it redirects back to `redirectUri`.

### Example Usage

<!-- UsageSnippet language="python" operationID="DomainsController_startDomainAutoConfigure" method="post" path="/v1/domains/{domain}/auto-configure/start" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.domains.auto_configure.start(domain="criminal-other.name", create_domain_connect_apply_url_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `domain`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `create_domain_connect_apply_url_dto`                                                   | [models.CreateDomainConnectApplyURLDto](../../models/createdomainconnectapplyurldto.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `idempotency_key`                                                                       | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | A header for idempotency purposes                                                       |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.DomainsControllerStartDomainAutoConfigureResponse](../../models/domainscontrollerstartdomainautoconfigureresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |