from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin

# Register your models here.
from .models import (
    Memory,
)

@admin.register(Memory)
class MemoryAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка Memory"""
    list_display = ("firstname","lastname")
