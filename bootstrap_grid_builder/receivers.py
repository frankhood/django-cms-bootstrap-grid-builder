import importlib

from django.core.signals import setting_changed
from django.dispatch import receiver
from . import settings as app_settings

"""
Update of settings
"""
@receiver(setting_changed)
def app_settings_reload_handler(**kwargs):
    if kwargs['setting'] in [
        'GRID_CONTAINER_PLUGIN', 'GRID_CONTAINER_PLUGIN_MODEL',
        'GRID_COL_PLUGIN', 'GRID_COL_PLUGIN_MODEL',
        'GRID_ROW_PLUGIN', 'GRID_ROW_PLUGIN_MODEL',
        "BASE_STRUCTURE_TAG_TYPE_DIV",
        "BASE_STRUCTURE_TAG_TYPE_ARTICLE",
        "BASE_STRUCTURE_TAG_TYPE_SECTION",
        "BASE_STRUCTURE_TAG_TYPE_HEADER",
        "BASE_STRUCTURE_TAG_TYPE_FOOTER",
        "BASE_STRUCTURE_TAG_TYPE_ASIDE",
        "VARIANT_GRID_CONTAINER_CLASS_NO_CONTAINER",
        "VARIANT_GRID_CONTAINER_CLASS_BOXED",
        "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_SM",
        "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_MD",
        "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_LG",
        "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_XL",
        "VARIANT_GRID_CONTAINER_CLASS_TOTALLY_FLUID",
        "TAG_TYPE_GRID_CONTAINER_SECTION",
        "TAG_TYPE_GRID_CONTAINER_DIV",
        "VARIANT_GRID_ROW_CLASS_LEFT",
        "VARIANT_GRID_ROW_CLASS_CENTER",
        "VARIANT_GRID_ROW_CLASS_RIGHT",
        "VARIANT_GRID_ROW_CLASS_AROUND",
        "VARIANT_GRID_ROW_CLASS_BETWEEN",
    ]:
        importlib.reload(app_settings)
