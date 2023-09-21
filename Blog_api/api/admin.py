from django.contrib import admin
from .models import Article,Categories

# Register your models here.
class Categories_model(admin.ModelAdmin):
    # class Meta:
        model=Article

class Article_model(admin.ModelAdmin):
    # class Meta:
        model=Article
        list_display=("title","text","creation_date")

admin.site.register(Categories,Categories_model)
admin.site.register(Article,Article_model)
