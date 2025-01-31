# GetSubscriberPreferencesResponseDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `preference`                                                       | [models.Preference](../models/preference.md)                       | :heavy_check_mark:                                                 | The preferences of the subscriber regarding the related workflow   |
| `template`                                                         | [Optional[models.TemplateResponse]](../models/templateresponse.md) | :heavy_minus_sign:                                                 | The workflow information and if it is critical or not              |