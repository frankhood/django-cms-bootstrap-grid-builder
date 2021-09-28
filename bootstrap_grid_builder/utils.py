""" utils
    Created at 24/04/20
"""
import logging
import json

from cms.plugin_pool import plugin_pool
from django.apps import apps
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


from .models import BaseStructurePluginModel, GridContainerPluginModel, GridRowPluginModel, GridColPluginModel

logger = logging.getLogger(__name__)


def create_grid_plugins_structure(parent_plugin, plugins_map):
    containers = []
    import ast
    plugins_map = ast.literal_eval(plugins_map)
    for container_data in plugins_map.get('containers', []):
        container_attrs = container_data.get('attrs', {})
        container_plugin_model = apps.get_model(
            getattr(settings, "GRID_CONTAINER_PLUGIN_MODEL", "bootstrap_grid_builder.GridContainerPluginModel")
        )
        container_plugin = plugin_pool.get_plugin(getattr(settings, "GRID_CONTAINER_PLUGIN", "GridContainerPlugin"))
        container_obj = container_plugin_model.objects.create(
            parent=parent_plugin, placeholder=parent_plugin.placeholder, language=parent_plugin.language,
            variant_class=container_attrs.get("variant_class", ""),
            plugin_type=container_plugin.__name__
        )
        for row_data in container_data.get('rows', []):
            row_attrs = row_data.get('attrs', {})
            row_plugin_model = apps.get_model(
                getattr(settings, "GRID_ROW_PLUGIN_MODEL", "bootstrap_grid_builder.GridRowPluginModel")
            )
            row_plugin = plugin_pool.get_plugin(getattr(settings, "GRID_ROW_PLUGIN", "GridRowPlugin"))
            row_obj = row_plugin_model.objects.create(
                parent=container_obj, placeholder=container_obj.placeholder, language=container_obj.language,
                variant_class=row_attrs.get("variant_class", ""),
                plugin_type=row_plugin.__name__
            )
            for col_data in row_data.get('cols', {}):
                col_attrs = col_data.get('attrs', {})
                col_plugin_model = apps.get_model(
                    getattr(settings, "GRID_COL_PLUGIN_MODEL", "bootstrap_grid_builder.GridColPluginModel")
                )
                col_plugin = plugin_pool.get_plugin(getattr(settings, "GRID_COL_PLUGIN", "GridColPlugin"))
                col_plugin_model.objects.create(
                    parent=row_obj, placeholder=row_obj.placeholder,
                    language=container_obj.language,
                    cols_xs=col_attrs.get("cols_xs", ""),
                    cols_sm=col_attrs.get("cols_sm", ""),
                    cols_md=col_attrs.get("cols_md", ""),
                    cols_lg=col_attrs.get("cols_lg", ""),
                    cols_xl=col_attrs.get("cols_xl", ""),
                    plugin_type=col_plugin.__name__
                )
        containers.append(container_obj)
    return containers
