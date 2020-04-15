# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# import textext

# -- Project information -----------------------------------------------------

project = 'TexText'
copyright = '2020, Alexander Blinne, Brian Clarke, Florent Becker, Jan Winkler, Pit Garbe, Pauli Virtanen, Robert Szalai, Rafal Kolanski, Sergei Izmailov, Toru Araki, @veltsov, Vladislav Gavryusev'
author = 'Alexander Blinne, Brian Clarke, Florent Becker, Jan Winkler, Pit Garbe, Pauli Virtanen, Robert Szalai, Rafal Kolanski, Sergei Izmailov, Toru Araki, @veltsov, Vladislav Gavryusev'

# The full version, including alpha/beta/rc tags
release = open("../../textext/VERSION").readline().strip()

# The short X.Y version (for doc title)
version = ".".join(release.split(".")[:2])

# Last stable 0.x release (compatible with Inkscape 0.92)
release_0x = "0.11.0"


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

nitpicky = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_favicon = "../../icons/logo.ico"

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'textextdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'TexText.tex', 'TexText Documentation',
     'Alexander Blinne, Brian Clarke, Florent Becker, Jan Winkler, Pit Garbe, Pauli Virtanen, Robert Szalai, Rafal Kolanski, Sergei Izmailov, Toru Araki, @veltsov, Vladislav Gavryusev', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'TexText', 'TexText Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'TexText', 'TexText Documentation',
     author, 'TexText', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

extlinks = {
    'issue_num': ('https://github.com/textext/textext/issues/%s', '#'),
    'issue': ('https://github.com/textext/textext/issues/%s', 'issue #'),
    'bb_issue_num': ('https://bitbucket.org/pv/textext/issues/%s', 'bb#'),
    'bb_issue': ('https://bitbucket.org/pv/textext/issues/%s', 'issue bb#'),

    # Links to current stable release compatible with Inkscape >= 1.0
    'textext_download_zip':    ('https://github.com/textext/textext/releases/download/{release}/TexText-%s-{release}.zip'.format(**locals()), 'v{release}-'.format(**locals())),
    'textext_download_tgz':    ('https://github.com/textext/textext/releases/download/{release}/TexText-%s-{release}.tar.gz'.format(**locals()), 'v{release}-'.format(**locals())),
    'textext_download_exe':    ('https://github.com/textext/textext/releases/download/{release}/TexText-%s-{release}.exe'.format(**locals()), 'v{release}-'.format(**locals())),
    'textext_current_release_page':    ('https://github.com/textext/textext/releases/tag/{release}#%s'.format(**locals()), 'v{release}'.format(**locals())),

    # Links to last stable release compatible with Inkscape 0.92
    'textext_0x_download_zip': ('https://github.com/textext/textext/releases/download/{release_0x}/TexText-%s-{release_0x}.zip'.format(**locals()), 'v{release_0x}-'.format(**locals())),
    'textext_0x_download_tgz': ('https://github.com/textext/textext/releases/download/{release_0x}/TexText-%s-{release_0x}.tar.gz'.format(**locals()), 'v{release_0x}-'.format(**locals())),
    'textext_0x_download_exe': ('https://github.com/textext/textext/releases/download/{release_0x}/TexText-%s-{release_0x}.exe'.format(**locals()), 'v{release_0x}-'.format(**locals())),
    'textext_0x_current_release_page': ('https://github.com/textext/textext/releases/tag/{release_0x}#%s'.format(**locals()),'v{release_0x}'.format(**locals())),
}
