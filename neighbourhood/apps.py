from django.apps import AppConfig


class NeighborhoodConfig(AppConfig):
    name = 'neighbourhood'

    def ready(self):
        import neighbourhood.signals
