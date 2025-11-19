# Saturday

Saturday schedule


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `is_enabled`                                           | *bool*                                                 | :heavy_check_mark:                                     | Day schedule enabled                                   | true                                                   |
| `hours`                                                | List[[models.TimeRangeDto](../models/timerangedto.md)] | :heavy_minus_sign:                                     | Hours                                                  | [<br/>{<br/>"start": "09:00 AM",<br/>"end": "05:00 PM"<br/>}<br/>] |