#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# NEXT STEPS:
# + DESCRIPTION & META_IMAGE
# + make it smartphone-friendly
# + tuto pour soumettre un article + JS form that submits a PR + email to send infos
#    cf. https://gist.github.com/bmcbride/62600e48274961819084
NOINDEX = True  # temporary

import logging
logging.root.setLevel(logging.INFO)

SITENAME = 'Hôpitaux À Défendre : GHM @ Grenoble'
SITESUBTITLE = 'Suivi de la lutte des employés du Groupe Hospitalier Mutualiste à Grenoble'
DESCRIPTION = '''

'''

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# "Open Graph tags do not acknowledge <base>, and should always have full absolute URLs" - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base
META_IMAGE = ''

LINKS = (
    ("Touche pas à ma Mut' - Collectif des usagers des cliniques mutualistes de Grenoble", "https://www.touchepasamamut.fr"),
    ("Page Wikipédia du GHM de Grenoble", "https://fr.wikipedia.org/wiki/Groupe_hospitalier_mutualiste_de_Grenoble"),
    ("Site officiel du GHM de Grenoble", "https://www.ghm-grenoble.fr"),
    ("Sources de ce site web", "https://github.com/hopitaux-a-defendre/ghm-grenoble/"),
)

PATH = './content'
OUTPUT_PATH = './output'

MARKDOWN = {'output_format': 'html5'}

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ('i18n_subsites', 'representative_image', 'w3c_validate')
logging.getLogger('i18n_subsites.i18n_subsites').setLevel(logging.DEBUG)
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'

THEME = '../html5-dopetrope'
DISABLE_LATEST_ARTICLES= True

# Disabling generation of unnecessary pages:
ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None


#######################################
# Config options specific to dev-mode:
#######################################

SITEURL = ''
RELATIVE_URLS = True

# Making output generation faster:
STATIC_CHECK_IF_MODIFIED = True # create links instead of copying files
STATIC_CREATE_LINKS = True # compare mtimes of content and output files, and only copy content files that are newer than existing output files
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True
