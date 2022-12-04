from pathlib import Path
import markdown as md
from copy import deepcopy
import shutil
import os
import logging

encoding = 'utf-8'


def normalize(self, target):
    """
    Inverse of relative_to, honestly no idea why this isn't already in pathlib.Path
    """
    rel = target.relative_to(self)
    norm = Path()
    for p in rel.parents:
        if p != Path():
            norm /= ".."
    return norm
Path.normalize = normalize


# Define some useful paths
root = Path(__file__).parent
build = root / "build"
source = root / "source"
# Read in template
with open(str(root / "template.html"), "r", encoding=encoding) as f:
    template = f.read()
logging.info(f"Read {root / 'template.html'}.")


def buildPage(file):
    # Copy template
    page = deepcopy(template)
    # Transpile html content
    with open(str(file), "r", encoding=encoding) as f:
        content_md = f.read()
    content_html = md.markdown(content_md)
    page = page.replace("{{content}}", content_html)
    # Mark asset paths as needing normalization
    page = page.replace("src=\"_assets/", "src=\"{{assets}}/")
    # Normalize paths
    for key in ("style", "utils", "assets"):
        norm = source.normalize(file) / ("_" + key)
        page = page.replace("{{%s}}" % key, str(norm).replace("\\", "/"))
    # Where to write html file to?
    outpath = build / file.relative_to(source).parent / (file.stem + ".html")
    # Make sure directory exists
    if not outpath.parent.is_dir():
        os.makedirs(str(outpath.parent))
        logging.info(f"Created directory {outpath.parent}.")
    # Write html file
    with open(str(outpath), "w", encoding=encoding) as f:
        f.write(page)
    # Log
    logging.info(f"Written {outpath} from {file}.")


# Copy style, assets and scripts over
for key in ("_assets", "_style", "_utils"):
    # Delete old build folder
    if (build / key).is_dir():
        shutil.rmtree(build / key)
        logging.info(f"Deleted folder {build / key}")
    # Copy source folder if there is one
    if (source / key).is_dir():
        shutil.copytree(
            source / key,
            build / key
        )
        logging.info(f"Copied {source / key} to {build / key}.")
# Build every md file in source tree
for file in source.glob("**/*.md"):
    buildPage(file)
