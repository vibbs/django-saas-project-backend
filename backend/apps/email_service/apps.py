from django.apps import AppConfig


class EmailServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.email_service"
    verbose_name = "Email Service"