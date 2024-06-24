from audit.models import Audit


class AuditDatalayer(object):

    @classmethod
    def filter_audit(cls, user=None, ip=None, module=None, label=None, start_date=None, end_date=None):

        queryset = Audit.objects.all()

        if user:
            queryset = queryset.filter(user=user)

        if ip:
            queryset = queryset.filter(ip=ip)

        if module:
            queryset = queryset.filter(module=module)

        if label:
            queryset = queryset.filter(label=label)

        if start_date and end_date:
            queryset = queryset.filter(created_at__date__range=[start_date, end_date])

        return queryset