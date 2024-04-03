from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin

from .models import Article
from .models import ArticleImage



class ImageInline(admin.StackedInline):
    model = ArticleImage
    extra = 0

@admin.register(Article)
class ArticleAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка новостей"""
    list_display = ("title","pub_date")
    inlines = (ImageInline,)


