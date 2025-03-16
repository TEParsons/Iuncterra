import re
from mkdocs.structure import pages, files
from mkdocs import config


def on_page_markdown(markdown: str, page: pages.Page, config: config.Config, files: files.File) -> str:
    """
    Convert codeblocks with language set to `statblock` into formatted stat blocks.

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
    def format_codeblock(match):
        system = match.group("system")
        content = match.group("content")

        if system:
            label = f"Statblock ({system})"
        else:
            label = f"Statblock"

        print(system, content)
        
        return (
            f"<details class='statblock {system}' markdown>\n"
            f"<summary>\n"
            f"{label}\n"
            f"</summary>\n"
            f"{content}\n"
            f"</details>\n"
        )

    re_statblock = r"```statblock:?(?P<system>[\w\d]*)?\n(?P<content>.*?)```"
    return re.sub(
        pattern=re_statblock,
        repl=format_codeblock,
        string=markdown,
        flags=re.DOTALL
    )