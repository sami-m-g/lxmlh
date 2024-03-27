# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime
import pathlib

project = 'lxmlh'
copyright = f'{datetime.date.today().year}, Mina Sami'
author = 'Mina Sami'

version_file = pathlib.Path(__file__).parent.parent / 'lxmlh' / 'VERSION'
# Read the version number from VERSION file
with open(version_file, 'r', encoding='UTF-8') as vf:
    # The full version, including alpha/beta/rc tags
    release_list = vf.read().strip().split('.')
release = '.'.join(release_list)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
