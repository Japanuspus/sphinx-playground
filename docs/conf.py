# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../'))


# -- Project information -----------------------------------------------------
import os

project = 'sphinx test'
copyright = '2019, NCC'
author = 'NCC'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Default role (to be used for `foo`) is :any:
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-any
default_role = "any"

extensions = [
    'sphinx.ext.autodoc',      # generate API documentation by scanning code
    'sphinx.ext.napoleon',     # allow google-style docstrings
    'sphinxcontrib.plantuml',  # allow embedded plantuml UML diagrams. Has dependencies
    'sphinx.ext.graphviz',     # allow embedded graphviz figures. Requires graphviz on path
    'recommonmark',             # Allow markdown files
    'sphinx.ext.mathjax',       # allow latex math input
    'sphinx_autodoc_typehints', # must come after napoleon, https://github.com/agronholm/sphinx-autodoc-typehints
]

# Configure recommonmark
# http://www.sphinx-doc.org/en/master/usage/markdown.html
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Configure m2r -- not active as markdown parser has issues
# 'm2r'  # Allow markdown within ReST files
# https://github.com/miyakogi/m2r#sphinx-integration
# source_suffix = ['.rst', '.md']

# Configure napoleon docstring parser
# http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
napoleon_numpy_docstring = False  # only allow google docstring
napoleon_google_docstring = True


# Configure sphinx_autodoc_typehints
always_document_param_types = True

# Configure plantuml
# https://pypi.org/project/sphinxcontrib-plantuml/
plantuml = os.getenv('PLANTUML')
plantuml_output_format = 'svg_img'


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'default'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


