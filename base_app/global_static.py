#!/usr/bin/python
from django.conf import settings
import os, os.path, time, glob

# get the site time code. we just use the start time of the server as the code.
# this is used to force browser caches to update once per server restart.
SERVER_START_MINUTE = int(time.time() / 60) # minutes since Jan 1, 1970

SITE_WIDE_CSS_ITEMS = []
SITE_WIDE_JS_ITEMS = []

# css
for filepath in sorted(glob.glob(os.path.join(settings.BASE_DIR, 'base_app/styles/global/*.css'))):
	if not os.path.split(filepath)[1].startswith('__'):
		fileurl = os.path.join(settings.STATIC_URL, 'base_app/styles/global', os.path.split(filepath)[1])
		SITE_WIDE_CSS_ITEMS.append('<link rel="stylesheet" type="text/css" href="%s?%i" />' % (fileurl, SERVER_START_MINUTE))
# js
for filepath in sorted(glob.glob(os.path.join(settings.BASE_DIR, 'base_app/scripts/global/*.js'))):
	if not os.path.split(filepath)[1].startswith('__'):
		fileurl = os.path.join(settings.STATIC_URL, 'base_app', 'scripts', 'global', os.path.split(filepath)[1])
		SITE_WIDE_JS_ITEMS.append('<script src="%s?%i"></script>' % (fileurl, SERVER_START_MINUTE))

# combine into a single string that can be included verbatim into all pages
SITE_WIDE_CSS = '\n'.join(SITE_WIDE_CSS_ITEMS)
SITE_WIDE_JS = '\n'.join(SITE_WIDE_JS_ITEMS)