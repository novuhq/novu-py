# Subscribers.Tokens

## Overview

### Available Operations

* [create](#create) - Create a subscriber login token

## create

Create a short-lived, Novu-signed login token for the subscriber identified by **subscriberId**.

    Call it from your backend with your secret key, then pass the token to the browser, which exchanges it for an Inbox session.
    Creating a token does not read or change the subscriber, so the subscriber does not need to exist yet.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_createSubscriberToken" method="post" path="/v2/subscribers/{subscriberId}/tokens" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.tokens.create(subscriber_id="<id>", create_subscriber_token_request_dto={
        "context": {
            "key": "org-acme",
        },
        "subscriber": {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "avatar": "https://example.com/avatar.jpg",
            "locale": "en-US",
            "timezone": "America/New_York",
        },
        "scope": [
            novu_py.SubscriberTokenScopeEnum.CHANNELS_SHARED,
        ],
        "expires_in": 600,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | The identifier of the subscriber                                                          |
| `create_subscriber_token_request_dto`                                                     | [models.CreateSubscriberTokenRequestDto](../../models/createsubscribertokenrequestdto.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `idempotency_key`                                                                         | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | A header for idempotency purposes                                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.SubscribersControllerCreateSubscriberTokenResponse](../../models/subscriberscontrollercreatesubscribertokenresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |