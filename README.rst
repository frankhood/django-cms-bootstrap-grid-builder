=================================
Django CMS bootstrap grid builder
=================================

.. image:: https://badge.fury.io/py/django-cms-bootstrap-grid-builder.svg
    :target: https://badge.fury.io/py/django-cms-bootstrap-grid-builder

.. image:: https://travis-ci.org/frankhood/django-cms-bootstrap-grid-builder.svg?branch=master
    :target: https://travis-ci.org/frankhood/django-cms-bootstrap-grid-builder

.. image:: https://codecov.io/gh/frankhood/django-cms-bootstrap-grid-builder/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/frankhood/django-cms-bootstrap-grid-builder


Documentation
-------------

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


Frontend with VUE.js Development guide
--------------------------------------

::

    at this path are located all the vue files of the project:
    django-cms-bootstrap-grid-builder/src

    once built, the dist wil be located at:
    django-cms-bootstrap-grid-builder/bootstrap_grid_builder/static/cms_plugin_structure/dist


JSON Serialization
--------------------------------------

::

    the serialization logic that produces the final JSON
    is implemented into the file:
    django-cms-bootstrap-grid-builder/src/page-layout-builder.vue



Grid elements templates
--------------------------------------

::

    the templates for each layout element are stored at the following path:
    django-cms-bootstrap-grid-builder/bootstrap_grid_builder/templates/configurable_grid



visible debug elements
--------------------------------------

::

    once the grid is created all the elements are empty, and so not visible.
    to have faster debug sessions, and a visible feedback, change temporarily
    the template files adding styles accordigly.
    it might be usefult to remove the 'template' tags in order to force the child plugin rendering.

    below theres an example of debug styles applied to templates

    configurable_grid.html
    style="display: block;position: absolute;padding: 10px;border: 1px solid black; background-color: rgba(150,150,150,0.2);min-height: 100px;"

    grid_column.html
    style="display: inline-block;position: relative;padding: 10px;border: 1px solid black; background-color: rgba(150,150,150,0.2);min-height: 100px;"

    grid_container.html
    style="display: block;position: relative;padding: 10px;border: 1px solid black; background-color: rgba(150,150,150,0.2);min-height: 100px;"

    grid_row.html
    style="display: block;position: relative;padding: 10px;border: 1px solid black; background-color: rgba(150,150,150,0.2);min-height: 100px;"


Running Tests
-------------

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    python manage.py migrate
    python manage.py runserver

    yarn install
    yarn build (dist is at django-cms-bootstrap-grid-builder/bootstrap_grid_builder/static/cms_plugin_structure/dist)



    


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
