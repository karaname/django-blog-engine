from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

def index(request):
	posts = Post.objects.order_by('-created_at')
	return render(request, 'blog/index.html', {'posts':posts})
