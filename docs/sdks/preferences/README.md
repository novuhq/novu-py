# Preferences
(*subscribers.preferences*)

## Overview

### Available Operations

* [list](#list) - Get subscriber preferences
* [update_global](#update_global) - Update subscriber global preferences
* [retrieve_by_level](#retrieve_by_level) - Get subscriber preferences by level
* [update](#update) - Update subscriber preference

## list

Get subscriber preferences

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
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

**[models.SubscribersControllerListSubscriberPreferencesResponse](../../models/subscriberscontrollerlistsubscriberpreferencesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ErrorDto                        | 414                                    | application/json                       |
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
    api_key=os.getenv("NOVU_API_KEY", ""),
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

**[models.SubscribersControllerUpdateSubscriberGlobalPreferencesResponse](../../models/subscriberscontrollerupdatesubscriberglobalpreferencesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ErrorDto                        | 414                                    | application/json                       |
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
    api_key=os.getenv("NOVU_API_KEY", ""),
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

**[models.SubscribersControllerGetSubscriberPreferenceByLevelResponse](../../models/subscriberscontrollergetsubscriberpreferencebylevelresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update subscriber preference

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
) as novu:

    res = novu.subscribers.preferences.update(subscriber_id="<id>", workflow_id="<id>", update_subscriber_preference_request_dto={})

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

**[models.SubscribersControllerUpdateSubscriberPreferenceResponse](../../models/subscriberscontrollerupdatesubscriberpreferenceresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |