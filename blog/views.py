from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def post_list(request):

    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})