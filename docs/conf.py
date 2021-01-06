# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Project information -----------------------------------------------------
project = 'my project'
copyright = '2019, Janus'
author = 'Janus'

# -- Path setup --------------------------------------------------------------

# Rely on editable install for establishing packages on path
import os

# -- General configuration ---------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Default role (to be used for `foo`) is :any:
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-any
default_role = "any"

# -- Options for HTML output -------------------------------------------------

html_theme = 'default'
html_static_path = ['_static']

# -- Extensions --------------------------------------------------------------

extensions = []

# Configure recommonmark
# http://www.sphinx-doc.org/en/master/usage/markdown.html
extensions.append('recommonmark')  # Allow markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Configure plantuml. allow embedded plantuml UML diagrams. Has dependencies including graphviz
# https://pypi.org/project/sphinxcontrib-plantuml/
extensions.append('sphinxcontrib.plantuml')  # 
extensions.append('sphinx.ext.graphviz')  # allow embedded graphviz figures. Requires graphviz on path
plantuml = os.getenv('PLANTUML')
plantuml_output_format = 'svg_img'

# Allow mathjax for math
extensions.append('sphinx.ext.mathjax')  # allow latex math input


# Configure autodoc
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_typehints
extensions.append('sphinx.ext.autodoc')  # generate API documentation by scanning code
autodoc_typehints = 'description'  # new in sphinx 3.0

# Configure napoleon docstring parser
# http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration
extensions.append('sphinx.ext.napoleon')  # allow google-style docstrings
napoleon_numpy_docstring = False  # only allow google docstring
napoleon_google_docstring = True