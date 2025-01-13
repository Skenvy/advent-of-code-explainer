################################################################################
# GENERAL
AUTHOR = 'Skenvy'
SITENAME = 'Advent of Code: Explainer'
SITEURL = "" # set in publishconf

TIMEZONE = 'UTC'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = 'en'

RELATIVE_URLS = False

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/Skenvy"),
    ("PyPI", "https://pypi.org/user/Skenvy/"),
    ("LinkedIn", "https://www.linkedin.com/in/nathan-levett/"),
)

################################################################################
# THEME
THEME = './theme' # our basic custom pyscript enabling theme
README_ARTICLE_URL = 'https://skenvy.github.io/advent-of-code-explainer/web/articles/9999-12-31-readme/'
PELICAN_THEME_SOURCE_URL = 'https://github.com/Skenvy/advent-of-code-explainer/tree/main/web/theme'

################################################################################
# CONTENT
PATH = 'content'
ARTICLE_PATHS = ['articles']

# "Extra" content hooked in
STATIC_PATHS = ["images", "scripts", "tests", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/version.html": {"path": "version.html"},
}

# default value is ('index', 'tags', 'categories', 'archives')
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

################################################################################
# OUTPUT
OUTPUT_PATH = 'output'
ARTICLE_URL = 'articles/{date:%Y-%m-%d}-{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

DEFAULT_PAGINATION = 5

################################################################################
# FEED
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
