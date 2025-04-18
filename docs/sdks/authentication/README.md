# Authentication
(*subscribers.authentication*)

## Overview

### Available Operations

* [chat_access_oauth](#chat_access_oauth) - Handle chat oauth
* [chat_access_oauth_call_back](#chat_access_oauth_call_back) - Handle providers oauth redirect

## chat_access_oauth

Handle chat oauth

### Example Usage

```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.authentication.chat_access_oauth(request={
        "subscriber_id": "<id>",
        "provider_id": "<id>",
        "hmac_hash": "<value>",
        "environment_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.SubscribersV1ControllerChatAccessOauthRequest](../../models/subscribersv1controllerchataccessoauthrequest.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.SubscribersV1ControllerChatAccessOauthResponse](../../models/subscribersv1controllerchataccessoauthresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## chat_access_oauth_call_back

Handle providers oauth redirect

### Example Usage

```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.authentication.chat_access_oauth_call_back(request={
        "subscriber_id": "<id>",
        "provider_id": "<id>",
        "hmac_hash": "<value>",
        "environment_id": "<id>",
        "code": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                 | [models.SubscribersV1ControllerChatOauthCallbackRequest](../../models/subscribersv1controllerchatoauthcallbackrequest.md) | :heavy_check_mark:                                                                                                        | The request object to use for the request.                                                                                |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.SubscribersV1ControllerChatOauthCallbackResponse](../../models/subscribersv1controllerchatoauthcallbackresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |