import re
import os
import logging
import pandas as pd
from pathlib import Path
from functools import partial
from mkdocs.structure import pages, files
from mkdocs import config


def construct_table(page: pages.Page, match: re.Match):
    """
    Load in table from spec and convert it to Markdown

    Parameters
    ----------
    page : pages.Page
        MkDocs page object
    match : re.Match
        Regex match for the table
    """
    # get params from regex match
    path, ext, index = match.groups()
    # remove starting /
    if path.startswith("/"):
        path = path[1:]
    # get possible files from path
    rel_path = Path(page.file.abs_src_path).parent / (path + ext)
    site_path = Path(os.getcwd()) / "source" / (path + ext)
    # use whichever one exists
    if rel_path.is_file():
        path = str(rel_path)
    elif site_path.is_file():
        path = str(site_path)
    else:
        logging.error(
            f"Could not find file {path + ext} as either relative ({rel_path}) or absolute "
            f"({site_path}). Current working directory is {os.getcwd()}"
        )
        return path + ext + index
    # read in data according to path
    try:
        if ext == ".xlsx":
            if index:
                data = pd.read_excel(path, sheet_name=index[1:])
            else:
                data = pd.read_excel(path)
        elif ext in (".csv", ".tsv"):
            data = pd.read_csv(path)
        else:
            logging.error(f"Unrecognised file type {ext}")
            return path + ext + index
    except Exception as err:
        logging.error(
            f"Failed to load table. Reason:\n"
            f"{err}"
        )
    # start off with blank string
    content = ""
    # make header
    headings = [str(head) for head in data.columns]
    borders = ["---" for head in data.columns]
    content += (
        f"| {' | '.join(headings)} |\n"
        f"| {' | '.join(borders)} |\n"
    )
    # make each row
    for row in data.itertuples():
        cells = [str(cell) for cell in row[1:]]
        content += (
            f"| {' | '.join(cells)} |\n"
        )

    return content


def on_page_markdown(markdown: str, page: pages.Page, config: config.Config, files: files.File) -> str:
    """
    Parse table markdown.

    Add a table from an xlsx file like so:
    ```
    [title](path/to/table.xlsx:page)
    ```
    ...or from a .csv like so:
    ```
    [title](path/to/table.csv)
    ```

    The table (or page, if given) will be rendered as a Markdown table.

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
    # pre-populate substitution function with relative root string
    repl = partial(construct_table, page)
    # regex to find IPA strings
    re_table = r"\|(.*)(\.csv|\.tsv|\.xlsx)(:.*)?\|"
    # do substitution
    return re.sub(
        pattern=re_table,
        string=markdown, 
        repl=repl
    )