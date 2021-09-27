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
    ]:
        importlib.reload(app_settings)
