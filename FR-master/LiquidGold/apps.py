from django.apps import AppConfig


class LiquidgoldConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LiquidGold'

    
    def ready(self):
        import LiquidGold.signals