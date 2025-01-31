# SubscribersControllerUpdateSubscriberPreferencesRequest


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `subscriber_id`                                                                    | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `patch_subscriber_preferences_dto`                                                 | [models.PatchSubscriberPreferencesDto](../models/patchsubscriberpreferencesdto.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `idempotency_key`                                                                  | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | A header for idempotency purposes                                                  |