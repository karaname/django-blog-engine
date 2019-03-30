from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from blog.forms import PostForm
from blog.models import Post

from django.contrib.auth.decorators import login_required


def index(request):
	posts = Post.objects.order_by('-created_at')
	return render(request, 'blog/index.html', {'posts':posts})

def show(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/show.html', {'post':post})

@login_required
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

@login_required
def update(request, pk):
	post = Post.objects.get(id=pk)

	form = PostForm(request.POST or None, instance=post)
	if form.is_valid():
		form.save()
		return redirect('blog:index')

	return render(request, 'blog/update.html', {'form':form})

@login_required
def delete(request, pk):
	post = Post.objects.get(id=pk).delete()
	return redirect('blog:index')

@login_required
def logout_view(request):
	logout(request)
	return redirect('blog:index')