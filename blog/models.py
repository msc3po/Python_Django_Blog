from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_lenght=255)
  content= models.TextField()
  published_date = models.DateTimeField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
     return self.title

class Author(models.Model):
   author_name = models.TextField(max_length= (80))