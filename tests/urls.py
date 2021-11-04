# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from cms.cms_wizards import cms_page_wizard, cms_subpage_wizard
from cms.wizards.wizard_pool import wizard_pool
from django.conf import settings
from django.conf.urls import include, static, url
from django.contrib import admin
from django.urls import re_path

from bootstrap_grid_builder.cms_wizards import cms_wizards

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    re_path(r"^", include("cms.urls")),
]


urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# OVERRIDE CMS WIZARD
wizard_pool.unregister(cms_page_wizard)
wizard_pool.unregister(cms_subpage_wizard)

wizard_pool.register(cms_wizards.cms_page_wizard)
wizard_pool.register(cms_wizards.cms_subpage_wizard)
