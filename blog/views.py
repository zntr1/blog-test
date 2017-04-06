from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    postliste = Post.objects.all().order_by('published_date')
	# 'posts ist die var im template, postliste die im view
    return render(request, 'blog/post_list.html', {'posts': postliste})