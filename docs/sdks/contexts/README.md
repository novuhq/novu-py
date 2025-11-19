# Contexts
(*contexts*)

## Overview

### Available Operations

* [create](#create) - Create a context
* [list](#list) - List all contexts
* [update](#update) - Update a context
* [retrieve](#retrieve) - Retrieve a context
* [delete](#delete) - Delete a context

## create

Create a new context with the specified type, id, and data. Returns 409 if context already exists.

      **type** and **id** are required fields, **data** is optional, if the context already exists, it returns the 409 response

### Example Usage

<!-- UsageSnippet language="python" operationID="ContextsController_createContext" method="post" path="/v2/contexts" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.contexts.create(create_context_request_dto={
        "type": "tenant",
        "id": "org-acme",
        "data": {},
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `create_context_request_dto`                                              | [models.CreateContextRequestDto](../../models/createcontextrequestdto.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `idempotency_key`                                                         | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A header for idempotency purposes                                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ContextsControllerCreateContextResponse](../../models/contextscontrollercreatecontextresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## list

Retrieve a paginated list of all contexts, optionally filtered by type and key pattern.

      **type** and **id** are optional fields, if provided, only contexts with the matching type and id will be returned.
      **search** is an optional field, if provided, only contexts with the matching key pattern will be returned.
      Checkout all possible parameters in the query section below for more details

### Example Usage

<!-- UsageSnippet language="python" operationID="ContextsController_listContexts" method="get" path="/v2/contexts" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.contexts.list(request={
        "id": "tenant-prod-123",
        "search": "tenant",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.ContextsControllerListContextsRequest](../../models/contextscontrollerlistcontextsrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ContextsControllerListContextsResponse](../../models/contextscontrollerlistcontextsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update the data of an existing context.
      **type** and **id** are required fields, **data** is required. Only the data field is updated, the rest of the context is not affected.
      If the context does not exist, it returns the 404 response

### Example Usage

<!-- UsageSnippet language="python" operationID="ContextsController_updateContext" method="patch" path="/v2/contexts/{type}/{id}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.contexts.update(id="<id>", type_="<value>", update_context_request_dto={
        "data": {},
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | Context ID                                                                |
| `type`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | Context type                                                              |
| `update_context_request_dto`                                              | [models.UpdateContextRequestDto](../../models/updatecontextrequestdto.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `idempotency_key`                                                         | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A header for idempotency purposes                                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ContextsControllerUpdateContextResponse](../../models/contextscontrollerupdatecontextresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Retrieve a specific context by its type and id.
      **type** and **id** are required fields, if the context does not exist, it returns the 404 response

### Example Usage

<!-- UsageSnippet language="python" operationID="ContextsController_getContext" method="get" path="/v2/contexts/{type}/{id}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.contexts.retrieve(id="<id>", type_="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Context ID                                                          |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Context type                                                        |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ContextsControllerGetContextResponse](../../models/contextscontrollergetcontextresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete a context by its type and id.
      **type** and **id** are required fields, if the context does not exist, it returns the 404 response

### Example Usage

<!-- UsageSnippet language="python" operationID="ContextsController_deleteContext" method="delete" path="/v2/contexts/{type}/{id}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.contexts.delete(id="<id>", type_="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Context ID                                                          |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Context type                                                        |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ContextsControllerDeleteContextResponse](../../models/contextscontrollerdeletecontextresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |