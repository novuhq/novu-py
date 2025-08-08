# Integrations
(*integrations*)

## Overview

With the help of the Integration Store, you can easily integrate your favorite delivery provider. During the runtime of the API, the Integrations Store is responsible for storing the configurations of all the providers.
<https://docs.novu.co/platform/integrations/overview>

### Available Operations

* [list](#list) - List all integrations
* [create](#create) - Create an integration
* [update](#update) - Update an integration
* [delete](#delete) - Delete an integration
* [set_as_primary](#set_as_primary) - Update integration as primary
* [list_active](#list_active) - List active integrations

## list

List all the channels integrations created in the organization

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_listIntegrations" method="get" path="/v1/integrations" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IntegrationsControllerListIntegrationsResponse](../../models/integrationscontrollerlistintegrationsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Create an integration for the current environment the user is based on the API key provided. 
    Each provider supports different credentials, check the provider documentation for more details.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_createIntegration" method="post" path="/v1/integrations" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.create(create_integration_request_dto={
        "provider_id": "<id>",
        "channel": novu_py.CreateIntegrationRequestDtoChannel.EMAIL,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `create_integration_request_dto`                                                  | [models.CreateIntegrationRequestDto](../../models/createintegrationrequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.IntegrationsControllerCreateIntegrationResponse](../../models/integrationscontrollercreateintegrationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update an integration by its unique key identifier **integrationId**. 
    Each provider supports different credentials, check the provider documentation for more details.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_updateIntegrationById" method="put" path="/v1/integrations/{integrationId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.update(integration_id="<id>", update_integration_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `integration_id`                                                                  | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `update_integration_request_dto`                                                  | [models.UpdateIntegrationRequestDto](../../models/updateintegrationrequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.IntegrationsControllerUpdateIntegrationByIDResponse](../../models/integrationscontrollerupdateintegrationbyidresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## delete

Delete an integration by its unique key identifier **integrationId**. 
    This action is irreversible.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_removeIntegration" method="delete" path="/v1/integrations/{integrationId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.delete(integration_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `integration_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IntegrationsControllerRemoveIntegrationResponse](../../models/integrationscontrollerremoveintegrationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## set_as_primary

Update an integration as **primary** by its unique key identifier **integrationId**. 
    This API will set the integration as primary for that channel in the current environment. 
    Primary integration is used to deliver notification for sms and email channels in the workflow.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_setIntegrationAsPrimary" method="post" path="/v1/integrations/{integrationId}/set-primary" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.set_as_primary(integration_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `integration_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IntegrationsControllerSetIntegrationAsPrimaryResponse](../../models/integrationscontrollersetintegrationasprimaryresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## list_active

List all the active integrations created in the organization

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_getActiveIntegrations" method="get" path="/v1/integrations/active" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.list_active()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IntegrationsControllerGetActiveIntegrationsResponse](../../models/integrationscontrollergetactiveintegrationsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |