"""
Script to sanitize filenames if they're not web safe (has to be called from gh actions because 
Windows doesn't notice when a filename is decapitalized -.-)
"""

import os
from pathlib import Path

src = Path(__file__).parent.parent / "source"

# detect capitals
for file in src.glob("**/*"):
    safename = file.stem
    # lowercase
    safename = safename.lower()
    # remove space
    safename = safename.replace(" ", "_")
    # reconstruct
    safe = file.parent / f"{safename}{file.suffix}"
    # construct intermediate
    inter = safe.parent / f"_{safe.stem}{safe.suffix}"
    # is it capital?
    if safe.stem != file.stem:
        # rename to intermediate
        print("RENAMING", file.stem, "TO", inter.stem)
        os.rename(file, inter)
        # rename to safe
        print("RENAMING", inter.stem, "TO", safe.stem)
        os.rename(inter, safe)
