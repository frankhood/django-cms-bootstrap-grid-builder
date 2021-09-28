""" cms_plugins
    Created at 09/04/20
"""
import logging

from cms.plugin_pool import plugin_pool
from django.conf import settings

from django.utils.translation import ugettext, ugettext_lazy as _
from .forms import GridPluginForm
from .utils import create_grid_plugins_structure

try:
    from django.forms.util import flatatt
except ImportError:
    from django.forms.utils import flatatt

from cms.plugin_base import CMSPluginBase

from .models import BaseStructurePluginModel, GridContainerPluginModel, GridRowPluginModel, GridColPluginModel

logger = logging.getLogger(__name__)


@plugin_pool.register_plugin
class ConfigurableGridPlugin(CMSPluginBase):
    model = BaseStructurePluginModel
    name = _('Cms Grid')
    render_template = 'configurable_grid/configurable_grid.html'
    allow_children = True
    child_classes = [getattr(settings, "GRID_CONTAINER_PLUGIN", "GridContainerPlugin")]

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

    change_fieldsets = (
        (None, {
            'fields': (
                ('tag_type',),
            )
        }),
    )

    @classmethod
    def get_child_classes(cls, slot, page, instance=None):
        return super().get_child_classes(slot, page, instance)

    def get_fieldsets(self, request, obj=None):
        if obj and obj.id:
            return self.change_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            return GridPluginForm
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        response = super().save_model(request, obj, form, change)
        if not change:
            plugins_map = form.cleaned_data.pop('form_data', {})
            create_grid_plugins_structure(obj, plugins_map)
        return response


class GridContainerPlugin(CMSPluginBase):
    model = GridContainerPluginModel
    name = _("Grid Container")
    render_template = 'configurable_grid/grid_container.html'
    allow_children = True
    child_classes = ["GridRowPlugin"]

    fieldsets = (
        (None, {"fields": (
            ("variant_class", "tag_type"),
        )}),
    )


if not getattr(settings, "GRID_CONTAINER_PLUGIN", None):
    plugin_pool.register_plugin(GridContainerPlugin)


class GridRowPlugin(CMSPluginBase):
    model = GridRowPluginModel
    name = _("Grid Row")
    render_template = 'configurable_grid/grid_row.html'
    allow_children = True
    require_parent = True
    parent_classes = ["GridContainerPlugin"]
    child_classes = ["GridColPlugin"]

    fieldsets = (
        (None, {"fields": (
            ("variant_class",),
        )}),
    )


if not getattr(settings, "GRID_ROW_PLUGIN", None):
    plugin_pool.register_plugin(GridRowPlugin)


class GridColPlugin(CMSPluginBase):
    model = GridColPluginModel
    name = _("Grid Column")
    render_template = 'configurable_grid/grid_column.html'
    allow_children = True
    require_parent = True
    parent_classes = ['GridRowPlugin']

    fieldsets = (
        (None, {"fields": (
            ("cols_xs",),
            ("cols_sm",),
            ("cols_md",),
            ("cols_lg",),
            ("cols_xl",),
        )}),
    )


if not getattr(settings, "GRID_COL_PLUGIN", None):
    plugin_pool.register_plugin(GridColPlugin)
