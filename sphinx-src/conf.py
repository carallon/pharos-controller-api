# -*- coding: utf-8 -*-
#
# Controller API Documentation build configuration file.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'2022 Pharos Architectural Controls Ltd'
author = u'Carallon Ltd'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'6.0'
# The full version, including alpha/beta/rc tags.
release = u'6.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Exclude warnings about documents not included in toctree
suppress_warnings = ['toc.excluded']

# Get vendor variant
# Check if we're building on RTD, in which case use project name to determine variant
if 'READTHEDOCS' in os.environ:
    rtd_project = os.environ.get('READTHEDOCS_PROJECT')
    print('Building for Read the Docs, project: {}'.format(rtd_project))
    rtd_project = rtd_project.lower()
    if 'mosaic' in rtd_project:
        variant = 'mosaic'
    else:
        # default to Pharos
        variant = 'pharos'
else:
    variant = os.environ.get('VARIANT', 'pharos').lower()

# Get product type
product = os.environ.get('PRODUCT', 'designer').lower()

# Substitutions
if variant == 'mosaic':
    print('Building Mosaic variant')
    rst_prolog = """
    .. |Vendor| replace:: Mosaic
    .. |Designer| replace:: Designer
    .. |LPC| replace:: MSC
    .. |LPC X| replace:: MSC X
    .. |TPC| replace:: MTPC
    .. |VLC| replace:: Atlas
    .. |VLC+| replace:: Atlas Pro
    .. |TPS| replace:: M-TS
    .. |XPC| replace:: XPC
    .. |EXT| replace:: TPC-RIO
    .. |EDN| replace:: EDN
    .. |EDN 20| replace:: EDN 20
    .. |EDN 10| replace:: EDN 10
    """
else:
    print('Building Pharos variant')
    rst_prolog = """
    .. |Vendor| replace:: Pharos
    .. |Designer| replace:: Designer
    .. |LPC| replace:: LPC
    .. |LPC X| replace:: LPC X
    .. |TPC| replace:: TPC
    .. |VLC| replace:: VLC
    .. |VLC+| replace:: VLC+
    .. |TPS| replace:: TPS
    .. |XPC| replace:: XPC
    .. |EXT| replace:: EXT
    .. |EDN| replace:: EDN
    .. |EDN 20| replace:: EDN 20
    .. |EDN 10| replace:: EDN 10
    """

# Include/Exclude based on product type
if product == 'expert':
    print('Building for Expert product')
    rst_prolog += """
    .. |Product| replace:: Expert
    """
    project = u'Expert API v' + version
    tags.add('expert')
    # Items which are removed from the Expert documentation
    exclude_patterns.append('lua-api/*')
    exclude_patterns.append('queryjs/*')
    exclude_patterns.append('*/command.rst')
    exclude_patterns.append('*/content-targets.rst')
    exclude_patterns.append('*/group.rst')
    exclude_patterns.append('*/lua-variable.rst')
    exclude_patterns.append('*/replication.rst')
    exclude_patterns.append('*/text-slots.rst')
    exclude_patterns.append('*/timeline.rst')
    exclude_patterns.append('*/trigger.rst')
    exclude_patterns.append('*/temperature.rst')
    exclude_patterns.append('*/enumerated-rio-types.rst')

if product == 'designer':
    print('Building for Designer product')
    rst_prolog += """
    .. |Product| replace:: Designer
    """
    project = u'Designer API v' + version
    tags.add('designer')
    exclude_patterns.append('*/mode.rst')
    exclude_patterns.append('*/space.rst')

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
#
html_theme = 'furo'
html_title = project

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

if variant == 'mosaic':
    html_theme_footer_icons = [
        {
            "name": "etcconnect.com",
            "url": "https://www.etcconnect.com",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                <path d="M 13.340655,10.689396 C 12.968429,10.66694 12.677747,10.589097 12.349206,10.423933 11.711141,10.103167 11.212522,9.5217978 10.980318,8.8278677 10.879229,8.5257626 10.849272,8.2930437 10.860902,7.9001776 c 0.01364,-0.461172 0.0675,-0.6823139 0.264317,-1.0854194 0.347908,-0.7125694 1.002107,-1.2316176 1.798121,-1.4266497 0.159366,-0.039045 0.221589,-0.040922 1.58259,-0.047708 l 1.416705,-0.00707 v 0.048556 c 0,0.026705 -0.01876,0.098707 -0.0417,0.1600024 -0.05586,0.1492774 -0.197818,0.2976788 -0.362251,0.378674 l -0.126966,0.062541 -1.054544,0.011017 c -1.252576,0.013085 -1.280428,0.016822 -1.658134,0.2227142 -0.51677,0.2816941 -0.895819,0.7726562 -1.034749,1.3402651 -0.05749,0.234887 -0.05749,0.6399814 0,0.8748681 0.09352,0.3820936 0.272008,0.6927996 0.566272,0.9857669 0.287447,0.2861766 0.589617,0.4715278 0.917346,0.562693 0.151969,0.042276 0.178936,0.043164 1.51341,0.049974 L 16,10.037329 v 0.04645 c 0,0.152136 -0.169438,0.404372 -0.337994,0.503154 -0.177383,0.103953 -0.182813,0.10446 -1.180248,0.110072 -0.510597,0.0029 -1.024091,-4.43e-4 -1.141103,-0.0076 z M 0.01336106,10.610366 c 0.03418733,-0.215352 0.18985083,-0.41061 0.41697058,-0.523034 l 0.125298,-0.06202 2.25136936,-0.0052 2.2513714,-0.0052 -0.010236,0.07645 c -0.02563,0.190923 -0.1896174,0.416266 -0.3701436,0.508569 -0.1841203,0.09414 -0.132185,0.0922 -2.4751924,0.09244 L 3.0838486e-4,10.692557 Z M 8.026879,8.3475069 l -0.00491,-2.3450573 -1.0806904,-0.005 -1.0806884,-0.005 0.012699,-0.082035 c 0.03171,-0.2046473 0.199892,-0.4136163 0.4134655,-0.5137176 l 0.1105915,-0.051835 2.2580232,-0.00507 2.2580261,-0.00507 v 0.047863 c 0,0.1726626 -0.181573,0.4210741 -0.390632,0.5344289 l -0.121897,0.066094 -0.8413198,0.00967 -0.8413197,0.00967 -0.00491,2.3450588 -0.00491,2.3450569 H 8.3700952 8.0317894 Z M 0.01200647,8.342093 C 0.04115453,8.1294356 0.20834707,7.9165564 0.42653275,7.8142916 l 0.11059128,-0.051834 2.26053407,-0.00508 2.2605344,-0.00506 -0.012769,0.082438 C 5.0025953,8.111144 4.734109,8.3598053 4.4236082,8.410652 4.3538654,8.422076 3.4601338,8.4295376 2.1542725,8.4296048 L 0,8.4297223 Z M 0.01292023,5.9146041 C 0.0449694,5.7141807 0.21205687,5.5042962 0.42118751,5.4017656 l 0.11604404,-0.056893 2.26054545,-0.00515 2.2605481,-0.00515 -0.012792,0.082513 C 5.013747,5.6222243 4.8457735,5.8310861 4.6319957,5.9312844 l -0.1105908,0.051834 -2.260534,0.00507 -2.26053420388,0.00507 0.0125866939,-0.078656 z"
                />
                </svg>
            """,
            "class": "",
        },
    ]

    html_theme_options = {
        'light_logo': 'mosaic-logo-light.png',
        'dark_logo': 'mosaic-logo-dark.png',
        'top_of_page_button': 'None',
        'footer_icons': html_theme_footer_icons,
    }
else:
    html_theme_footer_icons = [
        {
            "name": "pharoscontrols.com",
            "url": "https://www.pharoscontrols.com",
            "html": """
                <svg stroke="#0080ff" fill="#0080ff" stroke-width="0" viewBox="0 0 149 145">
                <path d="m 136.71125,30.7216 a 4.6082501,4.6082501 0 0 1 -4.60825,4.60825 4.6082501,4.6082501 0 0 1 -4.60825,-4.60825 4.6082501,4.6082501 0 0 1 4.60825,-4.608251 4.6082501,4.6082501 0 0 1 4.60825,4.608251 z M 79.876248,4.6082501 A 4.6082501,4.6082501 0 0 1 75.267998,9.2165003 4.6082501,4.6082501 0 0 1 70.659748,4.6082501 4.6082501,4.6082501 0 0 1 75.267998,0 4.6082501,4.6082501 0 0 1 79.876248,4.6082501 Z M 149.00025,99.845398 a 4.6082501,4.6082501 0 0 1 -4.60825,4.608252 4.6082501,4.6082501 0 0 1 -4.60825,-4.608252 4.6082501,4.6082501 0 0 1 4.60825,-4.60825 4.6082501,4.6082501 0 0 1 4.60825,4.60825 z m -38.402,39.938602 a 4.6082501,4.6082501 0 0 1 -4.60825,4.60825 4.6082501,4.6082501 0 0 1 -4.60825,-4.60825 4.6082501,4.6082501 0 0 1 4.60825,-4.60825 4.6082501,4.6082501 0 0 1 4.60825,4.60825 z m -64.515799,0 a 4.6082501,4.6082501 0 0 1 -4.60825,4.60825 4.6082501,4.6082501 0 0 1 -4.60825,-4.60825 4.6082501,4.6082501 0 0 1 4.60825,-4.60825 4.6082501,4.6082501 0 0 1 4.60825,4.60825 z M 9.2165003,92.164902 A 4.6082501,4.6082501 0 0 1 4.6082501,96.773152 4.6082501,4.6082501 0 0 1 0,92.164902 a 4.6082501,4.6082501 0 0 1 4.6082501,-4.60825 4.6082501,4.6082501 0 0 1 4.6082502,4.60825 z m 13.8247507,-59.9072 a 4.6082501,4.6082501 0 0 1 -4.60825,4.60825 4.6082501,4.6082501 0 0 1 -4.608251,-4.60825 4.6082501,4.6082501 0 0 1 4.608251,-4.60825 4.6082501,4.6082501 0 0 1 4.60825,4.60825 z m 30.721678,96.773308 a 6.14433,6.14433 0 0 1 -6.14433,6.14433 6.14433,6.14433 0 0 1 -6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,6.14433 z m 52.226801,0 a 6.14433,6.14433 0 0 1 -6.144332,6.14433 6.14433,6.14433 0 0 1 -6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,-6.14433 6.14433,6.14433 0 0 1 6.144332,6.14433 z m 32.2576,-33.793911 a 6.14433,6.14433 0 0 1 -6.14433,6.144331 6.14433,6.14433 0 0 1 -6.14433,-6.144331 6.14433,6.14433 0 0 1 6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,6.14433 z m -9.216,-56.834999 a 6.14433,6.14433 0 0 1 -6.14433,6.14433 6.14433,6.14433 0 0 1 -6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,6.14433 z M 81.412427,16.8969 a 6.14433,6.14433 0 0 1 -6.14433,6.14433 6.14433,6.14433 0 0 1 -6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,6.14433 z M 23.04123,89.092796 a 6.14433,6.14433 0 0 1 -6.14433,6.14433 6.14433,6.14433 0 0 1 -6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,6.14433 z m 10.7526,-49.154697 a 6.14433,6.14433 0 0 1 -6.14433,6.14433 6.14433,6.14433 0 0 1 -6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,-6.14433 6.14433,6.14433 0 0 1 6.14433,6.14433 z m 13.824679,9.216499 a 7.6804099,7.6804099 0 0 1 -7.68041,7.68041 7.6804099,7.6804099 0 0 1 -7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,7.68041 z m -7.680397,36.866001 a 7.6804099,7.6804099 0 0 1 -7.68041,7.68041 7.6804099,7.6804099 0 0 1 -7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,7.68041 z M 62.97941,115.206 a 7.6804099,7.6804099 0 0 1 -7.68041,7.68041 7.6804099,7.6804099 0 0 1 -7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,7.68041 z m 38.402,0 a 7.6804099,7.6804099 0 0 1 -7.680414,7.68041 7.6804099,7.6804099 0 0 1 -7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.680414,7.68041 z m 23.041,-26.113204 a 7.6804099,7.6804099 0 0 1 -7.68041,7.68041 7.6804099,7.6804099 0 0 1 -7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,7.68041 z m -6.144,-41.474197 a 7.6804099,7.6804099 0 0 1 -7.68041,7.68041 7.6804099,7.6804099 0 0 1 -7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,7.68041 z M 82.948408,32.257702 a 7.6804099,7.6804099 0 0 1 -7.68041,7.68041 7.6804099,7.6804099 0 0 1 -7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,-7.68041 7.6804099,7.6804099 0 0 1 7.68041,7.68041 z m 1.53608,18.432999 a 9.2164898,9.2164898 0 0 1 -9.21649,9.216489 9.2164898,9.2164898 0 0 1 -9.21649,-9.216489 9.2164898,9.2164898 0 0 1 9.21649,-9.21649 9.2164898,9.2164898 0 0 1 9.21649,9.21649 z M 64.51549,59.9072 A 9.2164898,9.2164898 0 0 1 55.299,69.12369 9.2164898,9.2164898 0 0 1 46.08251,59.9072 9.2164898,9.2164898 0 0 1 55.299,50.69071 9.2164898,9.2164898 0 0 1 64.51549,59.9072 Z m -4.6083,21.505199 a 9.2164898,9.2164898 0 0 1 -9.216489,9.21649 9.2164898,9.2164898 0 0 1 -9.21649,-9.21649 9.2164898,9.2164898 0 0 1 9.21649,-9.216489 9.2164898,9.2164898 0 0 1 9.216489,9.216489 z m 13.824803,16.896904 a 9.2164898,9.2164898 0 0 1 -9.21649,9.216487 9.2164898,9.2164898 0 0 1 -9.21649,-9.216487 9.2164898,9.2164898 0 0 1 9.21649,-9.21649 9.2164898,9.2164898 0 0 1 9.21649,9.21649 z m 21.505096,0 a 9.2164898,9.2164898 0 0 1 -9.21649,9.216487 9.2164898,9.2164898 0 0 1 -9.216489,-9.216487 9.2164898,9.2164898 0 0 1 9.216489,-9.21649 9.2164898,9.2164898 0 0 1 9.21649,9.21649 z M 109.06189,81.412399 a 9.2164898,9.2164898 0 0 1 -9.216492,9.21649 9.2164898,9.2164898 0 0 1 -9.21649,-9.21649 9.2164898,9.2164898 0 0 1 9.21649,-9.216489 9.2164898,9.2164898 0 0 1 9.216492,9.216489 z M 104.45359,59.9072 a 9.2164898,9.2164898 0 0 1 -9.216491,9.21649 9.2164898,9.2164898 0 0 1 -9.21649,-9.21649 9.2164898,9.2164898 0 0 1 9.21649,-9.21649 9.2164898,9.2164898 0 0 1 9.216491,9.21649 z M 89.092698,76.8041 a 13.8247,13.8247 0 0 1 -13.8247,13.8247 13.8247,13.8247 0 0 1 -13.824701,-13.8247 13.8247,13.8247 0 0 1 13.824701,-13.8247 13.8247,13.8247 0 0 1 13.8247,13.8247 z" />
                />
                </svg>
            """,
            "class": "",
        },
    ]

    html_theme_options = {
        'light_logo': 'pharos-logo-light.png',
        'dark_logo': 'pharos-logo-dark.png',
        'top_of_page_button': 'None',
        'footer_icons': html_theme_footer_icons,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ControllerApi'


# -- Options for LaTeX output ---------------------------------------------

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
    (master_doc, 'ControllerApi.tex', u'Controller API',
     u'Carallon Ltd', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'controllerapi', u'Controller API',
     [u'Carallon Ltd'], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ControllerApi', u'Controller API',
     u'Carallon Ltd', 'ControllerApi',
     'User documentation for Pharos Controller web and Lua APIs.',
     'Miscellaneous'),
]
