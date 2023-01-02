from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')
    contenu = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_created=True)
    update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre
    
