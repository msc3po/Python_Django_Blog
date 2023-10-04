from django.shortcuts import render
from .models import Post

def post_list(request):

    posts = Posts.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})
