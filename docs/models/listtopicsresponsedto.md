# ListTopicsResponseDto


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `data`                                                                          | List[[models.TopicResponseDto](../models/topicresponsedto.md)]                  | :heavy_check_mark:                                                              | List of returned Topics                                                         |
| `next`                                                                          | *Nullable[str]*                                                                 | :heavy_check_mark:                                                              | The cursor for the next page of results, or null if there are no more pages.    |
| `previous`                                                                      | *Nullable[str]*                                                                 | :heavy_check_mark:                                                              | The cursor for the previous page of results, or null if this is the first page. |