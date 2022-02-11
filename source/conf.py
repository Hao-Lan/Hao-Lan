# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Development Notes"
copyright = '2021, HaoLan'
author = 'HaoLan'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'plantweb.directive',
    # "sphinx.ext.duration",
    # "sphinx.ext.graphviz",  # graphviz pic
    # "sphinx.ext.imgmath",
]

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
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# language = 'zh_CN'
html_search_language = "zh_CN"

rst_epilog = """

"""
rst_prolog = """

"""
numfig = True

latex_engine = 'xelatex'

latex_use_xindy = True

latex_elements = {
    #     'fontpkg': r'''
    # \setmainfont{DejaVu Serif}
    # \setsansfont{DejaVu Sans}
    # \setmonofont{DejaVu Sans Mono}
    # ''',
    'preamble': r'''
\usepackage{ctex}
''',
    'fncychap': '',
    # 'printindex': r'\footnotesize\raggedright\printindex',
    # "papersize": "a4paper",
    # "passoptionstopackages": "模型应用笔记",
    'extraclassoptions': 'openany,oneside',
}

#
# https://juejin.im/post/5c7253c2e51d4512543327b4
#
# latex_logo = '_static/imgs/20220211111829.png'
latex_show_urls = 'footnote'
