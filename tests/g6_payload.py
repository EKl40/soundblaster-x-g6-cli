# tests/test_payload.py

import os
import re
import pytest
from src.g6_payload import Payload  # Adjust the import to match your module


@pytest.mark.parametrize("payload", list(Payload))
def test_get_relative_file_path_is_valid(payload):
    relative_path = payload.get_relative_file_path()

    # Check it's a string
    assert isinstance(relative_path, str), f"{payload} did not return a string."

    # Check that the file ends with `.hex`
    assert relative_path.endswith('.hex'), f"{payload} path does not end with '.hex'."

    # Check that path does not contain illegal characters
    invalid_chars_pattern = r'[<>:"|?*]'
    assert not re.search(invalid_chars_pattern, relative_path), f"{payload} path has invalid characters."

    # Optional: check no path traversal
    assert not ('..' in relative_path or relative_path.startswith('/')), f"{payload} returned an unsafe path."

    # Optional: simulate joining with base directory to ensure it forms a valid path
    try:
        full_path = os.path.join("/base/dir", relative_path)
    except Exception as e:
        pytest.fail(f"{payload} raised error when joining with base path: {e}")
