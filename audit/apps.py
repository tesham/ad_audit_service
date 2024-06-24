from django.apps import AppConfig


# class AuditConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'audit'


class AuditConfig(AppConfig):
    name = 'audit'

    def ready(self):
        print('running rabbitmq consumer')
        from .rabbitmq_consumer import run_consumer
        run_consumer("audit_queue")
