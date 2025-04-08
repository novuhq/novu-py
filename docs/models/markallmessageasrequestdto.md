# MarkAllMessageAsRequestDto


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `feed_identifier`                                              | [Optional[models.FeedIdentifier]](../models/feedidentifier.md) | :heavy_minus_sign:                                             | Optional feed identifier or array of feed identifiers          |
| `mark_as`                                                      | [models.MarkAs](../models/markas.md)                           | :heavy_check_mark:                                             | Mark all subscriber messages as read, unread, seen or unseen   |