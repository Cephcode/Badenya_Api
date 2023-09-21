
from django.urls import path,include
from .views import get_all_articles,get_article_by_id,update,get_articles_by_categories,search,update,create,delete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("articles/",get_all_articles),
    path("articles/<int:id>/",get_article_by_id),
    
    path("categories/<str:categorie>/",get_articles_by_categories),
    path("articles/search/<str:word>/",search),
    path("articles/update/<int:id>/",update),
    path("create/",create),
    path("delete/<int:id>/",delete),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)