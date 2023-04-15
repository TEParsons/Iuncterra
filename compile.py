import markdown
import markmoji
from pathlib import Path
import sys

sys.path.append("G:\\My Drive\\Projects\\Obsidian Wiki\\obsidian-wiki")
import obsidian_wiki

md = markdown.Markdown(extensions=["extra", "admonition", "nl2br", "meta", markmoji.Markmoji()])
__folder__ = Path(__file__).parent

wiki = obsidian_wiki.Wiki(
    name="Iuncterra",
    source=__folder__ / "source",
    dest=__folder__ / "docs",
    templates=__folder__ / "source" / "_templates" / "html",
    interpreter=md
)

wiki.compile()

import webbrowser
webbrowser.open("file://" + str(Path("docs/index.html").absolute()))
