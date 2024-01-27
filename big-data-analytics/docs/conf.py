"""Sphinx configuration."""
project = "Big Data Analytics"
author = "Wenhan Li"
copyright = "2024, Wenhan Li"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
