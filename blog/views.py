from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import logout
from blog.forms import PostForm
from blog.models import Post

def index(request):
	posts = Post.objects.order_by('-created_at')

	paginator = Paginator(posts, 15)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'blog/main/index.html', {'posts':posts})

def show(request, pk):
	post = get_object_or_404(Post, id=pk)
	return render(request, 'blog/main/show.html', {'post':post})

@login_required
def create(request):
	if request.method == 'GET':
		form = PostForm()
		return render(request, 'blog/main/create.html', {'form': form})
	else:
		form = PostForm(request.POST)

		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.save()
			return redirect('blog:index')

@login_required
def update(request, pk):
	post = get_object_or_404(Post, id=pk)

	form = PostForm(request.POST or None, instance=post)
	if form.is_valid():
		form.save()
		return redirect('blog:index')

	return render(request, 'blog/main/update.html', {'form':form})

@login_required
def delete(request, pk):
	post = get_object_or_404(Post, id=pk).delete()
	return redirect('blog:index')

@login_required
def logout_view(request):
	logout(request)
	return redirect('blog:index')