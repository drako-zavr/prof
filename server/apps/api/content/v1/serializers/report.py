from rest_framework import serializers
from ...models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    Сериализатор отчетов
    """

    class Meta:
        model = Report
        fields = "__all__"

