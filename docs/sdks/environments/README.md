# Environments

## Overview

Environments allow you to manage different stages of your application development lifecycle. Each environment has its own set of API keys and configurations, enabling you to separate development, staging, and production workflows.
<https://docs.novu.co/platform/environments>

### Available Operations

* [get_tags](#get_tags) - List environment tags
* [diff](#diff) - Compare resources between environments
* [publish](#publish) - Publish resources to target environment
* [create](#create) - Create an environment
* [list](#list) - List all environments
* [update](#update) - Update an environment
* [delete](#delete) - Delete an environment

## get_tags

Retrieve all unique tags used in workflows within the specified environment. These tags can be used for filtering workflows.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentsController_getEnvironmentTags" method="get" path="/v2/environments/{environmentId}/tags" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environments.get_tags(environment_id="6615943e7ace93b0540ae377")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Environment internal ID (MongoDB ObjectId) or identifier            | 6615943e7ace93b0540ae377                                            |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EnvironmentsControllerGetEnvironmentTagsResponse](../../models/environmentscontrollergetenvironmenttagsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## diff

Compares workflows and other resources between the source and target environments, returning detailed diff information including additions, modifications, and deletions.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentsController_diffEnvironment" method="post" path="/v2/environments/{targetEnvironmentId}/diff" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environments.diff(target_environment_id="6615943e7ace93b0540ae377", diff_environment_request_dto={
        "source_environment_id": "507f1f77bcf86cd799439011",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `target_environment_id`                                                       | *str*                                                                         | :heavy_check_mark:                                                            | Target environment ID (MongoDB ObjectId) to compare against                   | 6615943e7ace93b0540ae377                                                      |
| `diff_environment_request_dto`                                                | [models.DiffEnvironmentRequestDto](../../models/diffenvironmentrequestdto.md) | :heavy_check_mark:                                                            | Diff request configuration                                                    |                                                                               |
| `idempotency_key`                                                             | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A header for idempotency purposes                                             |                                                                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.EnvironmentsControllerDiffEnvironmentResponse](../../models/environmentscontrollerdiffenvironmentresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## publish

Publishes all workflows and resources from the source environment to the target environment. Optionally specify specific resources to publish or use dryRun mode to preview changes.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentsController_publishEnvironment" method="post" path="/v2/environments/{targetEnvironmentId}/publish" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environments.publish(target_environment_id="6615943e7ace93b0540ae377", publish_environment_request_dto={
        "source_environment_id": "507f1f77bcf86cd799439011",
        "resources": [
            {
                "resource_type": novu_py.ResourceTypeEnum.REGULAR,
                "resource_id": "workflow-id-1",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `target_environment_id`                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | Target environment ID (MongoDB ObjectId) to publish resources to                    | 6615943e7ace93b0540ae377                                                            |
| `publish_environment_request_dto`                                                   | [models.PublishEnvironmentRequestDto](../../models/publishenvironmentrequestdto.md) | :heavy_check_mark:                                                                  | Publish request configuration                                                       |                                                                                     |
| `idempotency_key`                                                                   | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | A header for idempotency purposes                                                   |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.EnvironmentsControllerPublishEnvironmentResponse](../../models/environmentscontrollerpublishenvironmentresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Creates a new environment within the current organization. 
    Environments allow you to manage different stages of your application development lifecycle.
    Each environment has its own set of API keys and configurations.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentsControllerV1_createEnvironment" method="post" path="/v1/environments" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environments.create(create_environment_request_dto={
        "name": "Production Environment",
        "parent_id": "60d5ecb8b3b3a30015f3e1a1",
        "color": "#3498db",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `create_environment_request_dto`                                                  | [models.CreateEnvironmentRequestDto](../../models/createenvironmentrequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EnvironmentsControllerV1CreateEnvironmentResponse](../../models/environmentscontrollerv1createenvironmentresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 402, 414                               | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## list

This API returns a list of environments for the current organization. 
    Each environment contains its configuration, API keys (if user has access), and metadata.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentsControllerV1_listMyEnvironments" method="get" path="/v1/environments" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environments.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvironmentsControllerV1ListMyEnvironmentsResponse](../../models/environmentscontrollerv1listmyenvironmentsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update an environment by its unique identifier **environmentId**. 
    You can modify the environment name, identifier, color, and other configuration settings.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentsControllerV1_updateMyEnvironment" method="put" path="/v1/environments/{environmentId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environments.update(environment_id="<id>", update_environment_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `environment_id`                                                                  | *str*                                                                             | :heavy_check_mark:                                                                | The unique identifier of the environment                                          |
| `update_environment_request_dto`                                                  | [models.UpdateEnvironmentRequestDto](../../models/updateenvironmentrequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EnvironmentsControllerV1UpdateMyEnvironmentResponse](../../models/environmentscontrollerv1updatemyenvironmentresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete an environment by its unique identifier **environmentId**. 
    This action is irreversible and will remove the environment and all its associated data.

### Example Usage

<!-- UsageSnippet language="python" operationID="EnvironmentsControllerV1_deleteEnvironment" method="delete" path="/v1/environments/{environmentId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.environments.delete(environment_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the environment                            |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvironmentsControllerV1DeleteEnvironmentResponse](../../models/environmentscontrollerv1deleteenvironmentresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |