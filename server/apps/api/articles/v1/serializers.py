from rest_framework import serializers

# Create your serializers here.
from ..models import Article, ArticleImage, ArticleDocument

class ArticleImagesSerializer(serializers.ModelSerializer):
    """
    Сериализатор фотографий
    """

    class Meta:
        model = ArticleImage
        fields = "__all__"

class ArticleDocumentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор документов
    """

    class Meta:
        model = ArticleDocument
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    """
    Сериализатор новостей
    """
    images = ArticleImagesSerializer(many=True)
    documents = ArticleDocumentsSerializer(many=True)


    class Meta:
        model = Article
        fields = "__all__"
    