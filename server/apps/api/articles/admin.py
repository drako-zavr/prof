from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin

# Register your models here.
from .models import Article
from .models import ArticleImage
# from .models import (
#     Memory,
# )


class ImageInline(admin.StackedInline):
    model = ArticleImage
    extra = 0

@admin.register(Article)
class ArticleAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка новостей"""
    list_display = ("title",)
    inlines = (ImageInline,)

# @admin.register(Memory)
# class DocumentAdmin( BaseAdminMixin, admin.ModelAdmin):
#     list_display = (
#         "firstname",
#     )

