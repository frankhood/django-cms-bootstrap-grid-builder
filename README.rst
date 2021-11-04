=============================
Django Cms Bootstrap Grid Builder
=============================

.. image:: https://badge.fury.io/py/django-cms-bootstrap-grid-builder.svg/?style=flat-square
    :target: https://badge.fury.io/py/django-cms-bootstrap-grid-builder

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square
    :target: https://django-cms-bootstrap-grid-builder.readthedocs.io/en/latest/

.. image:: https://img.shields.io/coveralls/github/frankhood/django-cms-bootstrap-grid-builder/main?style=flat-square
    :target: https://coveralls.io/github/frankhood/django-cms-bootstrap-grid-builder?branch=main
    :alt: Coverage Status

Documentation
=============

The full documentation is at https://django-cms-bootstrap-grid-builder.readthedocs.io.

Quickstart
----------

:warning: ATTENTION !!! This package requires **django-cms** integration


Install Django CMS bootstrap grid builder::

    pip install django-cms-bootstrap-grid-builder

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'bootstrap_grid_builder',
        ...
    )

If you want to use bootstrap_grid_builder by defaults you need to specify only
default plugin structure placeholder in your settings.py.

.. code-block:: python

    GRID_PLUGIN_STRUCTURE_PLACEHOLDER = "grid_placeholder"


And add this placeholder in your home.html like this:

.. code-block:: html

    {% load cms_tags sekizai_tags %}
    <html>
        <head>
            <title>{% page_attribute "page_title" %}</title>
            {% render_block "css" %}
        </head>
        <body>
            {% cms_toolbar %}
            {% placeholder "grid_placeholder" %}
            {% render_block "js" %}
        </body>
    </html>


Then run migrate to apply package migrations:

::

    $ python manage.py migrate


When the user create the page all the structure will be insert in this placeholder

HowTo customize Grid Plugins & Grid Plugin Models
-------------------------------------------------

You can override actual grid plugins.


Override GridContainerPlugin and unregister it.


.. code-block:: python

    # your_app/cms_plugins.py

    plugin_pool.unregister_plugin(GridContainerPlugin)

    @plugin_pool.register_plugin
    class MyCustomGridContainerPlugin(GridContainerPlugin):
        model = MyCustomGridContainerPluginModel
        module = _("Custom")
        name = _("Custom Grid Container")
        render_template = '...'

        fieldsets = (
            (None, {"fields": (
                ...
                ("variant_class",),
                ...
            )}),
        )


Repeat this action for all yours custom plugins.


And setting up this variable in your settings.py

.. code-block:: python

    GRID_CONTAINER_PLUGIN = "MyCustomGridContainerPlugin"


Repeat this action for all your custom plugins and setting up variables:

.. code-block:: python

    GRID_CONTAINER_PLUGIN = "MyCustomGridContainerPlugin"
    GRID_COL_PLUGIN = "MyCustomGridColPlugin"
    GRID_ROW_PLUGIN = "MyCustomGridRowPlugin"


It is necessary to do more or less the same thing for the models.


Override GridContainerPluginAbstractModel and create your model:

.. code-block:: python

    # your_app/models.py

    class MyCustomGridContainerPluginModel(GridContainerPluginAbstractModel):

    class Meta:
        verbose_name = _("My Custom grid container plugin")
        verbose_name_plural = _("My Custom grid container plugins")


Repeat this action for all yours custom plugin models.

And setting up this variable in your settings.py

.. code-block:: python

    GRID_CONTAINER_PLUGIN_MODEL = "your_app.MyCustomGridContainerPluginModel"

Repeat this action for all your custom plugin models and setting up variables:

.. code-block:: python

    GRID_CONTAINER_PLUGIN_MODEL = "your_app.MyCustomGridContainerPluginModel"
    GRID_COL_PLUGIN_MODEL = "your_app.MyCustomGridColPluginModel"
    GRID_ROW_PLUGIN_MODEL = "your_app.MyCustomGridRowPluginModel"


After model creation run makemigration & migrate to create yours models in database

::

    $ python manage.py makemigrations
    $ python manage.py migrate


Running Tests
-------------

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    # Back-end
    $ pip install -r requirements_dev.txt
    $ pre-commit install
    $ python manage.py migrate
    $ python manage.py runserver




Frontend
========
This is a Vue.js application for creating custom bootstrap grids throughout an intuitive interface and draggable elements

Browser Compatibility
---------------------
The page-layout-builder component is compatible with modern browsers such as Chrome, Firefox, Safari, Opera, and Edge. It also supports Internet Explorer 11 but with limited performance.


Frontend source folder ascii tree
---------------------------------

::

  /django-cms-bootstrap-grid-builder/src
  ├─ main.js  //Entrypoint for build
  ├─ index.js  //Entrypoint for development
  ├─ components
  │  ├─ CustomDragElement.vue
  │  ├─ page-layout-builder.vue
  │  ├─ GridItem.vue
  │  ├─ GridLayout.vue
  │  └─ index.js
  └─ helpers
     ├─ DOM.js
     ├─ draggableUtils.js
     ├─ responsiveUtils.js
     └─ utils.js


How it works
---------------------------------
The informations obtained from the interface configuration are serialized into a JSON object and sent to the backend wich replicates the desired grid structure with Django plugins templates


Development commands
---------------------

::

    # Front-end
    $ npm i -g yarn rimraf @vue/cliz
    $ yarn install
    $ yarn serve (for development, lauches local live reloading server)
    $ yarn build (for production build, creates dist at django-cms-bootstrap-grid-builder/bootstrap_grid_builder/static/cms_plugin_structure/dist)


Credits
-------

Tools used in rendering this package:

*  `Cookiecutter <https://github.com/audreyr/cookiecutter/>`_
*  `cookiecutter-djangopackage <https://github.com/pydanny/cookiecutter-djangopackage/>`_
*  `element-resize-detector <https://github.com/wnr/element-resize-detector/>`_
*  `interactjs <https://interactjs.io/>`_
*  `vue-drag-drop <https://github.com/cameronhimself/vue-drag-drop/>`_
*  `google-palette <https://github.com/google/palette.js/tree/master/>`_
*  `bootstrap <https://github.com/twbs/bootstrap/>`_
