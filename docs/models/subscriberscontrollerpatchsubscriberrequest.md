# SubscribersControllerPatchSubscriberRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `subscriber_id`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `idempotency_key`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | A header for idempotency purposes                                          |
| `patch_subscriber_request_dto`                                             | [models.PatchSubscriberRequestDto](../models/patchsubscriberrequestdto.md) | :heavy_check_mark:                                                         | N/A                                                                        |