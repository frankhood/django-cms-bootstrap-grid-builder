# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.urls import re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path(r'^', include('cms.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# OVERRIDE CMS WIZARD
from cms.cms_wizards import (
    cms_page_wizard as django_cms_page_wizard,
    cms_subpage_wizard as django_cms_subpage_wizard
)
from cms.wizards.wizard_pool import wizard_pool
from bootstrap_grid_builder.cms_wizards.cms_wizards import cms_page_wizard, cms_subpage_wizard

wizard_pool.unregister(django_cms_page_wizard)
wizard_pool.unregister(django_cms_subpage_wizard)

wizard_pool.register(cms_page_wizard)
wizard_pool.register(cms_subpage_wizard)