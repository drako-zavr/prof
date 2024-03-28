from rest_framework import views, generics
from ..models import Article
from .serializers import ArticleSerializer

class ArticleInfoAPIView(generics.ListAPIView):
    """
    Получение новостей
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.order_by("title")