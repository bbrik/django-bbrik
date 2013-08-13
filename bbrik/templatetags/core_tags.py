# -*- coding: utf-8 -*-

from django.template import Library
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured


register = Library()


def get_request(context):
    try:
        return context['request']
    except KeyError:
        error_msg = (u'Request not found in context. '
                     u'Add "django.core.context_processors.request" to your TEMPLATE_CONTEXT_PROCESSORS')
        raise ImproperlyConfigured(error_msg)


@register.simple_tag(takes_context=True)
def active(context, viewname, *args, **kwargs):
    """
    Usage is similar to django's url tag, but it doesn't return a url,
    it returns the string "active" if the specified view and arguments
    reverses to the path for the current request.

    """
    request = get_request(context)
    url = reverse(viewname, args=args, kwargs=kwargs)
    return 'active' if request.path == url else ''


@register.simple_tag(takes_context=True)
def active_start(context, viewname, *args, **kwargs):
    """
    Usage is similar to django's url tag, but it doesn't return a url,
    it returns the string "active" if the specified view and arguments
    reverses to a path that is the start of the path for the current request.

    """
    request = get_request(context)
    url = reverse(viewname, args=args, kwargs=kwargs)
    return 'active' if request.path.startswith(url) else ''
