# GetSubscriberPreferencesDto


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `global_`                                                                | [models.GlobalPreferenceDto](../models/globalpreferencedto.md)           | :heavy_check_mark:                                                       | Global preference settings                                               |
| `workflows`                                                              | List[[models.WorkflowPreferenceDto](../models/workflowpreferencedto.md)] | :heavy_check_mark:                                                       | Workflow-specific preference settings                                    |