=============================
Django CMS bootstrap grid builder
=============================

.. image:: https://badge.fury.io/py/django-cms-bootstrap-grid-builder.svg
    :target: https://badge.fury.io/py/django-cms-bootstrap-grid-builder

.. image:: https://travis-ci.org/frankhood/django-cms-bootstrap-grid-builder.svg?branch=master
    :target: https://travis-ci.org/frankhood/django-cms-bootstrap-grid-builder

.. image:: https://codecov.io/gh/frankhood/django-cms-bootstrap-grid-builder/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/frankhood/django-cms-bootstrap-grid-builder

Your project description goes here

Documentation
-------------

The full documentation is at https://django-cms-bootstrap-grid-builder.readthedocs.io.

Quickstart
----------

Install Django CMS bootstrap grid builder::

    pip install django-cms-bootstrap-grid-builder

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'bootstrap_grid_builder.apps.BootstrapGridBuilderConfig',
        ...
    )

Add Django CMS bootstrap grid builder's URL patterns:

.. code-block:: python

    from bootstrap_grid_builder import urls as bootstrap_grid_builder_urls


    urlpatterns = [
        ...
        url(r'^', include(bootstrap_grid_builder_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
