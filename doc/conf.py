import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))
import scortest

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              #'sphinx_gallery.gen_gallery',
              ]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'scortest'
copyright = '2018, Xavier Dupré'
author = 'Xavier'
version = "0.1"
release = version
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {}
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

htmlhelp_basename = 'scortest'
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

latex_documents = [
    (master_doc,
     'scortest.tex',
     'Documentation',
     'Xavier Dupré',
     'manual'),
]

texinfo_documents = [
    (master_doc, 'scortest_ci', 'scortest_ci Documentation',
     author, 'scortest_ci', 'One line description of project.',
     'Miscellaneous'),
]

intersphinx_mapping = {'https://docs.python.org/': None}

sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs' : os.path.join(os.path.dirname(__file__), '../examples'),
    # path where to save gallery generated examples
    'gallery_dirs'  : 'auto_examples'
}
