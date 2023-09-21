from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
def default():
    return Categories.objects.get(name="recent").id

class Article(models.Model):
    author=models.CharField(max_length=300,blank=True,null=True)
    title=models.CharField(max_length=200,blank=True,null=True)
    creation_date=models.DateField(auto_now_add=True)
    # header_image=models.ImageField(upload_to=)
    text=models.TextField(blank=True,null=True)
    categories=models.ForeignKey(Categories,blank=True, null=True,on_delete=models.CASCADE,related_name="articles")
    cover_img=models.ImageField(upload_to="articles_cover",blank=True,null=True)
    def __str__(self):
        return self.title
    
