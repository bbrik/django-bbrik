# -*- coding: utf-8 -*-

from django.template import Library
from django.shortcuts import resolve_url
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
def replace_in_query(context, **kwargs):
    """
    Returns the current request's GET replacing the query parameters with
    the values specified on the kwargs encoded as url query string.
    Leaves all other paramenters unchanged.

    """
    request = get_request(context)
    query = request.GET.copy()
    for k,v in kwargs.items():
        query[k] = unicode(v)
    return query.urlencode()


@register.simple_tag(takes_context=True)
def active_query(context, **kwargs):
    """
    Returns the string "active" if the specified kwargs are found in the
    request's GET.

    """
    request = get_request(context)
    query_in_get = [request.GET.get(k) == unicode(v) for k,v in kwargs.items()]
    return 'active' if all(query_in_get) else ''


@register.simple_tag(takes_context=True)
def active(context, viewname, *args, **kwargs):
    """
    Usage is similar to django's url tag, but it doesn't return a url,
    it returns the string "active" if the specified view and arguments
    reverses to the path for the current request.

    """
    request = get_request(context)
    url = resolve_url(viewname, *args, **kwargs)
    return 'active' if request.path == url else ''


@register.simple_tag(takes_context=True)
def active_start(context, viewname, *args, **kwargs):
    """
    Usage is similar to django's url tag, but it doesn't return a url,
    it returns the string "active" if the specified view and arguments
    reverses to a path that is the start of the path for the current request.

    """
    request = get_request(context)
    url = resolve_url(viewname, *args, **kwargs)
    return 'active' if request.path.startswith(url) else ''
