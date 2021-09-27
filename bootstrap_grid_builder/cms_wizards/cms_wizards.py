""" cms_wizards.py
    Created at 24/04/20
"""
import logging

from cms.models import Page
from cms.cms_wizards import (CMSPageWizard, CMSSubPageWizard)

from django.utils.translation import ugettext, ugettext_lazy as _
from .forms import CreateCMSPageForm, CreateCMSSubPageForm

logger = logging.getLogger(__name__)

cms_page_wizard = CMSPageWizard(
    title=_(u"New page"),
    weight=100,
    form=CreateCMSPageForm,
    model=Page,
    description=_(u"Create a new page next to the current page.")
)

cms_subpage_wizard = CMSSubPageWizard(
    title=_(u"New sub page"),
    weight=110,
    form=CreateCMSSubPageForm,
    model=Page,
    description=_(u"Create a page below the current page.")
)

