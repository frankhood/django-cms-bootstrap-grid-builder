# -*- coding: utf-8
from django.apps import AppConfig


class BootstrapGridBuilderConfig(AppConfig):
    name = 'bootstrap_grid_builder'

    def ready(self):
        super().ready()
        from . import receivers