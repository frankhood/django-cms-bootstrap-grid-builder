from cms import models
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.db import models


class ExamplePluginModel(CMSPlugin):
    content = models.TextField("Content", default="", blank=True)    

    class Meta(CMSPlugin.Meta):

        verbose_name = "Example Plugin Model"
        verbose_name_plural = "Example Plugin Models"

    def __str__(self) -> str:
        return super().__str__()
        

@plugin_pool.register_plugin
class ExamplePlugin(CMSPluginBase):

    model = ExamplePluginModel
    module = "Example"
    name = "Example Plugin Title"
    render_template = 'cms_plugins/example_content.html'

    fieldsets = (
        ("Example Content", {"fields": (
            ("content",),
        )}),
    )
