# Agents.Integrations

## Overview

### Available Operations

* [create](#create) - Create an agent integration
* [list](#list) - List agent integrations
* [update](#update) - Update an agent integration
* [delete](#delete) - Delete an agent integration

## create

Create a link between an agent (by identifier) and an integration (by integration **identifier**, not the internal _id).

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentIntegrationsController_addAgentIntegration" method="post" path="/v1/agents/{identifier}/integrations" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.integrations.create(identifier="<value>", add_agent_integration_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `identifier`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `add_agent_integration_request_dto`                                                   | [models.AddAgentIntegrationRequestDto](../../models/addagentintegrationrequestdto.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `idempotency_key`                                                                     | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A header for idempotency purposes                                                     |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AgentIntegrationsControllerAddAgentIntegrationResponse](../../models/agentintegrationscontrolleraddagentintegrationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## list

Retrieve integration links for an agent identified by its external identifier. Supports cursor pagination via **after**, **before**, **limit**, **orderBy**, and **orderDirection**.

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentIntegrationsController_listAgentIntegrations" method="get" path="/v1/agents/{identifier}/integrations" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.integrations.list(request={
        "identifier": "<value>",
        "limit": 10,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                 | [models.AgentIntegrationsControllerListAgentIntegrationsRequest](../../models/agentintegrationscontrollerlistagentintegrationsrequest.md) | :heavy_check_mark:                                                                                                                        | The request object to use for the request.                                                                                                |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |

### Response

**[models.AgentIntegrationsControllerListAgentIntegrationsResponse](../../models/agentintegrationscontrollerlistagentintegrationsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## update

Update which integration a link points to (by integration **identifier**, not the internal _id).

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentIntegrationsController_updateAgentIntegration" method="patch" path="/v1/agents/{identifier}/integrations/{agentIntegrationId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.integrations.update(identifier="<value>", agent_integration_id="<id>", update_agent_integration_request_dto={
        "integration_identifier": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `identifier`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `agent_integration_id`                                                                      | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `update_agent_integration_request_dto`                                                      | [models.UpdateAgentIntegrationRequestDto](../../models/updateagentintegrationrequestdto.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `idempotency_key`                                                                           | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | A header for idempotency purposes                                                           |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.AgentIntegrationsControllerUpdateAgentIntegrationResponse](../../models/agentintegrationscontrollerupdateagentintegrationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## delete

Delete a specific agent-integration link by its document id.

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentIntegrationsController_removeAgentIntegration" method="delete" path="/v1/agents/{identifier}/integrations/{agentIntegrationId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.integrations.delete(identifier="<value>", agent_integration_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `agent_integration_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentIntegrationsControllerRemoveAgentIntegrationResponse](../../models/agentintegrationscontrollerremoveagentintegrationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |