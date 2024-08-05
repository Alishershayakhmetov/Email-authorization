from django.apps import AppConfig


class OtpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'otp_email'
    
    def ready(self):
        import otp_email.signals
