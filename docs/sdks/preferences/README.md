# Preferences
(*subscribers.preferences*)

## Overview

### Available Operations

* [list](#list) - Retrieve subscriber preferences
* [update](#update) - Update subscriber preferences
* [bulk_update](#bulk_update) - Bulk update subscriber preferences

## list

Retrieve subscriber channel preferences by its unique key identifier **subscriberId**. 
    This API returns all five channels preferences for all workflows and global preferences.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_getSubscriberPreferences" method="get" path="/v2/subscribers/{subscriberId}/preferences" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.preferences.list(subscriber_id="<id>", criticality=novu_py.Criticality.NON_CRITICAL)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `criticality`                                                       | [Optional[models.Criticality]](../../models/criticality.md)         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerGetSubscriberPreferencesResponse](../../models/subscriberscontrollergetsubscriberpreferencesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update subscriber preferences by its unique key identifier **subscriberId**. 
    **workflowId** is optional field, if provided, this API will update that workflow preference, 
    otherwise it will update global preferences

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_updateSubscriberPreferences" method="patch" path="/v2/subscribers/{subscriberId}/preferences" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.preferences.update(subscriber_id="<id>", patch_subscriber_preferences_dto={
        "schedule": {
            "is_enabled": True,
            "weekly_schedule": {
                "monday": {
                    "is_enabled": True,
                    "hours": [
                        {
                            "start": "09:00 AM",
                            "end": "05:00 PM",
                        },
                    ],
                },
                "tuesday": {
                    "is_enabled": True,
                    "hours": [
                        {
                            "start": "09:00 AM",
                            "end": "05:00 PM",
                        },
                    ],
                },
                "wednesday": {
                    "is_enabled": True,
                    "hours": [
                        {
                            "start": "09:00 AM",
                            "end": "05:00 PM",
                        },
                    ],
                },
                "thursday": {
                    "is_enabled": True,
                    "hours": [
                        {
                            "start": "09:00 AM",
                            "end": "05:00 PM",
                        },
                    ],
                },
                "friday": {
                    "is_enabled": True,
                    "hours": [
                        {
                            "start": "09:00 AM",
                            "end": "05:00 PM",
                        },
                    ],
                },
                "saturday": {
                    "is_enabled": True,
                    "hours": [
                        {
                            "start": "09:00 AM",
                            "end": "05:00 PM",
                        },
                    ],
                },
                "sunday": {
                    "is_enabled": True,
                    "hours": [
                        {
                            "start": "09:00 AM",
                            "end": "05:00 PM",
                        },
                    ],
                },
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `patch_subscriber_preferences_dto`                                                    | [models.PatchSubscriberPreferencesDto](../../models/patchsubscriberpreferencesdto.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `idempotency_key`                                                                     | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A header for idempotency purposes                                                     |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.SubscribersControllerUpdateSubscriberPreferencesResponse](../../models/subscriberscontrollerupdatesubscriberpreferencesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## bulk_update

Bulk update subscriber preferences by its unique key identifier **subscriberId**. 
    This API allows updating multiple workflow preferences in a single request.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_bulkUpdateSubscriberPreferences" method="patch" path="/v2/subscribers/{subscriberId}/preferences/bulk" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.preferences.bulk_update(subscriber_id="<id>", bulk_update_subscriber_preferences_dto={
        "preferences": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                 | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `bulk_update_subscriber_preferences_dto`                                                        | [models.BulkUpdateSubscriberPreferencesDto](../../models/bulkupdatesubscriberpreferencesdto.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `idempotency_key`                                                                               | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | A header for idempotency purposes                                                               |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.SubscribersControllerBulkUpdateSubscriberPreferencesResponse](../../models/subscriberscontrollerbulkupdatesubscriberpreferencesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |