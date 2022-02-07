#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# NEXT STEPS:
# Feedbacks Tanguy :
#   * faire remonter le bandeau du bas en haut pour que l'on comprenne le but du site dès la première vue d'écran.
#   * titre cryptique : "Hôpitaux À Défendre : GHM @ Grenoble" peut-être trouver un titre plus explicite (le sous-titre est beaucoup plus clair)
#   * utiliser une police d'écriture sans sérif
#   * relayer les communiqués et tracts des personnels en lutte
#   * rajouter un lien vers une page "comment agir"
# + tuto pour soumettre un article + JS form that submits a PR + email to send infos
#    cf. https://gist.github.com/bmcbride/62600e48274961819084
# + rédiger page "Chronologie" / timeline avec Lise ?
# + mentions légales
# + section contacts ?

import logging
logging.root.setLevel(logging.INFO)
logging.getLogger('pelican.utils').setLevel(logging.WARN)  # avoids very verbose "-> Copying ..." logs

SITENAME = 'Hôpitaux À Défendre : GHM @ Grenoble'
SITESUBTITLE = 'Suivi de la lutte des soignants du Groupe Hospitalier Mutualiste à Grenoble'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

THEME = '../html5-dopetrope'
DISPLAY_HOMEPAGE_ON_MENU = True
MENUITEMS = (
    ('Liens', '#footer'),
)
DISABLE_LATEST_ARTICLES= True

ABOUT_TEXT = '''
Le <b>Groupe Hospitalier Mutualiste de Grenoble</b>, surnommé « La Mut’ », autrefois géré par la mutuelle ADREA, a été racheté par le groupe <b>AVEC</b> (ex Doctegestio) en octobre 2020, malgré une opposition des salariés et usagers. Ce rachat pose plusieurs problèmes : menace de passer au privé à but lucratif, gel des embauches, management toxique...
<br>
Ce site web vise à servir de <b>revue de presse</b> pour couvrir cette affaire.
'''
# "Open Graph tags do not acknowledge <base>, and should always have full absolute URLs" - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base
META_IMAGE = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Dr_Hermitte_street_in_grenoble_%28outside%29.jpg/640px-Dr_Hermitte_street_in_grenoble_%28outside%29.jpg'
META_IMAGE_TYPE = 'image/jpeg'
ABOUT_IMAGE = META_IMAGE
COPYRIGHT = 'Photo du GHM : Jean-Paul Corlin - <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC BY-SA 4.0</a> (<a href="https://commons.wikimedia.org/wiki/File:Dr_Hermitte_street_in_grenoble_(outside).jpg">Wikipédia</a>)'

LINKS = (
    ("Touche pas à ma Mut' - Collectif des usagers des cliniques mutualistes de Grenoble", "https://www.touchepasamamut.fr"),
    ("Association des Amis des Cliniques Mutualistes de Grenoble", "https://amisdescliniquesmutualistesgrenoble.fr/index.php/les-cliniques-vendues/"),
    ("Page Wikipédia du GHM de Grenoble", "https://fr.wikipedia.org/wiki/Groupe_hospitalier_mutualiste_de_Grenoble"),
    ("GHM de Grenoble sur Google Maps", "https://g.page/ghmgrenoble?share"),
    ("Site officiel du GHM de Grenoble", "https://www.ghm-grenoble.fr"),
    ("Sources de ce site web @GitHub", "https://github.com/hopitaux-a-defendre/ghm-grenoble/"),
)

PATH = './content'
OUTPUT_PATH = './output'

MARKDOWN = {'output_format': 'html5'}

PLUGIN_PATHS = ('../pelican-plugins',)
PLUGINS = ('i18n_subsites', 'representative_image')#, 'w3c_validate')
logging.getLogger('i18n_subsites.i18n_subsites').setLevel(logging.DEBUG)
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'

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
