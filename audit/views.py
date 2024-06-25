from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from audit.datalayer import AuditDatalayer


class AuthenticatedView(APIView):
    pass


class UnauthenticatedView(APIView):
    permission_classes = ()


class AuditApiView(AuthenticatedView):

    def get(self, request):
        try:
            user = request.query_params.get('user', None)
            ip = request.query_params.get('ip', None)
            module = request.query_params.get('module', None)
            label = request.query_params.get('label', None)
            start_date = request.query_params.get('start_date', None)
            end_date = request.query_params.get('end_date', None)
            queryset = AuditDatalayer.filter_audit(
                user=user, ip=ip, label=label, start_date=start_date, end_date=end_date, module=module
            )

            data = queryset.order_by('-created_at').values()

            return Response(
                data, status=status.HTTP_200_OK
            )

        except Exception as exe:
            return Response(
                dict(
                    message=str(exe)
                ), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )