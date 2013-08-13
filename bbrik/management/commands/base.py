# -*- coding: utf-8 -*-

from unipath import Path

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


try:
    LESS_INPUT_FILE = Path(settings.LESS_INPUT_FILE)
except AttributeError:
    msg = "Define LESS_INPUT_FILE = 'path/to/project.less' in settings"
    raise ImproperlyConfigured(msg)


if settings.STATICFILES_DIRS:
    output_path = settings.STATICFILES_DIRS[0].child('css')
    output_file_default = Path(output_path, LESS_INPUT_FILE.stem + '.css')
else:
    output_file_default = None

CSS_OUTPUT_FILE = getattr(settings, 'CSS_OUTPUT_FILE', output_file_default)

if CSS_OUTPUT_FILE is None:
    msg = ("Define CSS_OUTPUT_FILE = 'path/to/project.css' in settings or "
           "set at least one entry in STATICFILES_DIRS")
    raise ImproperlyConfigured(msg)
