# UploadTranslationsResponseDto


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `total_files`                             | *float*                                   | :heavy_check_mark:                        | Total number of files processed           | 3                                         |
| `successful_uploads`                      | *float*                                   | :heavy_check_mark:                        | Number of files successfully uploaded     | 2                                         |
| `failed_uploads`                          | *float*                                   | :heavy_check_mark:                        | Number of files that failed to upload     | 1                                         |
| `errors`                                  | List[*str*]                               | :heavy_check_mark:                        | List of error messages for failed uploads | [<br/>"Invalid JSON in file: es-ES.json"<br/>] |