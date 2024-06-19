import re
from mkdocs.structure import pages, files
from mkdocs import config
from functools import partial


site_url = "."


def substitute_root_link(match) -> str:
    """
    Make a root link (beginning with a slash) relative to the *site* root rather than the **server* root.

    Parameters
    ----------
    match : re.Match
        Regex match for the link
    """
    # get all groups
    label, link = match.groups()
    # remove .md file extension
    for ext in (".md", ".md/"):
        if link.endswith(ext):
            link = link[:-len(ext)]
    # construct full link
    full_link = f"[{label}]({site_url}{link})"

    return full_link


def on_pre_build(config: config.defaults.MkDocsConfig) -> None:
    """
    Find the homepage of the current site and store it in a global variable.

    Parameters
    ----------
    config : config.MkDocsConfig
        Config for the current site
    """
    global site_url
    # set site url from config
    site_url = config.site_url or ""
    # replace any \ (Windows only) with / (accepted by Windows and Unix)
    site_url = site_url.replace("\\", "/")
    # make sure we finish with a /
    if not site_url.endswith("/"):
        site_url += "/"


def on_page_markdown(markdown: str, page: pages.Page, config: config.Config, files: files.File) -> str:
    """
    Make links beginning with a slash relative to the *site* root rather than the *server* root.

    Parameters
    ----------
    markdown : str
        Markdown text
    page : pages.Page
        MkDocs page object
    config : config.Config
        MkDocs configutation object
    files : files.File
        MkDocs file object

    Returns
    -------
    str
        Parsed markdown text
    """
    # regex to find root links
    re_link = r"\[([^\]]*)\]\(\/([^\)]*)\)"
    # do substitution
    return re.sub(
        pattern=re_link,
        string=markdown, 
        repl=substitute_root_link
    )