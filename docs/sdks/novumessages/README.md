# ~~Subscribers.Messages~~

> [!WARNING]
> This SDK is **DEPRECATED**

## Overview

### Available Operations

* [~~update_as_seen~~](#update_as_seen) - Update notification action status :warning: **Deprecated**
* [~~mark_all~~](#mark_all) - Update all notifications state :warning: **Deprecated**
* [~~mark_all_as~~](#mark_all_as) - Update notifications state :warning: **Deprecated**

## ~~update_as_seen~~

This API is deprecated, use v2 API instead. Update in-app notification's action status by its unique key identifier **messageId** and type field **type**. 
      **type** field can be **primary** or **secondary**

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_markActionAsSeen" method="post" path="/v1/subscribers/{subscriberId}/messages/{messageId}/actions/{type}" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.messages.update_as_seen(request={
        "message_id": "<id>",
        "type": "<value>",
        "subscriber_id": "<id>",
        "mark_message_action_as_seen_dto": {
            "status": novu_py.MarkMessageActionAsSeenDtoStatus.PENDING,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                               | [models.SubscribersV1ControllerMarkActionAsSeenRequest](../../models/subscribersv1controllermarkactionasseenrequest.md) | :heavy_check_mark:                                                                                                      | The request object to use for the request.                                                                              |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.SubscribersV1ControllerMarkActionAsSeenResponse](../../models/subscribersv1controllermarkactionasseenresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## ~~mark_all~~

This API is deprecated, use v2 API instead. Update all subscriber in-app notifications state such as read, unread, seen or unseen by **subscriberId**.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_markAllUnreadAsRead" method="post" path="/v1/subscribers/{subscriberId}/messages/mark-all" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.messages.mark_all(subscriber_id="<id>", mark_all_message_as_request_dto={
        "mark_as": novu_py.MarkAs.READ,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `subscriber_id`                                                                 | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `mark_all_message_as_request_dto`                                               | [models.MarkAllMessageAsRequestDto](../../models/markallmessageasrequestdto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `idempotency_key`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | A header for idempotency purposes                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersV1ControllerMarkAllUnreadAsReadResponse](../../models/subscribersv1controllermarkallunreadasreadresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## ~~mark_all_as~~

This API is deprecated, use v2 API instead. Update subscriber's multiple in-app notifications state such as seen, read, unseen or unread by **subscriberId**. 
      **messageId** is of type mongodbId of notifications.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_markMessagesAs" method="post" path="/v1/subscribers/{subscriberId}/messages/mark-as" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.messages.mark_all_as(subscriber_id="<id>", message_mark_as_request_dto={
        "message_id": [],
        "mark_as": novu_py.MessageMarkAsRequestDtoMarkAs.SEEN,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `subscriber_id`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `message_mark_as_request_dto`                                             | [models.MessageMarkAsRequestDto](../../models/messagemarkasrequestdto.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `idempotency_key`                                                         | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A header for idempotency purposes                                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SubscribersV1ControllerMarkMessagesAsResponse](../../models/subscribersv1controllermarkmessagesasresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |