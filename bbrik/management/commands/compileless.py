# -*- coding: utf-8 -*-

from subprocess import call
import errno
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured

from ..base import LESS_INPUT_FILE, CSS_OUTPUT_FILE


class Command(BaseCommand):
    help = 'Compiles less into css'
    option_list = BaseCommand.option_list + (
        make_option('-c', '--compress', action='store_true', dest='compress',
                    default=False, help='minify output'),
    )

    def handle(self, *args, **options):
        CSS_OUTPUT_FILE.ancestor(1).mkdir()

        try:
            if options['compress']:
                call(['lessc', '--yui-compress', LESS_INPUT_FILE, CSS_OUTPUT_FILE])
            else:
                call(['lessc', LESS_INPUT_FILE, CSS_OUTPUT_FILE])
        except OSError as e:
            if e.errno == errno.ENOENT:
                error_msg = "lessc not found. install node, npm and less"
                raise ImproperlyConfigured(error_msg)
            else:
                raise
