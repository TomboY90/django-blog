from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(req):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    return render(req, 'blog/post_list.html', {'posts': posts})
