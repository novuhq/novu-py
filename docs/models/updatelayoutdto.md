# UpdateLayoutDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Name of the layout                                                   |
| `is_translation_enabled`                                             | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Enable or disable translations for this layout                       |
| `control_values`                                                     | [models.LayoutControlValuesDto](../models/layoutcontrolvaluesdto.md) | :heavy_check_mark:                                                   | Control values for the layout                                        |