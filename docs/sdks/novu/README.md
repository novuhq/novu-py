# Novu SDK

## Overview

Novu API: Novu REST API. Please see https://docs.novu.co/api-reference for more details.

Novu Documentation
<https://docs.novu.co>

### Available Operations

* [support_controller_fetch_user_organizations](#support_controller_fetch_user_organizations)
* [create](#create)

## support_controller_fetch_user_organizations

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

with Novu(
    security=novu_py.Security(
        secret_key=os.getenv("NOVU_SECRET_KEY", ""),
    ),
) as novu:

    novu.support_controller_fetch_user_organizations(plain_card_request_dto={
        "timestamp": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `plain_card_request_dto`                                            | [models.PlainCardRequestDto](../../models/plaincardrequestdto.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

with Novu(
    security=novu_py.Security(
        secret_key=os.getenv("NOVU_SECRET_KEY", ""),
    ),
) as novu:

    novu.create(create_support_thread_dto={
        "text": "<value>",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `create_support_thread_dto`                                             | [models.CreateSupportThreadDto](../../models/createsupportthreaddto.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `idempotency_key`                                                       | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | A header for idempotency purposes                                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |