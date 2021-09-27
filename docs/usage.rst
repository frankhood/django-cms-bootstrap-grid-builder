=====
Usage
=====

To use Django CMS bootstrap grid builder in a project, add it to your `INSTALLED_APPS`:

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
