# SubscribersControllerUnsnoozeNotificationRequest


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `subscriber_id`                    | *str*                              | :heavy_check_mark:                 | The identifier of the subscriber   |
| `notification_id`                  | *str*                              | :heavy_check_mark:                 | The identifier of the notification |
| `context_keys`                     | List[*str*]                        | :heavy_minus_sign:                 | Context keys for filtering         |
| `idempotency_key`                  | *Optional[str]*                    | :heavy_minus_sign:                 | A header for idempotency purposes  |