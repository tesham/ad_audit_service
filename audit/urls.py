from django.urls import path
from .views import *

urlpatterns = [
    path('audit', AuditApiView.as_view(), name='audit_api_view'),
]