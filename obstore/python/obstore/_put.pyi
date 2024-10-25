from pathlib import Path
from typing import IO, TypedDict

from .store import ObjectStore

class PutResult(TypedDict):
    """
    Result for a put request.
    """

    e_tag: str | None
    """
    The unique identifier for the newly created object

    <https://datatracker.ietf.org/doc/html/rfc9110#name-etag>
    """

    version: str | None
    """A version indicator for the newly created object."""

def put(
    store: ObjectStore,
    path: str,
    file: IO[bytes] | Path | bytes,
) -> PutResult:
    """Save the provided bytes to the specified location

    The operation is guaranteed to be atomic, it will either successfully write the
    entirety of `file` to `location`, or fail. No clients should be able to observe a
    partially written object.

    Args:
        store: The ObjectStore instance to use.
        path: The path within ObjectStore for where to save the file.
        file: The object to upload. Can either be file-like, a `Path` to a local file,
            or a `bytes` object.
    """

async def put_async(
    store: ObjectStore,
    path: str,
    file: IO[bytes] | Path | bytes,
) -> PutResult:
    """Call `put` asynchronously.

    Refer to the documentation for [put][obstore.put].
    """

def put_multipart(
    store: ObjectStore,
    path: str,
    file: IO[bytes] | Path | bytes,
    *,
    chunk_size: int = 5 * 1024 * 1024,
    max_concurrency: int = 12,
) -> PutResult:
    """Save the provided bytes to the specified location

    The operation is guaranteed to be atomic, it will either successfully write the
    entirety of `file` to `location`, or fail. No clients should be able to observe a
    partially written object.

    Args:
        store: The ObjectStore instance to use.
        path: The path within ObjectStore for where to save the file.
        file: The object to upload. Can either be file-like, a `Path` to a local file,
            or a `bytes` object.

    Keyword args:
        chunk_size: The size of chunks to use within each part of the multipart upload. Defaults to 5 MB.
        max_concurrency: The maximum number of chunks to upload concurrently. Defaults to 12.
    """

async def put_multipart_async(
    store: ObjectStore,
    path: str,
    file: IO[bytes] | Path | bytes,
    *,
    use_multipart: bool | None = None,
    chunk_size: int = 5 * 1024 * 1024,
    max_concurrency: int = 12,
) -> PutResult:
    """Call `put_multipart` asynchronously.

    Refer to the documentation for [put_multipart][obstore.put_multipart].
    """
