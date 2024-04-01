from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("articles/", include("apps.api.articles.v1")),
    path("content/", include("apps.api.content.v1")),
]
