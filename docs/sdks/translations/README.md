# Translations

## Overview

Used to localize your notifications to different languages.
<https://docs.novu.co/platform/workflow/translations>

### Available Operations

* [create](#create) - Create a translation
* [retrieve](#retrieve) - Retrieve a translation
* [delete](#delete) - Delete a translation
* [upload](#upload) - Upload translation files

## create

Create a translation for a specific workflow and locale, if the translation already exists, it will be updated

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_createTranslationEndpoint" method="post" path="/v2/translations" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.translations.create(create_translation_request_dto={
        "resource_id": "welcome-email",
        "resource_type": novu_py.ResourceType.LAYOUT,
        "locale": "en_US",
        "content": {
            "welcome.title": "Welcome",
            "welcome.message": "Hello there!",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `create_translation_request_dto`                                                  | [models.CreateTranslationRequestDto](../../models/createtranslationrequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.TranslationResponseDto](../../models/translationresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieve a specific translation by resource type, resource ID and locale

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_getSingleTranslation" method="get" path="/v2/translations/{resourceType}/{resourceId}/{locale}" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.translations.retrieve(resource_type=novu_py.TranslationControllerGetSingleTranslationPathParamResourceType.LAYOUT, resource_id="welcome-email", locale="en_US")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `resource_type`                                                                                                                                         | [models.TranslationControllerGetSingleTranslationPathParamResourceType](../../models/translationcontrollergetsingletranslationpathparamresourcetype.md) | :heavy_check_mark:                                                                                                                                      | Resource type                                                                                                                                           |                                                                                                                                                         |
| `resource_id`                                                                                                                                           | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | Resource ID                                                                                                                                             | welcome-email                                                                                                                                           |
| `locale`                                                                                                                                                | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | Locale code                                                                                                                                             | en_US                                                                                                                                                   |
| `idempotency_key`                                                                                                                                       | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | A header for idempotency purposes                                                                                                                       |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.TranslationResponseDto](../../models/translationresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a specific translation by resource type, resource ID and locale

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_deleteTranslationEndpoint" method="delete" path="/v2/translations/{resourceType}/{resourceId}/{locale}" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    novu.translations.delete(resource_type=novu_py.TranslationControllerDeleteTranslationEndpointPathParamResourceType.LAYOUT, resource_id="<id>", locale="pl")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `resource_type`                                                                                                                                                   | [models.TranslationControllerDeleteTranslationEndpointPathParamResourceType](../../models/translationcontrollerdeletetranslationendpointpathparamresourcetype.md) | :heavy_check_mark:                                                                                                                                                | Resource type                                                                                                                                                     |
| `resource_id`                                                                                                                                                     | *str*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                | Resource ID                                                                                                                                                       |
| `locale`                                                                                                                                                          | *str*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                | Locale code                                                                                                                                                       |
| `idempotency_key`                                                                                                                                                 | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | A header for idempotency purposes                                                                                                                                 |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## upload

Upload one or more JSON translation files for a specific workflow. Files name must match the locale, e.g. en_US.json. Supports both "files" and "files[]" field names for backwards compatibility.

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_uploadTranslationFiles" method="post" path="/v2/translations/upload" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.translations.upload(request_body={
        "resource_id": "welcome-email",
        "resource_type": novu_py.TranslationControllerUploadTranslationFilesResourceType.WORKFLOW,
        "files": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                          | [models.TranslationControllerUploadTranslationFilesRequestBody](../../models/translationcontrolleruploadtranslationfilesrequestbody.md) | :heavy_check_mark:                                                                                                                      | N/A                                                                                                                                     |
| `idempotency_key`                                                                                                                       | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | A header for idempotency purposes                                                                                                       |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.UploadTranslationsResponseDto](../../models/uploadtranslationsresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |