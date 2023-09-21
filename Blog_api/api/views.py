from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article,Categories
from .serializers import Article_serializers,Categorie_serializers

# Create your views here
# implementation du CRUD

# Read ( all articles)

@api_view(["GET"])
def get_all_articles(request):
    articles=Article.objects.all()
    data=Article_serializers(articles,many=True).data
    return  Response(data)

# Read (one articles)

@api_view(["GET"])
def get_article_by_id(request,id):
    article=Article.objects.filter(id=id)
    data=Article_serializers(article,many=True).data
    return Response(data)

#Read articles by categories

@api_view(["GET"])
def get_articles_by_categories(request,categorie):
    categorie=Categories.objects.filter(name=categorie)
    data=Categorie_serializers(categorie,many=True).data
    return Response(data)
#Read articles by searching
@api_view(["GET"])
def search(request,word):
    articles=Article.objects.filter(title__icontains=word)
    data=Article_serializers(articles,many=True).data
    return Response(data)

#Update article
@api_view(["GET","POST","PUT","PATCH"])
def update(request,id):
    article=Article.objects.filter(id=id).first()

    if request.method=="GET":
        data=Article_serializers(article,many=True).data
        categories_id=data[0]["categories"]
        data[0]["categories"]=Categories.objects.get(id=categories_id).name

    elif request.method=="POST":
        data=Article_serializers(article,data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)

#Create article
@api_view(["GET","POST"])
def create(request):
    if request.method=="POST":
        data=Article_serializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)


#DELETE article
@api_view(["DELETE"])
def delete(request,id):
    if request.method=="DELETE":
        article=Article.objects.filter(id=id).first()
        article.delete()
        return Response({"delete successfull"})

