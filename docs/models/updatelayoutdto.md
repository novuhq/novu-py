# UpdateLayoutDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Name of the layout                                                   |
| `is_translation_enabled`                                             | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Enable or disable translations for this layout                       |
| `control_values`                                                     | [OptionalNullable[models.ControlValues]](../models/controlvalues.md) | :heavy_minus_sign:                                                   | Control values for the layout                                        |