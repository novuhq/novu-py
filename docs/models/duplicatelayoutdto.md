# DuplicateLayoutDto


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `name`                                                                           | *str*                                                                            | :heavy_check_mark:                                                               | Name of the layout                                                               |
| `layout_id`                                                                      | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | Identifier for the duplicated layout. When omitted, it is derived from the name. |
| `is_translation_enabled`                                                         | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Enable or disable translations for this layout                                   |