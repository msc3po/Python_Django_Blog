from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView
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


### refactor to a DetailView?
def read_post(request, post_id):

        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'blog/read_post.html', {'post': post})