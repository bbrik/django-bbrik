============
Installation
============

Installing django-bbrik
~~~~~~~~~~~~~~~~~~~~~~~

#. Install using pip::

    pip install git+ssh://git@github.com/bbrik/django-bbrik.git

#. Add ``bbrik`` to your ``INSTALLED_APPS`` in settings.py::

    INSTALLED_APPS = (
        ...
        'bbrik',
    )

Management commands
~~~~~~~~~~~~~~~~~~~

compileless
***********

Install ``node``, ``npm`` and ``less``

Add ``LESS_INPUT_FILE`` to settings.py::

    LESS_INPUT_FILE = '/path/to/project.less'

Output is automatically rendered with the same name with ``.css`` extension in a
``css`` directory in the first entry in ``STATICFILES_DIRS``. For example:
``/static/css/project.css``

You can specify an output using ``CSS_OUTPUT_FILE`` in settings.py::

    CSS_OUTPUT_FILE = '/path/to/project.css'


Tags
~~~~

active and active_start
***********************

Used to style any html as active based on the current request's path.

Add ``django.core.context_processors.request`` to ``TEMPLATE_CONTEXT_PROCESSORS`` in
settings.py

The syntax is the similar as django's ``url`` tag.

For example, with an ``urls.py``::

    ...
    url(
       regex=r'^post/$',
       view=post_home_view,
       name='post_home'
    ),
    url(
       regex=r'^post/detail/(?P<slug>[\w_-]+)/$',
       view=post_detail_view,
       name='post_detail'
    ),

In a template for a site header you could have::

    <li class="{% active_start 'post_home' %}">
      <a href="{% url 'post_home %}">
        Posts
      </a>
    </li>

This will render the ``<li>`` active for any path that starts with ``/post/``.

In a template, on a list of lists to posts::

    <li class="{% active 'post_detail' slug=post.slug %}">
      <a href="{% url 'post_detail' slug=post.slug %}">
        {{ post.title }}
      </a>
    </li>

This will render the ``<li>`` active if the current path is the detail for the post.

You can also provide hard coded urls::

    <li class="{% active_start '/post/' %}">
      <a href="{% url 'post_home %}">
        Posts
      </a>
    </li>

