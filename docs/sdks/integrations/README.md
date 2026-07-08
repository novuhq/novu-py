# Integrations

## Overview

With the help of the Integration Store, you can easily integrate your favorite delivery provider. During the runtime of the API, the Integrations Store is responsible for storing the configurations of all the providers.
<https://docs.novu.co/platform/integrations/overview>

### Available Operations

* [list](#list) - List all integrations
* [create](#create) - Create an integration
* [update](#update) - Update an integration
* [delete](#delete) - Delete an integration
* [integrations_controller_auto_configure_integration](#integrations_controller_auto_configure_integration) - Auto-configure an integration for inbound webhooks
* [set_as_primary](#set_as_primary) - Update integration as primary
* [create_mobile_link](#create_mobile_link) - Issue a short-lived mobile setup link for an existing integration
* [integrations_controller_configure_integration_webhook](#integrations_controller_configure_integration_webhook) - Configure a chat integration webhook
* [list_active](#list_active) - List active integrations
* [generate_connect_o_auth_url](#generate_connect_o_auth_url) - Generate OAuth URL for a workspace/tenant connection
* [link_channel_endpoint](#link_channel_endpoint) - Issue a URL to link a subscriber chat identity
* [generate_link_user_o_auth_url](#generate_link_user_o_auth_url) - Generate OAuth URL to link a subscriber user identity
* [~~generate_chat_o_auth_url~~](#generate_chat_o_auth_url) - Generate chat OAuth URL :warning: **Deprecated**

## list

List all the channels integrations created in the organization. Only integration metadata is returned, credentials field is returned as an empty object.

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
    Each provider supports different credentials, check the provider documentation for more details. Only integration metadata is returned, credentials field is returned as an empty object.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_createIntegration" method="post" path="/v1/integrations" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.create(create_integration_request_dto={})

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
    Each provider supports different credentials, check the provider documentation for more details. Only integration metadata is returned, credentials field is returned as an empty object.

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
    This action is irreversible. Only integration metadata is returned, credentials field is returned as empty object.

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

## integrations_controller_auto_configure_integration

Auto-configure an integration by its unique key identifier **integrationId** for inbound webhook support. 
    This will automatically generate required webhook signing keys and configure webhook endpoints. Only integration metadata is returned, credentials field is returned as an empty object.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_autoConfigureIntegration" method="post" path="/v1/integrations/{integrationId}/auto-configure" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.integrations_controller_auto_configure_integration(integration_id="<id>")

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

**[models.IntegrationsControllerAutoConfigureIntegrationResponse](../../models/integrationscontrollerautoconfigureintegrationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## set_as_primary

Update an integration as **primary** by its unique key identifier **integrationId**. 
    This API will set the integration as primary for that channel in the current environment. 
    Primary integration is used to deliver notification for sms and email channels in the workflow. 
    Only integration metadata is returned, credentials field is returned as an empty object.

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

## create_mobile_link

Returns an opaque, single-use setup token plus a mobile URL for configuring an existing chat integration. Telegram is the only supported provider initially.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_createIntegrationMobileLink" method="post" path="/v1/integrations/{integrationIdentifier}/mobile-link" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.create_mobile_link(integration_identifier="<value>", issue_integration_mobile_link_request_dto={
        "subscriber_id": "subscriber-123",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `integration_identifier`                                                                            | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `issue_integration_mobile_link_request_dto`                                                         | [models.IssueIntegrationMobileLinkRequestDto](../../models/issueintegrationmobilelinkrequestdto.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `idempotency_key`                                                                                   | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | A header for idempotency purposes                                                                   |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.IntegrationsControllerCreateIntegrationMobileLinkResponse](../../models/integrationscontrollercreateintegrationmobilelinkresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## integrations_controller_configure_integration_webhook

Registers the Novu webhook URL with the chat provider for the specified integration. Telegram is the only supported provider initially.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_configureIntegrationWebhook" method="post" path="/v1/integrations/{integrationIdentifier}/webhook/configure" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.integrations_controller_configure_integration_webhook(integration_identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `integration_identifier`                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IntegrationsControllerConfigureIntegrationWebhookResponse](../../models/integrationscontrollerconfigureintegrationwebhookresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## list_active

List all the active integrations created in the organization. Only integration metadata is returned, credentials field is returned as an empty object.

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

## generate_connect_o_auth_url

Generate an OAuth URL that creates a workspace or tenant-level channel connection (Slack workspace install or MS Teams admin consent). 
    The generated URL expires after 5 minutes.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_generateConnectOAuthUrl" method="post" path="/v1/integrations/channel-connections/oauth" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.generate_connect_o_auth_url(generate_connect_oauth_url_request_dto={
        "subscriber_id": "subscriber-123",
        "integration_identifier": "<value>",
        "connection_identifier": "slack-connection-abc123",
        "context": {
            "key": "org-acme",
        },
        "scope": [
            "chat:write",
            "chat:write.public",
            "channels:read",
        ],
        "connection_mode": novu_py.GenerateConnectOauthURLRequestDtoConnectionMode.SHARED,
        "auto_link_user": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `generate_connect_oauth_url_request_dto`                                                      | [models.GenerateConnectOauthURLRequestDto](../../models/generateconnectoauthurlrequestdto.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A header for idempotency purposes                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.IntegrationsControllerGenerateConnectOAuthURLResponse](../../models/integrationscontrollergenerateconnectoauthurlresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## link_channel_endpoint

Returns a provider-specific URL the subscriber opens to link their chat identity. The integration provider is resolved from integrationIdentifier; Telegram returns a deep link.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_linkChannelEndpoint" method="post" path="/v1/integrations/channel-endpoints/link" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.link_channel_endpoint(link_channel_endpoint_request_dto={
        "integration_identifier": "telegram-bot",
        "subscriber_id": "subscriber-123",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `link_channel_endpoint_request_dto`                                                   | [models.LinkChannelEndpointRequestDto](../../models/linkchannelendpointrequestdto.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `idempotency_key`                                                                     | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A header for idempotency purposes                                                     |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.IntegrationsControllerLinkChannelEndpointResponse](../../models/integrationscontrollerlinkchannelendpointresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## generate_link_user_o_auth_url

Generate an OAuth URL that links a specific subscriber to their chat identity (Slack user ID or MS Teams user OID). 
    The generated URL expires after 5 minutes.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_generateLinkUserOAuthUrl" method="post" path="/v1/integrations/channel-endpoints/oauth" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.generate_link_user_o_auth_url(generate_link_user_oauth_url_request_dto={
        "subscriber_id": "subscriber-123",
        "integration_identifier": "<value>",
        "connection_identifier": "slack-connection-abc123",
        "context": {
            "key": "org-acme",
        },
        "user_scope": [
            "identity.basic",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `generate_link_user_oauth_url_request_dto`                                                      | [models.GenerateLinkUserOauthURLRequestDto](../../models/generatelinkuseroauthurlrequestdto.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `idempotency_key`                                                                               | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | A header for idempotency purposes                                                               |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.IntegrationsControllerGenerateLinkUserOAuthURLResponse](../../models/integrationscontrollergeneratelinkuseroauthurlresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## ~~generate_chat_o_auth_url~~

**Deprecated** — use `POST /integrations/channel-connections/oauth` (connect) or `POST /integrations/channel-endpoints/oauth` (link_user) instead.
    Generate an OAuth URL for chat integrations like Slack and MS Teams. 
    This URL allows subscribers to authorize the integration, enabling the system to send messages 
    through their chat workspace. The generated URL expires after 5 minutes.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="IntegrationsController_getChatOAuthUrl" method="post" path="/v1/integrations/chat/oauth" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.integrations.generate_chat_o_auth_url(generate_chat_oauth_url_request_dto={
        "subscriber_id": "subscriber-123",
        "integration_identifier": "<value>",
        "connection_identifier": "slack-connection-abc123",
        "context": {
            "key": "org-acme",
        },
        "scope": [
            "chat:write",
            "chat:write.public",
            "channels:read",
            "groups:read",
            "users:read",
            "users:read.email",
            "incoming-webhook",
        ],
        "user_scope": [
            "identity.basic",
        ],
        "mode": novu_py.Mode.LINK_USER,
        "connection_mode": novu_py.GenerateChatOauthURLRequestDtoConnectionMode.SHARED,
        "auto_link_user": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `generate_chat_oauth_url_request_dto`                                                   | [models.GenerateChatOauthURLRequestDto](../../models/generatechatoauthurlrequestdto.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `idempotency_key`                                                                       | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | A header for idempotency purposes                                                       |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.IntegrationsControllerGetChatOAuthURLResponse](../../models/integrationscontrollergetchatoauthurlresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |