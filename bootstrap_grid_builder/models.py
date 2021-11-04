# -*- coding: utf-8 -*-
from typing import List, Optional, Tuple

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import fields
from . import settings as app_settings

COL_CHOICES: List[Tuple[Optional[str], str]] = [(str(x), str(x)) for x in range(1, 13)]
COL_CHOICES += [
    ("auto", _("Auto")),
    (None, _("No Definition")),
]
DEFAULT_COL_CHOICE = ("12", "12")


class BaseStructurePluginAbstractModel(CMSPlugin):
    tag_type = models.CharField(
        verbose_name="Tag Type",
        choices=app_settings.BASE_STRUCTURE_TAG_TYPES_CHOICES,
        default=app_settings.BASE_STRUCTURE_TAG_TYPES_CHOICES[0][0],
        max_length=64,
    )

    class Meta:
        """BaseStructurePluginAbstractModel Meta."""

        abstract = True


class GridContainerPluginAbstractModel(CMSPlugin):
    variant_class = models.CharField(
        verbose_name="Variant Class",
        choices=app_settings.VARIANT_GRID_CONTAINER_CLASS_CHOICES,
        max_length=64,
    )

    tag_type = models.CharField(
        verbose_name="Tag Type",
        choices=app_settings.TAG_TYPE_GRID_CONTAINER_CLASS_CHOICES,
        default=app_settings.TAG_TYPE_GRID_CONTAINER_DIV,
        max_length=64,
        blank=True,
    )

    class Meta:
        """GridContainerPluginAbstractModel Meta."""

        abstract = True


class GridColPluginAbstractModel(CMSPlugin):
    cols_xs = fields.ColClassPrefixField(
        verbose_name="Base column Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_("Default"),
    )

    cols_sm = fields.ColSMClassPrefixField(
        verbose_name="Column sm Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 576px"),
    )

    cols_md = fields.ColMDClassPrefixField(
        verbose_name="Column md Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 768px"),
    )

    cols_lg = fields.ColLGClassPrefixField(
        verbose_name="Column lg Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 992px"),
    )

    cols_xl = fields.ColXLClassPrefixField(
        verbose_name="Column xl Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 1200px"),
    )

    class Meta:
        """GridColPluginAbstractModel Meta."""

        abstract = True


class GridRowPluginAbstractModel(CMSPlugin):
    variant_class = fields.ClassGridRowPrefixField(
        verbose_name="Variant Class",
        choices=app_settings.VARIANT_GRID_ROW_CLASSES_CHOICES,
        max_length=64,
        null=True,
        blank=True,
    )

    class Meta:
        """GridRowPluginAbstractModel Meta."""

        abstract = True


class BaseStructurePluginModel(BaseStructurePluginAbstractModel):
    class Meta:
        """BaseStructurePluginModel Meta."""

        verbose_name = _("Base Structure Plugin")
        verbose_name_plural = _("Base Structure Plugins")


class GridContainerPluginModel(GridContainerPluginAbstractModel):
    class Meta:
        """GridContainerPluginModel Meta."""

        verbose_name = _("Grid Container Plugin")
        verbose_name_plural = _("Grid Container Plugins")


class GridColPluginModel(GridColPluginAbstractModel):
    class Meta:
        """GridColPluginModel Meta."""

        verbose_name = _("Grid Column Plugin")
        verbose_name_plural = _("Grid Column Plugins")


class GridRowPluginModel(GridRowPluginAbstractModel):
    class Meta:
        """GridRowPluginModel Meta."""

        verbose_name = _("Grid Row Plugin")
        verbose_name_plural = _("Grid Row Plugins")
