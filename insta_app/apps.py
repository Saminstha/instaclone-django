from django.apps import AppConfig


class InstaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insta_app'

    def ready(self):
        import insta_app.signals
