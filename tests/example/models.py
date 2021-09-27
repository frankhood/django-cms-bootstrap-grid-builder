""" models
    Created at 24/04/20
"""
import logging

from django.utils.translation import ugettext_lazy as _

from bootstrap_grid_builder.models import BaseStructurePluginAbstractModel, GridContainerPluginAbstractModel, GridRowPluginAbstractModel, GridColPluginAbstractModel

logger = logging.getLogger(__name__)


class BaseStructurePluginModel(BaseStructurePluginAbstractModel):

    class Meta:
        verbose_name = _("Base Structure Plugin")
        verbose_name_plural = _("Base Structure Plugins")


class GridContainerPluginModel(GridContainerPluginAbstractModel):

    class Meta:
        verbose_name = _("Grid Container Plugin")
        verbose_name_plural = _("Grid Container Plugins")


class GridColPluginModel(GridColPluginAbstractModel):

    class Meta:
        verbose_name = _("Grid Column Plugin")
        verbose_name_plural = _("Grid Column Plugins")


class GridRowPluginModel(GridRowPluginAbstractModel):

    class Meta:
        verbose_name = _("Grid Row Plugin")
        verbose_name_plural = _("Grid Roe Plugins")
