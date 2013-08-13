============
Installation
============

Installing django-bbrik
~~~~~~~~~~~~~~~~~~~~~~~

Install latest stable version into your python path using pip or easy_install::

    pip install git+ssh://git@github.com/bbrik/django-accounts.git

Add ``bbrik`` to your ``INSTALLED_APPS`` in settings.py::

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

