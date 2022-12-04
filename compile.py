from pathlib import Path
import markdown as md
from copy import deepcopy
import shutil
import os
import logging
import re

encoding = 'utf-8'
logging.getLogger().setLevel(logging.INFO)


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
build = root / "docs"
source = root / "source"
# Read in template
with open(str(root / "template.html"), "r", encoding=encoding) as f:
    template = f.read()
logging.info(f"Read {root / 'template.html'}.")


def buildPage(file):
    """
    Build an html page in the build folder from a md file in the source folder.
    """
    def preprocess(content):
        """
        Transformations to apply to markdown content before compiling to HTML
        """
        # Mark asset paths as needing normalization
        content = content.replace("_assets/", "{{assets}}/")
        # Replace refs to markdown files with refs to equivalent html files
        content = content.replace(".md)", ".html)")
        # Add splash to images
        def _splash(match):
            alt = match.group(1) or ""
            src = match.group(2) or ""
            return f"<figure class=splashimg><img src={src} alt={alt} /></figure>"
        content = re.sub(r"\!\[(.*)\]\((.*)\)", _splash, content)
        
        return content

    def postprocess(content):
        """
        Transformations to apply to HTML content after compiling from markdown
        """

        return content


    # Copy template
    page = deepcopy(template)
    # Transpile html content
    with open(str(file), "r", encoding=encoding) as f:
        content_md = f.read()
    # Transpile html content
    content_md = preprocess(content_md)
    content_html = md.markdown(content_md)
    content_html = postprocess(content_html)
    # Insert content into page
    page = page.replace("{{content}}", content_html)
    
    # Normalize paths
    for key in ("style", "utils", "assets"):
        norm = source.normalize(file) / key
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


# Clear build folder
if build.is_dir():
    shutil.rmtree(build)
    logging.info(f"Deleted folder {build}")
os.mkdir(str(build))
logging.info(f"Created folder {build}")
# Copy style, assets and scripts over
for key in ("assets", "style", "utils"):
    # Copy source folder if there is one
    if (source / ("_" + key)).is_dir():
        shutil.copytree(
            source / ("_" + key),
            build / key
        )
        logging.info(f"Copied {source / key} to {build / key}.")
# Build every md file in source tree
for file in source.glob("**/*.md"):
    buildPage(file)
