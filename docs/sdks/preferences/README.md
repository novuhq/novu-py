# Preferences
(*subscribers.preferences*)

## Overview

### Available Operations

* [list](#list) - Get subscriber preferences
* [update](#update) - Update subscriber global or workflow specific preferences

## list

Get subscriber global and workflow specific preferences

### Example Usage

```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.preferences.list(subscriber_id="<id>")

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


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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