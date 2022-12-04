# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import pathlib
import pprint
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# sys.path.insert(0, '.')
# sys.path.insert(0, os.path.abspath('../../../build'))
# sys.path.insert(0, os.path.abspath('../../../build/docs'))
# sys.path.insert(0, os.path.abspath('../../../build/.doctrees'))
# sys.path.insert(0, os.path.abspath('../../../build/docs/api-docs'))
# pprint.pprint(sys.path)
sys.path.append(os.path.abspath('exts'))
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix() + "/src/")

project = 'properly'
copyright = '2022, Geir'
author = 'Geir Ekeberg Emblemsvåg'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    # 'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinxcontrib.restbuilder',
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

# Defines RST output for GitHub Wiki
rst_file_suffix = '.rst'
rst_link_suffix = ''
rst_line_width = 78
rst_indent = 4


def rst_file_transform(docname: str) -> str:
    if docname == 'index':
        docname = 'home'
    return docname.title() + rst_file_suffix


def rst_link_transform(docname: str) -> str:
    if docname == 'index':
        return 'wiki'
    return 'wiki/' + docname.title()
