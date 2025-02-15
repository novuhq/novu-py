# Novu SDK

## Overview

Novu API: Novu REST API. Please see https://docs.novu.co/api-reference for more details.

Novu Documentation
<https://docs.novu.co>

### Available Operations

* [trigger](#trigger) - Trigger event
* [trigger_bulk](#trigger_bulk) - Bulk trigger event
* [trigger_broadcast](#trigger_broadcast) - Broadcast event to all
* [cancel](#cancel) - Cancel triggered event

## trigger


    Trigger event is the main (and only) way to send notifications to subscribers. 
    The trigger identifier is used to match the particular workflow associated with it. 
    Additional information can be passed according the body interface below.
    

### Example Usage

```python
import novu_py
from novu_py import Novu

with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.trigger(trigger_event_request_dto=novu_py.TriggerEventRequestDto(
        workflow_id="workflow_identifier",
        to={
            "subscriber_id": "<id>",
        },
        payload={
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
        overrides={
            "fcm": {
                "data": {
                    "key": "value",
                },
            },
        },
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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## trigger_bulk


      Using this endpoint you can trigger multiple events at once, to avoid multiple calls to the API.
      The bulk API is limited to 100 events per request.
    

### Example Usage

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
                to={
                    "subscriber_id": "<id>",
                },
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            ),
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
                to=[
                    {
                        "topic_key": "<value>",
                        "type": novu_py.TriggerRecipientsTypeEnum.SUBSCRIBER,
                    },
                ],
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            ),
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
                to=[
                    "SUBSCRIBER_ID",
                    "SUBSCRIBER_ID",
                ],
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
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

```python
from novu_py import Novu

with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.trigger_broadcast(trigger_event_to_all_request_dto={
        "name": "<value>",
        "payload": {
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
    })

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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## cancel


    Using a previously generated transactionId during the event trigger,
     will cancel any active or pending workflows. This is useful to cancel active digests, delays etc...
    

### Example Usage

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