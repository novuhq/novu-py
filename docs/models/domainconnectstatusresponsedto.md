# DomainConnectStatusResponseDto


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `available`                                                            | *bool*                                                                 | :heavy_check_mark:                                                     | N/A                                                                    |
| `provider_name`                                                        | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `provider_id`                                                          | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `reason`                                                               | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `reason_code`                                                          | [Optional[models.ReasonCode]](../models/reasoncode.md)                 | :heavy_minus_sign:                                                     | N/A                                                                    |
| `manual_records`                                                       | List[[models.ExpectedDNSRecordDto](../models/expecteddnsrecorddto.md)] | :heavy_check_mark:                                                     | N/A                                                                    |