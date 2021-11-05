import json
import logging

import django
from django import forms
from django.forms.widgets import Textarea
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from packaging import version

from .models import BaseStructurePluginModel

try:
    from django.forms.util import flatatt
except ImportError:
    from django.forms.utils import flatatt

logger = logging.getLogger(__name__)

basestring = (str, bytes)


class GridBuilderWidget(Textarea):
    class Media:
        """GridBuilderWidget Media."""

        js = (
            "cms_plugin_structure/dist/js/app.js",
            # getattr(settings, "JSON_EDITOR_JS", 'jsoneditor/jsoneditor.js'),
        )
        css = {
            "all": (
                # getattr(settings, "JSON_EDITOR_CSS", 'jsoneditor/jsoneditor.css'),
                # 'cms_plugin_structure/dist/app.css',
            )
        }

    def render(self, name, value, attrs=None, renderer=None):
        if not isinstance(value, basestring):
            value = json.dumps(value)
        input_attrs = {"hidden": True}
        input_attrs.update(attrs)
        if "class" not in input_attrs:
            input_attrs["class"] = "for_jsoneditor"
        else:
            input_attrs["class"] += " for_jsoneditor"
        r = super().render(name, value, input_attrs)
        div_attrs = {}
        div_attrs.update(attrs)
        div_attrs.update({"id": (attrs["id"] + "_jsoneditor")})
        if version.parse(django.get_version()) >= version.parse("1.11"):
            final_attrs = self.build_attrs(div_attrs, extra_attrs={"name": name})
        else:
            final_attrs = self.build_attrs(div_attrs, name=name)
        """ r += '''
        <div %(attrs)s></div>
        ''' % {
            'attrs': flatatt(final_attrs),
        } """
        # devo inviare un form con un input form_data con dentro il json
        context = {"attrs": flatatt(final_attrs)}
        template = get_template("cms_plugin_structure/widgets/grid_builder.html")
        content = template.render(context)
        r += content

        return mark_safe(r)


class GridBuilderField(forms.CharField):
    widget = GridBuilderWidget


class GridPluginForm(forms.ModelForm):
    form_data = GridBuilderField(label="")

    class Meta:
        """GridPluginForm Meta."""

        model = BaseStructurePluginModel
        fields = ("form_data",)
