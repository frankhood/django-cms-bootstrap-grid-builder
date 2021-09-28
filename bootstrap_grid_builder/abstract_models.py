from cms.models import CMSPlugin
from django.db import models

from django.utils.translation import ugettext_lazy as _

from . import settings as app_settings
from .fields import ColLGClassPrefixField, ColClassPrefixField, ColSMClassPrefixField, ColMDClassPrefixField, \
    ColXLClassPrefixField, ClassGridRowPrefixField


class BaseStructurePluginAbstractModel(CMSPlugin):
    variant_class = models.CharField(
        verbose_name="Variant Class",
        choices=app_settings.BASE_STRUCTURE_VARIANT_CLASSES_CHOICES,
        default=app_settings.BASE_STRUCTURE_VARIANT_CLASSES_CHOICES[0][0],
        max_length=64
    )

    class Meta:
        abstract = True


class GridContainerPluginAbstractModel(CMSPlugin):
    variant_class = models.CharField(
        verbose_name="Variant Class",
        choices=app_settings.VARIANT_GRID_CONTAINER_CLASS_CHOICES,
        max_length=64
    )

    tag_type = models.CharField(
        verbose_name="Tag Type",
        choices=app_settings.TAG_TYPE_GRID_CONTAINER_CLASS_CHOICES,
        max_length=64,
        blank=True,
        default=""
    )

    class Meta:
        abstract = True


COL_CHOICES = [(str(x), str(x)) for x in range(1, 13)]
COL_CHOICES += (
    ("auto", _("Auto")),
    (None, _("No Definition")),
)
DEFAULT_COL_CHOICE = ('12', '12')


class GridColPluginAbstractModel(CMSPlugin):
    cols = ColClassPrefixField(
        verbose_name="Base column Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_("Default")
    )

    cols_sm = ColSMClassPrefixField(
        verbose_name="Column sm Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 576px")
    )

    cols_md = ColMDClassPrefixField(
        verbose_name="Column md Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 768px")
    )

    cols_lg = ColLGClassPrefixField(
        verbose_name="Column lg Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 992px")
    )

    cols_xl = ColXLClassPrefixField(
        verbose_name="Column xl Class",
        choices=COL_CHOICES,
        max_length=64,
        null=True,
        default="12",
        help_text=_(">= 1200px")
    )

    class Meta:
        abstract = True


class GridRowPluginAbstractModel(CMSPlugin):
    variant_class = ClassGridRowPrefixField(
        verbose_name="Variant Class",
        choices=app_settings.VARIANT_GRID_ROW_CLASSES_CHOICES,
        max_length=64,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
