# ConstraintValidation


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `messages`                                           | List[*str*]                                          | :heavy_check_mark:                                   | List of validation error messages                    | [<br/>"Field is required",<br/>"Invalid format"<br/>] |
| `value`                                              | [OptionalNullable[models.Value]](../models/value.md) | :heavy_minus_sign:                                   | Value that failed validation                         | xx xx xx                                             |