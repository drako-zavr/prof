from rest_framework import serializers

# Create your serializers here.
from ..models import Article, ArticleImage

class ArticleImagesSerializer(serializers.ModelSerializer):
    """
    Сериализатор фотографий
    """

    class Meta:
        model = ArticleImage
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    """
    Сериализатор новостей
    """
    images = ArticleImagesSerializer(many=True)


    class Meta:
        model = Article
        fields = "__all__"