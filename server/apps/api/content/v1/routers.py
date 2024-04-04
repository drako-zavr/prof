from django.urls import path

from .views import(
    MemoryAPIView,
    ReportAPIView,
    
)

app_name = "content"

urlpatterns = [
    # path("", ContentView.as_view(), name="index"),
    path("memory/", MemoryAPIView.as_view(), name="memory-list"),
    path("report/", ReportAPIView.as_view(), name="report-list"),
]
