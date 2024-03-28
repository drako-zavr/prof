from django.urls import path
from .views import ArticleInfoAPIView

app_name = "articles"

urlpatterns = [
    path("list/", ArticleInfoAPIView.as_view(), name="articles"),
]
