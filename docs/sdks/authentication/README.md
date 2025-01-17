# Authentication
(*subscribers.authentication*)

## Overview

### Available Operations

* [chat_access_oauth_call_back](#chat_access_oauth_call_back) - Handle providers oauth redirect
* [chat_access_oauth](#chat_access_oauth) - Handle chat oauth

## chat_access_oauth_call_back

Handle providers oauth redirect

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.authentication.chat_access_oauth_call_back(request={
    "subscriber_id": "<id>",
    "provider_id": "<id>",
    "hmac_hash": "<value>",
    "environment_id": "<id>",
    "code": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.SubscribersControllerChatOauthCallbackRequest](../../models/subscriberscontrollerchatoauthcallbackrequest.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.SubscribersControllerChatOauthCallbackResponse](../../models/subscriberscontrollerchatoauthcallbackresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## chat_access_oauth

Handle chat oauth

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.authentication.chat_access_oauth(request={
    "subscriber_id": "<id>",
    "provider_id": "<id>",
    "hmac_hash": "<value>",
    "environment_id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [models.SubscribersControllerChatAccessOauthRequest](../../models/subscriberscontrollerchataccessoauthrequest.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.SubscribersControllerChatAccessOauthResponse](../../models/subscriberscontrollerchataccessoauthresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |