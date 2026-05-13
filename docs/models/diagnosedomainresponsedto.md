# DiagnoseDomainResponseDto


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `ok`                                                                           | *bool*                                                                         | :heavy_check_mark:                                                             | True when there are no error-severity issues                                   |
| `run_at`                                                                       | *str*                                                                          | :heavy_check_mark:                                                             | ISO timestamp when the diagnostic run finished                                 |
| `checks`                                                                       | List[[models.DomainDiagnosticCheckDto](../models/domaindiagnosticcheckdto.md)] | :heavy_check_mark:                                                             | N/A                                                                            |
| `issues`                                                                       | List[[models.DomainDiagnosticIssueDto](../models/domaindiagnosticissuedto.md)] | :heavy_check_mark:                                                             | N/A                                                                            |