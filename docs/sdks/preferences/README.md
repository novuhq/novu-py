# Preferences
(*subscribers.preferences*)

## Overview

### Available Operations

* [list](#list) - Get subscriber preferences
* [update_global](#update_global) - Update subscriber global preferences
* [retrieve_by_level](#retrieve_by_level) - Get subscriber preferences by level
* [update_legacy](#update_legacy) - Update subscriber preference
* [retrieve](#retrieve) - Get subscriber preferences
* [update](#update) - Update subscriber global or workflow specific preferences

## list

Get subscriber preferences

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.preferences.list(subscriber_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                                           | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `include_inactive_channels`                                                                                               | *Optional[bool]*                                                                                                          | :heavy_minus_sign:                                                                                                        | A flag which specifies if the inactive workflow channels should be included in the retrieved preferences. Default is true |
| `idempotency_key`                                                                                                         | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | A header for idempotency purposes                                                                                         |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.SubscribersV1ControllerListSubscriberPreferencesResponse](../../models/subscribersv1controllerlistsubscriberpreferencesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update_global

Update subscriber global preferences

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.preferences.update_global(subscriber_id="<id>", update_subscriber_global_preferences_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                                   | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `update_subscriber_global_preferences_request_dto`                                                                | [models.UpdateSubscriberGlobalPreferencesRequestDto](../../models/updatesubscriberglobalpreferencesrequestdto.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `idempotency_key`                                                                                                 | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | A header for idempotency purposes                                                                                 |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.SubscribersV1ControllerUpdateSubscriberGlobalPreferencesResponse](../../models/subscribersv1controllerupdatesubscriberglobalpreferencesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve_by_level

Get subscriber preferences by level

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.preferences.retrieve_by_level(preference_level=novu_py.Parameter.TEMPLATE, subscriber_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `preference_level`                                                                                                        | [models.Parameter](../../models/parameter.md)                                                                             | :heavy_check_mark:                                                                                                        | the preferences level to be retrieved (template / global)                                                                 |
| `subscriber_id`                                                                                                           | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `include_inactive_channels`                                                                                               | *Optional[bool]*                                                                                                          | :heavy_minus_sign:                                                                                                        | A flag which specifies if the inactive workflow channels should be included in the retrieved preferences. Default is true |
| `idempotency_key`                                                                                                         | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | A header for idempotency purposes                                                                                         |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.SubscribersV1ControllerGetSubscriberPreferenceByLevelResponse](../../models/subscribersv1controllergetsubscriberpreferencebylevelresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update_legacy

Update subscriber preference

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.preferences.update_legacy(subscriber_id="<id>", workflow_id="<id>", update_subscriber_preference_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                     | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `workflow_id`                                                                                       | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `update_subscriber_preference_request_dto`                                                          | [models.UpdateSubscriberPreferenceRequestDto](../../models/updatesubscriberpreferencerequestdto.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `idempotency_key`                                                                                   | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | A header for idempotency purposes                                                                   |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.SubscribersV1ControllerUpdateSubscriberPreferenceResponse](../../models/subscribersv1controllerupdatesubscriberpreferenceresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Get subscriber global and workflow specific preferences

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.preferences.retrieve(subscriber_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

Update subscriber global or workflow specific preferences

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.preferences.update(subscriber_id="<id>", patch_subscriber_preferences_dto={
        "channels": {},
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