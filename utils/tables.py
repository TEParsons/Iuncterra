import re
import pandas as pd
from mkdocs.structure import pages, files
from mkdocs import config


def construct_table(match):
    """
    Load in table from spec and convert it to Markdown

    Parameters
    ----------
    match : re.Match
        Regex match for the table
    """
    # get params from regex match
    path, ext, index = match.groups()
    # read in data according to path
    if ext == ".xlsx":
        if index:
            data = pd.read_excel(path + ext, sheet_name=index[1:])
        else:
            data = pd.read_excel(path + ext)
    elif ext in (".csv", ".tsv"):
        data = pd.read_csv(path + ext)
    else:
        raise ValueError(f"Unrecognised file type {ext}")
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
    # regex to find IPA strings
    re_table = r"\|(.*)(\.csv|\.tsv|\.xlsx)(:.*)?\|"
    # do substitution
    return re.sub(
        pattern=re_table,
        string=markdown, 
        repl=construct_table
    )