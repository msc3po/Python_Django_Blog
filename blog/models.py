from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  content= models.TextField()
  published_date = models.DateTimeField(null=True, blank = True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
     return self.title

class Author(models.Model):
   author_name = models.CharField(max_length= 20)
   email = models.EmailField(null=True, blank=True)
   bio = models.TextField(null=True, blank=True)
   profile_picture = models.ImageField(upload_to= 'profile_pictures/', null=True, blank=True)