# EnvironmentVariables

## Overview

### Available Operations

* [list](#list) - List all variables
* [create](#create) - Create a variable
* [retrieve](#retrieve) - Get environment variable
* [update](#update) - Update a variable
* [delete](#delete) - Delete environment variable
* [usage](#usage) - Retrieve a variable usage

## list

Returns all environment variables for the current organization. Secret values are masked.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentVariablesController_listEnvironmentVariables" method="get" path="/v1/environment-variables" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environment_variables.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter variables by key (case-insensitive partial match)            |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvironmentVariablesControllerListEnvironmentVariablesResponse](../../models/environmentvariablescontrollerlistenvironmentvariablesresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Creates a new environment variable. Keys must be uppercase with underscores only (e.g. BASE_URL). Secret variables are encrypted at rest and masked in API responses.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentVariablesController_createEnvironmentVariable" method="post" path="/v1/environment-variables" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environment_variables.create(create_environment_variable_request_dto={
        "key": "<key>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `create_environment_variable_request_dto`                                                         | [models.CreateEnvironmentVariableRequestDto](../../models/createenvironmentvariablerequestdto.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `idempotency_key`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A header for idempotency purposes                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.EnvironmentVariablesControllerCreateEnvironmentVariableResponse](../../models/environmentvariablescontrollercreateenvironmentvariableresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 404, 405, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## retrieve

Returns a single environment variable by key. Secret values are masked.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentVariablesController_getEnvironmentVariable" method="get" path="/v1/environment-variables/{variableKey}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environment_variables.retrieve(variable_key="BASE_URL")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `variable_key`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique key of the environment variable (e.g. BASE_URL)          | BASE_URL                                                            |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EnvironmentVariablesControllerGetEnvironmentVariableResponse](../../models/environmentvariablescontrollergetenvironmentvariableresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## update

Updates an existing environment variable. Providing values replaces all existing per-environment values.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentVariablesController_updateEnvironmentVariable" method="patch" path="/v1/environment-variables/{variableKey}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environment_variables.update(variable_key="BASE_URL", update_environment_variable_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `variable_key`                                                                                    | *str*                                                                                             | :heavy_check_mark:                                                                                | The unique key of the environment variable (e.g. BASE_URL)                                        | BASE_URL                                                                                          |
| `update_environment_variable_request_dto`                                                         | [models.UpdateEnvironmentVariableRequestDto](../../models/updateenvironmentvariablerequestdto.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |                                                                                                   |
| `idempotency_key`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A header for idempotency purposes                                                                 |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.EnvironmentVariablesControllerUpdateEnvironmentVariableResponse](../../models/environmentvariablescontrollerupdateenvironmentvariableresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## delete

Deletes an environment variable by key.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentVariablesController_deleteEnvironmentVariable" method="delete" path="/v1/environment-variables/{variableKey}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environment_variables.delete(variable_key="BASE_URL")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `variable_key`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique key of the environment variable (e.g. BASE_URL)          | BASE_URL                                                            |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EnvironmentVariablesControllerDeleteEnvironmentVariableResponse](../../models/environmentvariablescontrollerdeleteenvironmentvariableresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## usage

Returns the workflows that reference this environment variable via `{{env.KEY}}` in their step controls. **variableId** is required.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentVariablesController_getEnvironmentVariableUsage" method="get" path="/v1/environment-variables/{variableKey}/usage" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environment_variables.usage(variable_key="BASE_URL")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `variable_key`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique key of the environment variable (e.g. BASE_URL)          | BASE_URL                                                            |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EnvironmentVariablesControllerGetEnvironmentVariableUsageResponse](../../models/environmentvariablescontrollergetenvironmentvariableusageresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |