# TranslationControllerUploadTranslationFilesRequest


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A header for idempotency purposes                                                |
| `upload_translations_request_dto`                                                | [models.UploadTranslationsRequestDto](../models/uploadtranslationsrequestdto.md) | :heavy_check_mark:                                                               | Translation files upload body details                                            |