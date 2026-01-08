# ChannelConnections

## Overview

### Available Operations

* [list](#list) - List all channel connections
* [create](#create) - Create a channel connection
* [retrieve](#retrieve) - Retrieve a channel connection
* [update](#update) - Update a channel connection
* [delete](#delete) - Delete a channel connection

## list

List all channel connections for a resource.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelConnectionsController_listChannelConnections" method="get" path="/v1/channel-connections" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_connections.list(request={
        "limit": 10,
        "subscriber_id": "subscriber-123",
        "channel": novu_py.QueryParamChannel.CHAT,
        "provider_id": novu_py.ProvidersIDEnum.SLACK,
        "integration_identifier": "slack-prod",
        "context_keys": [
            "tenant:org-123",
            "region:us-east-1",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                     | [models.ChannelConnectionsControllerListChannelConnectionsRequest](../../models/channelconnectionscontrollerlistchannelconnectionsrequest.md) | :heavy_check_mark:                                                                                                                            | The request object to use for the request.                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.ChannelConnectionsControllerListChannelConnectionsResponse](../../models/channelconnectionscontrollerlistchannelconnectionsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Create a new channel connection for a resource for given integration. Only one channel connection is allowed per resource and integration.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelConnectionsController_createChannelConnection" method="post" path="/v1/channel-connections" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_connections.create(create_channel_connection_request_dto={
        "identifier": "slack-prod-user123-abc4",
        "subscriber_id": "subscriber-123",
        "context": {
            "key": "org-acme",
        },
        "integration_identifier": "slack-prod",
        "workspace": {
            "id": "T123456",
            "name": "Acme HQ",
        },
        "auth": {
            "access_token": "Workspace access token",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `create_channel_connection_request_dto`                                                       | [models.CreateChannelConnectionRequestDto](../../models/createchannelconnectionrequestdto.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A header for idempotency purposes                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.ChannelConnectionsControllerCreateChannelConnectionResponse](../../models/channelconnectionscontrollercreatechannelconnectionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Retrieve a specific channel connection by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelConnectionsController_getChannelConnectionByIdentifier" method="get" path="/v1/channel-connections/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_connections.retrieve(identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the channel connection                     |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChannelConnectionsControllerGetChannelConnectionByIdentifierResponse](../../models/channelconnectionscontrollergetchannelconnectionbyidentifierresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update an existing channel connection by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelConnectionsController_updateChannelConnection" method="patch" path="/v1/channel-connections/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_connections.update(identifier="<value>", update_channel_connection_request_dto={
        "workspace": {
            "id": "T123456",
            "name": "Acme HQ",
        },
        "auth": {
            "access_token": "Workspace access token",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `identifier`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | The unique identifier of the channel connection                                               |
| `update_channel_connection_request_dto`                                                       | [models.UpdateChannelConnectionRequestDto](../../models/updatechannelconnectionrequestdto.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A header for idempotency purposes                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.ChannelConnectionsControllerUpdateChannelConnectionResponse](../../models/channelconnectionscontrollerupdatechannelconnectionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete a specific channel connection by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelConnectionsController_deleteChannelConnection" method="delete" path="/v1/channel-connections/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_connections.delete(identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the channel connection                     |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChannelConnectionsControllerDeleteChannelConnectionResponse](../../models/channelconnectionscontrollerdeletechannelconnectionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |