""" forms
    Created at 24/04/20
"""
import logging

from cms.admin.forms import AddPageForm
from django.conf import settings

from django.db import transaction

from cms.plugin_pool import plugin_pool
from cms.utils import permissions
from cms.utils.conf import get_cms_setting

from cms.forms.wizards import CreateCMSPageForm as DjangoCMSCreateCMSPageForm

from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms
from ..forms import GridBuilderField
from ..utils import create_grid_plugins_structure

logger = logging.getLogger(__name__)


class CreateCMSPageForm(DjangoCMSCreateCMSPageForm):
    content = None
    form_data = GridBuilderField(
        required=True,
        label='',
    )
    data_dumper = forms.CharField(
        widget=forms.Textarea(
          attrs={
            'style': 'display:none',
            'id': 'json-data',
          }
        ),
        required=False,
        label='',
    )

    class Media:
        js = (
            'cms_plugin_structure/page.js',
            # getattr(settings, "JSON_EDITOR_JS", 'jsoneditor/jsoneditor.js'),
        )
        css = {
            'all': (
                # getattr(settings, "JSON_EDITOR_CSS", 'jsoneditor/jsoneditor.css'),
                'cms_plugin_structure/page.css',
            )
        }

    # def __init__(self, *args, **kwargs):
    #     super(CreateCMSPageForm, self).__init__(*args, **kwargs)
    #     #self.fields['content'].widget = forms.Textarea()
    #     self.fields.pop('content',None)

    @transaction.atomic
    def save(self, **kwargs):
        from cms.api import add_plugin

        new_page = AddPageForm.save(self, **kwargs)

        if self.cleaned_data.get("page_type"):
            return new_page

        parent_node = self.cleaned_data.get('parent_node')

        if parent_node and new_page.parent_page.is_page_type:
            # the new page was created under a page-type page
            # set the new page as a page-type too
            new_page.update(
                draft_only=True,
                is_page_type=True,
                in_navigation=False,
            )

        # If the user provided content, then use that instead.
        content = self.cleaned_data.get('content',None)
        plugin_type = get_cms_setting('PAGE_WIZARD_CONTENT_PLUGIN')
        plugin_body = get_cms_setting('PAGE_WIZARD_CONTENT_PLUGIN_BODY')
        slot = get_cms_setting('PAGE_WIZARD_CONTENT_PLACEHOLDER')

        if plugin_type in plugin_pool.plugins and plugin_body:
            if content and permissions.has_plugin_permission(
                    self.user, plugin_type, "add"):
                new_page.rescan_placeholders()
                placeholder = self.get_placeholder(new_page, slot=slot)
                if placeholder:
                    opts = {
                        'placeholder': placeholder,
                        'plugin_type': plugin_type,
                        'language': self.language_code,
                        plugin_body: content,
                    }
                    add_plugin(**opts)

        json_data = self.cleaned_data.get('form_data')
        plugin_type = 'ConfigurableGridPlugin'

        if plugin_type in plugin_pool.plugins:
            if json_data and permissions.has_plugin_permission(
                    self.user, plugin_type, "add"):
                new_page.rescan_placeholders()
                placeholder = self.get_placeholder(new_page, slot=getattr(settings, "GRID_PLUGIN_STRUCTURE_PLACEHOLDER", None))
                if placeholder:
                    opts = {
                        'placeholder': placeholder,
                        'plugin_type': plugin_type,
                        'language': self.language_code,
                    }
                    plugin = add_plugin(**opts)
                    create_grid_plugins_structure(plugin, json_data)
        return new_page


class CreateCMSSubPageForm(CreateCMSPageForm):
    sub_page_form = True
