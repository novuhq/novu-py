# EventBody


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `status`                              | [models.Status](../models/status.md)  | :heavy_check_mark:                    | Status of the event                   |
| `date_`                               | *str*                                 | :heavy_check_mark:                    | Date of the event                     |
| `external_id`                         | *Optional[str]*                       | :heavy_minus_sign:                    | External ID from the provider         |
| `attempts`                            | *Optional[float]*                     | :heavy_minus_sign:                    | Number of attempts                    |
| `response`                            | *Optional[str]*                       | :heavy_minus_sign:                    | Response from the provider            |
| `row`                                 | *Optional[str]*                       | :heavy_minus_sign:                    | Raw content from the provider webhook |