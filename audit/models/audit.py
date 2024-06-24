from django.db import models


class Audit(models.Model):
    user = models.CharField(max_length=100)
    session_id = models.IntegerField(null=True)
    module = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    action = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'audits'
