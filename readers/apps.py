from django.apps import AppConfig


class ReadersConfig(AppConfig):
    name = 'readers'
    def ready(self):
        import readers.signals
