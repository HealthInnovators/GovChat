# `File`

The `File` model is the fundamental model for storing file references in the GovChat system. It maintains a lightweight reference to files location in S3.


::: GovChat.models.file.File

# `FileStatus`

The `File` model also has a companion `FileStatus` model that helps track the status of the file processing. This nests `ChunkStatus` models to see if chunks have been created and if they have been completely embedded yet.

::: GovChat.models.file.FileStatus