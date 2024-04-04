from rest_framework import generics
from ...models import Report
from ..serializers import ReportSerializer

class ReportAPIView(generics.ListAPIView):
    """
    Отчеты
    """
    serializer_class = ReportSerializer
    queryset = Report.objects.order_by("id")