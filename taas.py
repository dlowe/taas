#!/usr/bin/env python3

import mmap
import os

def reverse_lines(filename):
    ## mmaping a zero-byte file is an error, so we need to explicitly handle it
    if os.path.getsize(filename) == 0:
        return

    with open(filename, "rb") as f:
        with mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) as contents:
            eol = len(contents)

            ## if the last byte of the file is a newline, back over it to avoid yielding an empty line
            if contents[eol-1] == ord(b"\n"):
                eol = eol - 1

            ## yield one line at a time
            while True:
                sol = contents.rfind(b"\n", 0, eol)
                yield contents[sol+1:eol+1]
                if sol == -1:
                    break
                eol = sol
