from django.apps import AppConfig
from health_check.plugins import plugin_dir


class HealthcheckConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "healthcheck"

    def ready(self):
        from .views import AzureBlobHealthCheck, AzureFrontDoorHealthCheck, JiraFilterHealthCheckView

        plugin_dir.register(JiraFilterHealthCheckView)
        plugin_dir.register(AzureBlobHealthCheck)
        plugin_dir.register(AzureFrontDoorHealthCheck)
