# GetSubscriberPreferencesDto


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `global_`                                                                                    | [models.SubscriberGlobalPreferenceDto](../models/subscriberglobalpreferencedto.md)           | :heavy_check_mark:                                                                           | Global preference settings                                                                   |
| `workflows`                                                                                  | List[[models.SubscriberWorkflowPreferenceDto](../models/subscriberworkflowpreferencedto.md)] | :heavy_check_mark:                                                                           | Workflow-specific preference settings                                                        |