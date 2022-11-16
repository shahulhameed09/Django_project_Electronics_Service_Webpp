from django.apps import AppConfig


class ElectroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'electro'

    def ready(self):
        import electro.signals
