# AgentSkillInputDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | [models.AgentSkillInputDtoType](../models/agentskillinputdtotype.md) | :heavy_check_mark:                                                   | N/A                                                                  |
| `skill_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Skill identifier, e.g. "xlsx" or "skill_01XJ5..."                    |
| `version`                                                            | [OptionalNullable[models.Version]](../models/version.md)             | :heavy_minus_sign:                                                   | Version to pin. Omit for latest.                                     |