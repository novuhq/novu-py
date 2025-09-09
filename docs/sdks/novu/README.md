# Novu SDK

## Overview

Novu API: Novu REST API. Please see https://docs.novu.co/api-reference for more details.

Novu Documentation
<https://docs.novu.co>

### Available Operations

* [inbound_webhooks_controller_handle_webhook](#inbound_webhooks_controller_handle_webhook)
* [trigger](#trigger) - Trigger event
* [cancel](#cancel) - Cancel triggered event
* [trigger_broadcast](#trigger_broadcast) - Broadcast event to all
* [trigger_bulk](#trigger_bulk) - Bulk trigger event

## inbound_webhooks_controller_handle_webhook

### Example Usage

<!-- UsageSnippet language="python" operationID="InboundWebhooksController_handleWebhook" method="post" path="/v2/inbound-webhooks/delivery-providers/{environmentId}/{integrationId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    novu.inbound_webhooks_controller_handle_webhook(environment_id="<id>", integration_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `integration_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## trigger

    Trigger event is the main (and only) way to send notifications to subscribers. The trigger identifier is used to match the particular workflow associated with it. Additional information can be passed according the body interface below.
    To prevent duplicate triggers, you can optionally pass a **transactionId** in the request body. If the same **transactionId** is used again, the trigger will be ignored. The retention period depends on your billing tier.

### Example Usage

<!-- UsageSnippet language="python" operationID="EventsController_trigger" method="post" path="/v1/events/trigger" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.trigger(trigger_event_request_dto=novu_py.TriggerEventRequestDto(
        workflow_id="workflow_identifier",
        payload={
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
        overrides=novu_py.Overrides(),
        to="SUBSCRIBER_ID",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `trigger_event_request_dto`                                             | [models.TriggerEventRequestDto](../../models/triggereventrequestdto.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `idempotency_key`                                                       | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | A header for idempotency purposes                                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.EventsControllerTriggerResponse](../../models/eventscontrollertriggerresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.PayloadValidationExceptionDto | 400                                  | application/json                     |
| models.ErrorDto                      | 414                                  | application/json                     |
| models.ErrorDto                      | 401, 403, 404, 405, 409, 413, 415    | application/json                     |
| models.ValidationErrorDto            | 422                                  | application/json                     |
| models.ErrorDto                      | 500                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## cancel


    Using a previously generated transactionId during the event trigger,
     will cancel any active or pending workflows. This is useful to cancel active digests, delays etc...
    

### Example Usage

<!-- UsageSnippet language="python" operationID="EventsController_cancel" method="delete" path="/v1/events/trigger/{transactionId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.cancel(transaction_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EventsControllerCancelResponse](../../models/eventscontrollercancelresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## trigger_broadcast

Trigger a broadcast event to all existing subscribers, could be used to send announcements, etc.

      In the future could be used to trigger events to a subset of subscribers based on defined filters.

### Example Usage

<!-- UsageSnippet language="python" operationID="EventsController_broadcastEventToAll" method="post" path="/v1/events/trigger/broadcast" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.trigger_broadcast(trigger_event_to_all_request_dto=novu_py.TriggerEventToAllRequestDto(
        name="<value>",
        payload={
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
        overrides=novu_py.TriggerEventToAllRequestDtoOverrides(
            **{
                "fcm": {
                    "data": {
                        "key": "value",
                    },
                },
            },
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `trigger_event_to_all_request_dto`                                                | [models.TriggerEventToAllRequestDto](../../models/triggereventtoallrequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EventsControllerBroadcastEventToAllResponse](../../models/eventscontrollerbroadcasteventtoallresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.PayloadValidationExceptionDto | 400                                  | application/json                     |
| models.ErrorDto                      | 414                                  | application/json                     |
| models.ErrorDto                      | 401, 403, 404, 405, 409, 413, 415    | application/json                     |
| models.ValidationErrorDto            | 422                                  | application/json                     |
| models.ErrorDto                      | 500                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## trigger_bulk


      Using this endpoint you can trigger multiple events at once, to avoid multiple calls to the API.
      The bulk API is limited to 100 events per request.
    

### Example Usage

<!-- UsageSnippet language="python" operationID="EventsController_triggerBulk" method="post" path="/v1/events/trigger/bulk" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.trigger_bulk(bulk_trigger_event_dto={
        "events": [
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides=novu_py.Overrides(),
                to="SUBSCRIBER_ID",
            ),
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides=novu_py.Overrides(),
                to="SUBSCRIBER_ID",
            ),
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides=novu_py.Overrides(),
                to="SUBSCRIBER_ID",
            ),
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `bulk_trigger_event_dto`                                            | [models.BulkTriggerEventDto](../../models/bulktriggereventdto.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EventsControllerTriggerBulkResponse](../../models/eventscontrollertriggerbulkresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.PayloadValidationExceptionDto | 400                                  | application/json                     |
| models.ErrorDto                      | 414                                  | application/json                     |
| models.ErrorDto                      | 401, 403, 404, 405, 409, 413, 415    | application/json                     |
| models.ValidationErrorDto            | 422                                  | application/json                     |
| models.ErrorDto                      | 500                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |