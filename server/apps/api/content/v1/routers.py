from django.urls import path

from .views import(
    MemoryAPIView
)

app_name = "content"

urlpatterns = [
    # path("", ContentView.as_view(), name="index"),
    path("list/", MemoryAPIView.as_view(), name="memory"),
]
