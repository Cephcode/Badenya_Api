from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Article,Categories



class Article_serializers(ModelSerializer):
    categories = serializers.CharField(source='categories.name', read_only=True)
    # categories=Categorie_serializer(Categories,many=True)
    class Meta:
        model = Article
        fields = '__all__'

class Categorie_serializers(ModelSerializer):
    articles=Article_serializers(Article,many=True)
    
    class Meta:
        model=Categories
        fields="__all__"