AUTHOR = 'Skenvy'
SITENAME = 'Advent of Code: Explainer'
SITEURL = ""

THEME = './theme' # our custom theme
PATH = "content"
ARTICLE_PATHS = ['articles']
RELATIVE_URLS = False

TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
)

# See https://github.com/getpelican/pelican/wiki/Tips-n-Tricks 

# "Extra" content hooked in
STATIC_PATHS = ["images", "extra/robots.txt", "extra/favicon.ico", "scripts"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"}
}

# default value is ('index', 'tags', 'categories', 'archives')
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
