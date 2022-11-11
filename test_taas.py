#!/usr/bin/env python3

from taas import reverse_lines
import os
import tempfile
import time


def _run_reverse_lines_on(input_bytes):
    with tempfile.TemporaryDirectory() as directory:
        os.chdir(directory)
        filename = "test"
        with open(filename, "wb") as f:
            f.write(input_bytes)
        return list(reverse_lines(filename))


def test_reverse_lines():
    assert _run_reverse_lines_on(b"1\n2\n3\n") == [b"3\n", b"2\n", b"1\n"]
    assert _run_reverse_lines_on(b"123") == [b"123"]
    assert _run_reverse_lines_on(b"1\n") == [b"1\n"]
    assert _run_reverse_lines_on(b"1\n2") == [b"2", b"1\n"]
    assert _run_reverse_lines_on(b"") == []
