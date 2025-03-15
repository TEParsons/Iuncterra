import re
from mkdocs.structure import pages, files
from mkdocs import config
from functools import partial


site_url = "/"
source_dir = "/"


def substitute_root_link(to_root: str, match: re.Match, output: str="md") -> str:
    """
    Make a root link (beginning with a slash) relative to the *site* root rather than the **server* root.

    Parameters
    ----------
    to_root : str
        Root path to make link relative to
    match : re.Match
        Regex match for the link
    output : str
        Either "md" for a markdown link or "html" for an html link, default is "md"
    """
    # get all groups
    label = match.group("label")
    link = match.group("link")
    # remove start if link includes root folder
    for pre in ("source/", ):
        if link.startswith(pre):
            link = link[len(pre):]
    # construct full link
    if output == "md":
        full_link = f"[{label}]({to_root}/{link})"
    elif output == "html":
        full_link = f"<a href={to_root}/{link}>{label}</a>"
    else:
        raise ValueError("Unrecognised output type '{output}', allowed values are 'md' or 'html'.")

    return full_link


# create prepopulated susbtitution functions for md and html
substitute_root_link_md = partial(substitute_root_link, output="md")
substitute_root_link_html = partial(substitute_root_link, output="html")


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
    # construct relative path to root
    num_back = page.file.src_uri.count("/")
    if page.file.name != "index":
        num_back += 1
    to_root = "/".join([".."] * num_back)
    # pre-populate substitution functions with relative root string
    repl_md = partial(substitute_root_link_md, to_root)
    repl_html = partial(substitute_root_link_html, to_root)
    # regex to find root links
    re_link_md = r"\[(?P<label>[^\]]*)\]\(\/(?P<link>[^\)]*)\)"
    re_link_html = r"<a .*href=\"\/(?P<link>[^\">]*)\">(?P<label>[^<]*)</a>"
    # do substitution in md
    markdown = re.sub(
        pattern=re_link_md,
        string=markdown, 
        repl=repl_md
    )
    # do substitution in html
    markdown = re.sub(
        pattern=re_link_html,
        string=markdown, 
        repl=repl_html
    )

    return markdown
