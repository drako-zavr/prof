from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin

# Register your models here.
from .models import (
    Memory,
    Report
)

@admin.register(Memory)
class MemoryAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка Memory"""
    list_display = ("firstname","lastname")

@admin.register(Report)
class ReportAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка отчетов"""
    list_display = ("title",)
