from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="projects/static/img")
    
    
class About(models.Model):
    des = models.TextField()
    img = models.ImageField(upload_to='projects/templates/pics')
    
    
