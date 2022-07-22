from django.apps import AppConfig


class CarSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_system'

    def ready(self):
    	from . import signals