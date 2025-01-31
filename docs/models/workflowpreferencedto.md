# WorkflowPreferenceDto


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `enabled`                                                    | *bool*                                                       | :heavy_check_mark:                                           | Whether notifications are enabled for this workflow          |
| `channels`                                                   | [models.PreferenceChannels](../models/preferencechannels.md) | :heavy_check_mark:                                           | Channel-specific preference settings for this workflow       |
| `overrides`                                                  | List[[models.Overrides](../models/overrides.md)]             | :heavy_check_mark:                                           | List of preference overrides                                 |
| `workflow`                                                   | [models.WorkflowInfoDto](../models/workflowinfodto.md)       | :heavy_check_mark:                                           | Workflow information                                         |