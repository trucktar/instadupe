from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'instadupe.app'

    def ready(self):
        from instadupe.app import signals
