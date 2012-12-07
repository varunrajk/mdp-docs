# -*- coding: utf-8 -*-
#
# MDP-toolkit documentation build configuration file, created by
# sphinx-quickstart on Mon Jul 19 16:38:42 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import mdp

def get_mdp_version():
    return mdp.__version__

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.autosummary',
              'sphinx.ext.extlinks',
              'extapi',
              'codesnippet',
              'version_string',
              'linkcheck2',
              'descriptions_string',]
#              'download_links']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MDP'

version = get_mdp_version()
release = get_mdp_version()

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['main.rst',
                    'tutorial/using_mdp_is_as_easy.rst',
                    ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'mdp'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

html_title = "Modular toolkit for Data Processing (MDP)"


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['talks', '_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d %X %Z'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# A list of regular expressions that match URIs that should not be checked
# when doing a ``linkcheck`` build.
linkcheck2_ignore = [r'http://mdp-toolkit.*']

# Output file base name for HTML help builder.
htmlhelp_basename = 'MDP-toolkitdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('pdf', 'MDP-tutorial.tex',
   ur'''Modular toolkit for Data Processing\\\mbox{ }\\Tutorial''',
   u'Authors: MDP Developers', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'examples/logo/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = False

# ========== Extensions configuration ===============
# doctest
trim_doctest_flags = True
doctest_global_setup ="""
import mdp
import numpy as np
np.random.seed(0)
"""

# codesnippet
# set path for download links in codesnippet
codesnippet_path = "code"

# wheter to strip '# doctest: ...' (True by default)
# codesnippet_strip_doctest_directives = True

# extlinks
prefix = '%s/%s' %(mdp.__homepage__, codesnippet_path)
extlinks = {'code_snippet': (prefix+'/%s', 'code_snippet')}

# extapi
extapi_epydoc_path = os.path.join('build_api','api')
extapi_link_prefix = '%s/api'%mdp.__homepage__

# download links
#download_link = ('http://sourceforge.net/projects/mdp-toolkit/files/mdp-toolkit'
#                 '/%s/MDP-%s.tar.gz/download'%(version, version))

# overwrite default signature and members documentation
# features of autodoc

def setup(app):
    from sphinx.ext.autodoc import cut_lines
    def autodoc_skip_member(app, what, name, obj, skip, options):
        # only document public nodes, but none of their members! 
        if name.startswith('_') or what != 'module':
            return True
        else:
            return False

    def autodoc_process_signature(app, what, name, obj, options,
                                  signature, return_annotation):
        # remove signature altogether
        return (None, None)

    def autodoc_process_docstring(app, what, name, obj, options, lines):
        # add link to api at the end of the docstring
        shortname = name.split('.')[-1]
        link = 'Full API documentation: :api:`%s <%s>`' % (name, shortname)
        lines.extend(['', link])

    # app.connect(event, callback)
    app.connect('autodoc-process-signature', autodoc_process_signature)
    app.connect('autodoc-skip-member', autodoc_skip_member)
    app.connect('autodoc-process-docstring', autodoc_process_docstring)
