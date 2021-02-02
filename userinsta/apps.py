from django.apps import AppConfig


class UserinstaConfig(AppConfig):
    name = 'userinsta'

    def ready(self):
        import userinsta.signals
