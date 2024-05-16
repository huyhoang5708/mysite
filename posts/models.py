from django.db import models

# Create your models here.
class Post (models.Model):
    name=models.CharField(max_length=255)
    body=models.TextField()
    slug=models.SlugField()
    image=models.ImageField(upload_to="media/image")
    