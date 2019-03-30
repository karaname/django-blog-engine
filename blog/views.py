from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from blog.forms import PostForm
from blog.models import Post

def index(request):
	posts = Post.objects.order_by('-created_at')
	return render(request, 'blog/index.html', {'posts':posts})

def show(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/show.html', {'post':post})

def new(request):
	if request.method == 'GET':
		form = PostForm()
		return render(request, 'blog/new.html', {'form': form})
	else:
		form = PostForm(request.POST)

		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.save()
			return redirect('blog:index')


def logout_view(request):
	logout(request)
	return redirect('blog:index')