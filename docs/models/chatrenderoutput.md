# ChatRenderOutput


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `body`                                                                          | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Body of the chat message. Mutually exclusive with `card`.                       |
| `card`                                                                          | Dict[str, *Any*]                                                                | :heavy_minus_sign:                                                              | Rich Chat: compiled provider-agnostic card DSL. Mutually exclusive with `body`. |