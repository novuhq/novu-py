# Subscribers.Notifications

## Overview

### Available Operations

* [list](#list) - Retrieve subscriber notifications
* [delete](#delete) - Delete a notification
* [complete_action](#complete_action) - Complete a notification action
* [revert_action](#revert_action) - Revert a notification action
* [archive](#archive) - Archive a notification
* [mark_as_read](#mark_as_read) - Mark a notification as read
* [snooze](#snooze) - Snooze a notification
* [unarchive](#unarchive) - Unarchive a notification
* [mark_as_unread](#mark_as_unread) - Mark a notification as unread
* [unsnooze](#unsnooze) - Unsnooze a notification
* [archive_all](#archive_all) - Archive all notifications
* [count](#count) - Retrieve subscriber notifications count
* [delete_all](#delete_all) - Delete all notifications
* [mark_all_as_read](#mark_all_as_read) - Mark all notifications as read
* [archive_all_read](#archive_all_read) - Archive all read notifications
* [mark_as_seen](#mark_as_seen) - Mark notifications as seen
* [feed](#feed) - Retrieve subscriber notifications
* [unseen_count](#unseen_count) - Retrieve unseen notifications count

## list

Retrieve in-app (inbox) notifications for a subscriber by its unique key identifier **subscriberId**. 
    Supports filtering by tags, read/archived/snoozed/seen state, data attributes, severity, date range, and context keys.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_getSubscriberNotifications" method="get" path="/v2/subscribers/{subscriberId}/notifications" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.list(request={
        "subscriber_id": "<id>",
        "offset": 0,
        "created_gte": 1704067200000,
        "created_lte": 1735689599999,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                               | [models.SubscribersControllerGetSubscriberNotificationsRequest](../../models/subscriberscontrollergetsubscribernotificationsrequest.md) | :heavy_check_mark:                                                                                                                      | The request object to use for the request.                                                                                              |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.SubscribersControllerGetSubscriberNotificationsResponse](../../models/subscriberscontrollergetsubscribernotificationsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete a specific in-app (inbox) notification permanently by its unique identifier **notificationId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_deleteNotification" method="delete" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.delete(subscriber_id="<id>", notification_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the subscriber                                    |
| `notification_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the notification                                  |
| `context_keys`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Context keys for filtering                                          |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerDeleteNotificationResponse](../../models/subscriberscontrollerdeletenotificationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## complete_action

Mark a single in-app (inbox) notification's action (primary or secondary) as completed by its unique identifier **notificationId** and action type **actionType**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_completeNotificationAction" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/actions/{actionType}/complete" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.complete_action(request={
        "subscriber_id": "<id>",
        "notification_id": "<id>",
        "action_type": novu_py.ActionType.SECONDARY,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                               | [models.SubscribersControllerCompleteNotificationActionRequest](../../models/subscriberscontrollercompletenotificationactionrequest.md) | :heavy_check_mark:                                                                                                                      | The request object to use for the request.                                                                                              |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.SubscribersControllerCompleteNotificationActionResponse](../../models/subscriberscontrollercompletenotificationactionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## revert_action

Revert a single in-app (inbox) notification's action (primary or secondary) to pending state by its unique identifier **notificationId** and action type **actionType**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_revertNotificationAction" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/actions/{actionType}/revert" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.revert_action(request={
        "subscriber_id": "<id>",
        "notification_id": "<id>",
        "action_type": novu_py.PathParamActionType.PRIMARY,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                           | [models.SubscribersControllerRevertNotificationActionRequest](../../models/subscriberscontrollerrevertnotificationactionrequest.md) | :heavy_check_mark:                                                                                                                  | The request object to use for the request.                                                                                          |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.SubscribersControllerRevertNotificationActionResponse](../../models/subscriberscontrollerrevertnotificationactionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## archive

Archive a specific in-app (inbox) notification by its unique identifier **notificationId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_archiveNotification" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/archive" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.archive(subscriber_id="<id>", notification_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the subscriber                                    |
| `notification_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the notification                                  |
| `context_keys`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Context keys for filtering                                          |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerArchiveNotificationResponse](../../models/subscriberscontrollerarchivenotificationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## mark_as_read

Mark a specific in-app (inbox) notification as read by its unique identifier **notificationId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_markNotificationAsRead" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/read" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.mark_as_read(subscriber_id="<id>", notification_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the subscriber                                    |
| `notification_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the notification                                  |
| `context_keys`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Context keys for filtering                                          |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerMarkNotificationAsReadResponse](../../models/subscriberscontrollermarknotificationasreadresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## snooze

Snooze a specific in-app (inbox) notification by its unique identifier **notificationId** until a specified time.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_snoozeNotification" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/snooze" -->
```python
from novu_py import Novu
from novu_py.utils import parse_datetime


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.snooze(request={
        "subscriber_id": "<id>",
        "notification_id": "<id>",
        "snooze_subscriber_notification_dto": {
            "snooze_until": parse_datetime("2026-03-01T10:00:00Z"),
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                               | [models.SubscribersControllerSnoozeNotificationRequest](../../models/subscriberscontrollersnoozenotificationrequest.md) | :heavy_check_mark:                                                                                                      | The request object to use for the request.                                                                              |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.SubscribersControllerSnoozeNotificationResponse](../../models/subscriberscontrollersnoozenotificationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## unarchive

Unarchive a specific in-app (inbox) notification by its unique identifier **notificationId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_unarchiveNotification" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/unarchive" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.unarchive(subscriber_id="<id>", notification_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the subscriber                                    |
| `notification_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the notification                                  |
| `context_keys`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Context keys for filtering                                          |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerUnarchiveNotificationResponse](../../models/subscriberscontrollerunarchivenotificationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## mark_as_unread

Mark a specific in-app (inbox) notification as unread by its unique identifier **notificationId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_markNotificationAsUnread" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/unread" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.mark_as_unread(subscriber_id="<id>", notification_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the subscriber                                    |
| `notification_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the notification                                  |
| `context_keys`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Context keys for filtering                                          |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerMarkNotificationAsUnreadResponse](../../models/subscriberscontrollermarknotificationasunreadresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## unsnooze

Unsnooze a specific in-app (inbox) notification by its unique identifier **notificationId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_unsnoozeNotification" method="patch" path="/v2/subscribers/{subscriberId}/notifications/{notificationId}/unsnooze" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.unsnooze(subscriber_id="<id>", notification_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the subscriber                                    |
| `notification_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The identifier of the notification                                  |
| `context_keys`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Context keys for filtering                                          |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerUnsnoozeNotificationResponse](../../models/subscriberscontrollerunsnoozenotificationresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## archive_all

Archive all in-app (inbox) notifications matching the specified filters. Supports context-based filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_archiveAllNotifications" method="post" path="/v2/subscribers/{subscriberId}/notifications/archive" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.archive_all(subscriber_id="<id>", update_all_subscriber_notifications_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | The identifier of the subscriber                                                                  |
| `update_all_subscriber_notifications_dto`                                                         | [models.UpdateAllSubscriberNotificationsDto](../../models/updateallsubscribernotificationsdto.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `idempotency_key`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A header for idempotency purposes                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.SubscribersControllerArchiveAllNotificationsResponse](../../models/subscriberscontrollerarchiveallnotificationsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## count

Retrieve count of in-app (inbox) notifications for a subscriber by its unique key identifier **subscriberId**. 
    Supports multiple filters to count in-app (inbox) notifications by different criteria, including context keys.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_getSubscriberNotificationsCount" method="get" path="/v2/subscribers/{subscriberId}/notifications/count" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.count(subscriber_id="<id>", filters="[{\"read\":false,\"archived\":false},{\"tags\":[\"important\"]},{\"tags\":{\"and\":[{\"or\":[\"a\",\"b\"]},{\"or\":[\"c\"]}]}}]")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                           | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The identifier of the subscriber                                                                          |                                                                                                           |
| `filters`                                                                                                 | *str*                                                                                                     | :heavy_check_mark:                                                                                        | Array of filter objects (max 30) to count notifications by different criteria                             | [{"read":false,"archived":false},{"tags":["important"]},{"tags":{"and":[{"or":["a","b"]},{"or":["c"]}]}}] |
| `idempotency_key`                                                                                         | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | A header for idempotency purposes                                                                         |                                                                                                           |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.SubscribersControllerGetSubscriberNotificationsCountResponse](../../models/subscriberscontrollergetsubscribernotificationscountresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete_all

Permanently delete all in-app (inbox) notifications matching the specified filters. Supports context-based filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_deleteAllNotifications" method="post" path="/v2/subscribers/{subscriberId}/notifications/delete" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.delete_all(subscriber_id="<id>", update_all_subscriber_notifications_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | The identifier of the subscriber                                                                  |
| `update_all_subscriber_notifications_dto`                                                         | [models.UpdateAllSubscriberNotificationsDto](../../models/updateallsubscribernotificationsdto.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `idempotency_key`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A header for idempotency purposes                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.SubscribersControllerDeleteAllNotificationsResponse](../../models/subscriberscontrollerdeleteallnotificationsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## mark_all_as_read

Mark all in-app (inbox) notifications matching the specified filters as read. Supports context-based filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_markAllNotificationsAsRead" method="post" path="/v2/subscribers/{subscriberId}/notifications/read" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.mark_all_as_read(subscriber_id="<id>", update_all_subscriber_notifications_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | The identifier of the subscriber                                                                  |
| `update_all_subscriber_notifications_dto`                                                         | [models.UpdateAllSubscriberNotificationsDto](../../models/updateallsubscribernotificationsdto.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `idempotency_key`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A header for idempotency purposes                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.SubscribersControllerMarkAllNotificationsAsReadResponse](../../models/subscriberscontrollermarkallnotificationsasreadresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## archive_all_read

Archive all read in-app (inbox) notifications matching the specified filters. Supports context-based filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_archiveAllReadNotifications" method="post" path="/v2/subscribers/{subscriberId}/notifications/read-archive" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.archive_all_read(subscriber_id="<id>", update_all_subscriber_notifications_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | The identifier of the subscriber                                                                  |
| `update_all_subscriber_notifications_dto`                                                         | [models.UpdateAllSubscriberNotificationsDto](../../models/updateallsubscribernotificationsdto.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `idempotency_key`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A header for idempotency purposes                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.SubscribersControllerArchiveAllReadNotificationsResponse](../../models/subscriberscontrollerarchiveallreadnotificationsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## mark_as_seen

Mark specific and multiple in-app (inbox) notifications as seen. Supports context-based filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_markNotificationsAsSeen" method="post" path="/v2/subscribers/{subscriberId}/notifications/seen" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.mark_as_seen(subscriber_id="<id>", mark_subscriber_notifications_as_seen_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                     | *str*                                                                                               | :heavy_check_mark:                                                                                  | The identifier of the subscriber                                                                    |
| `mark_subscriber_notifications_as_seen_dto`                                                         | [models.MarkSubscriberNotificationsAsSeenDto](../../models/marksubscribernotificationsasseendto.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `idempotency_key`                                                                                   | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | A header for idempotency purposes                                                                   |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.SubscribersControllerMarkNotificationsAsSeenResponse](../../models/subscriberscontrollermarknotificationsasseenresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## feed

Retrieve subscriber in-app (inbox) notifications by its unique key identifier **subscriberId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_getNotificationsFeed" method="get" path="/v1/subscribers/{subscriberId}/notifications/feed" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.feed(request={
        "subscriber_id": "<id>",
        "page": 0,
        "payload": "btoa(JSON.stringify({ foo: 123 })) results in base64 encoded string like eyJmb28iOjEyM30=",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                       | [models.SubscribersV1ControllerGetNotificationsFeedRequest](../../models/subscribersv1controllergetnotificationsfeedrequest.md) | :heavy_check_mark:                                                                                                              | The request object to use for the request.                                                                                      |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.SubscribersV1ControllerGetNotificationsFeedResponse](../../models/subscribersv1controllergetnotificationsfeedresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## unseen_count

Retrieve unseen in-app (inbox) notifications count for a subscriber by its unique key identifier **subscriberId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_getUnseenCount" method="get" path="/v1/subscribers/{subscriberId}/notifications/unseen" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.unseen_count(subscriber_id="<id>", seen=False, limit=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `seen`                                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates whether to count seen notifications.                      |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | The maximum number of notifications to return.                      |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersV1ControllerGetUnseenCountResponse](../../models/subscribersv1controllergetunseencountresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |