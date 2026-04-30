# ExpectedDNSRecordDto


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `type`                               | *str*                                | :heavy_check_mark:                   | N/A                                  | MX                                   |
| `name`                               | *str*                                | :heavy_check_mark:                   | N/A                                  | inbound                              |
| `content`                            | *str*                                | :heavy_check_mark:                   | N/A                                  | inbound-smtp.us-east-1.amazonaws.com |
| `ttl`                                | *str*                                | :heavy_check_mark:                   | N/A                                  | Auto                                 |
| `priority`                           | *Optional[float]*                    | :heavy_minus_sign:                   | N/A                                  | 10                                   |