import shutil
from pathlib import Path


def on_html_collect_pages(app):
    for f in app.builder.config.rawfiles:
        src = str(Path(app.srcdir) / Path(f))
        dst = str(Path(app.builder.outdir) / Path(f))
        if Path(src).is_file():
            shutil.copy(src, dst)
        else:
            shutil.copytree(src, dst)
    return ()


def setup(app) -> None:
    app.add_config_value("rawfiles", [], "html")
    app.connect("html-collect-pages", on_html_collect_pages)
