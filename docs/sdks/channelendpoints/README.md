# ChannelEndpoints

## Overview

### Available Operations

* [list](#list) - List all channel endpoints
* [create](#create) - Create a channel endpoint
* [retrieve](#retrieve) - Retrieve a channel endpoint
* [update](#update) - Update a channel endpoint
* [delete](#delete) - Delete a channel endpoint

## list

List all channel endpoints for a resource based on query filters.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelEndpointsController_listChannelEndpoints" method="get" path="/v1/channel-endpoints" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_endpoints.list(request={
        "limit": 10,
        "subscriber_id": "subscriber-123",
        "context_keys": [
            "tenant:org-123",
            "region:us-east-1",
        ],
        "provider_id": novu_py.ProvidersIDEnum.SLACK,
        "integration_identifier": "slack-prod",
        "connection_identifier": "slack-connection-abc123",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                             | [models.ChannelEndpointsControllerListChannelEndpointsRequest](../../models/channelendpointscontrollerlistchannelendpointsrequest.md) | :heavy_check_mark:                                                                                                                    | The request object to use for the request.                                                                                            |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.ChannelEndpointsControllerListChannelEndpointsResponse](../../models/channelendpointscontrollerlistchannelendpointsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Create a new channel endpoint for a resource.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelEndpointsController_createChannelEndpoint" method="post" path="/v1/channel-endpoints" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_endpoints.create(request_body={
        "subscriber_id": "subscriber-123",
        "integration_identifier": "slack-prod",
        "type": novu_py.CreateSlackChannelEndpointDtoType.SLACK_CHANNEL,
        "endpoint": {
            "channel_id": "C123456789",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                  | [models.ChannelEndpointsControllerCreateChannelEndpointRequestBody](../../models/channelendpointscontrollercreatechannelendpointrequestbody.md) | :heavy_check_mark:                                                                                                                              | Channel endpoint creation request. The structure varies based on the type field.                                                                |
| `idempotency_key`                                                                                                                               | *Optional[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | A header for idempotency purposes                                                                                                               |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |

### Response

**[models.ChannelEndpointsControllerCreateChannelEndpointResponse](../../models/channelendpointscontrollercreatechannelendpointresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Retrieve a specific channel endpoint by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelEndpointsController_getChannelEndpoint" method="get" path="/v1/channel-endpoints/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_endpoints.retrieve(identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the channel endpoint                       |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChannelEndpointsControllerGetChannelEndpointResponse](../../models/channelendpointscontrollergetchannelendpointresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update an existing channel endpoint by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelEndpointsController_updateChannelEndpoint" method="patch" path="/v1/channel-endpoints/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_endpoints.update(identifier="<value>", update_channel_endpoint_request_dto={
        "endpoint": {
            "user_id": "U123456789",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `identifier`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | The unique identifier of the channel endpoint                                             |
| `update_channel_endpoint_request_dto`                                                     | [models.UpdateChannelEndpointRequestDto](../../models/updatechannelendpointrequestdto.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `idempotency_key`                                                                         | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | A header for idempotency purposes                                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.ChannelEndpointsControllerUpdateChannelEndpointResponse](../../models/channelendpointscontrollerupdatechannelendpointresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete a specific channel endpoint by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChannelEndpointsController_deleteChannelEndpoint" method="delete" path="/v1/channel-endpoints/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.channel_endpoints.delete(identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the channel endpoint                       |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChannelEndpointsControllerDeleteChannelEndpointResponse](../../models/channelendpointscontrollerdeletechannelendpointresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |