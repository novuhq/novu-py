# Translations.Master

## Overview

### Available Operations

* [retrieve](#retrieve) - Retrieve master translations JSON
* [import_master_json](#import_master_json) - Import master translations JSON
* [upload](#upload) - Upload master translations JSON file

## retrieve

Retrieve all translations for a locale in master JSON format organized by resourceId (workflowId)

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_getMasterJsonEndpoint" method="get" path="/v2/translations/master-json" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.translations.master.retrieve(locale="en_US")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `locale`                                                               | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Locale to export. If not provided, exports organization default locale | en_US                                                                  |
| `idempotency_key`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | A header for idempotency purposes                                      |                                                                        |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[models.GetMasterJSONResponseDto](../../models/getmasterjsonresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## import_master_json

Import translations for multiple workflows from master JSON format for a specific locale

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_importMasterJsonEndpoint" method="post" path="/v2/translations/master-json" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.translations.master.import_master_json(import_master_json_request_dto={
        "locale": "en_US",
        "master_json": {
            "workflows": {
                "welcome-email": {
                    "welcome.title": "Welcome to our platform",
                    "welcome.message": "Hello there!",
                },
                "password-reset": {
                    "reset.title": "Reset your password",
                    "reset.message": "Click the link to reset",
                },
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `import_master_json_request_dto`                                                | [models.ImportMasterJSONRequestDto](../../models/importmasterjsonrequestdto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `idempotency_key`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | A header for idempotency purposes                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ImportMasterJSONResponseDto](../../models/importmasterjsonresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## upload

Upload a master JSON file containing translations for multiple workflows. Locale is automatically detected from filename (e.g., en_US.json)

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_uploadMasterJsonEndpoint" method="post" path="/v2/translations/master-json/upload" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.translations.master.upload(request_body={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                              | [models.TranslationControllerUploadMasterJSONEndpointRequestBody](../../models/translationcontrolleruploadmasterjsonendpointrequestbody.md) | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `idempotency_key`                                                                                                                           | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | A header for idempotency purposes                                                                                                           |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.ImportMasterJSONResponseDto](../../models/importmasterjsonresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |