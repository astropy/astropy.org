# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'astropy.org'
copyright = '2026, Astropy Community'
author = 'Astropy Community'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'LICENSE.rst',
    'README.md',
    'CONTRIBUTING.md',
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'astropy'

html_static_path = ['_static']

html_theme_options = {
    "show_prev_next": False,
    "sst_is_root": True,
}

html_sidebars = {
    "*": [],
}

html_css_files = [
    "css/astropy-org.css"
]
