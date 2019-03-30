from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.http import HttpResponse
from blog.forms import PostForm
from blog.models import Post


class MainView(TemplateView):
	def index(request):
		posts = Post.objects.order_by('-created_at')

		paginator = Paginator(posts, 4)
		page = request.GET.get('page')
		posts = paginator.get_page(page)
		return render(request, 'blog/main/index.html', {'posts':posts})

	def show(request, pk):
		post = Post.objects.get(pk=pk)
		return render(request, 'blog/main/show.html', {'post':post})

	@login_required
	def new(request):
		if request.method == 'GET':
			form = PostForm()
			return render(request, 'blog/main/new.html', {'form': form})
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

		return render(request, 'blog/main/update.html', {'form':form})

	@login_required
	def delete(request, pk):
		post = Post.objects.get(id=pk).delete()
		return redirect('blog:index')

class AuthView(TemplateView):
	@login_required
	def logout_view(request):
		logout(request)
		return redirect('blog:index')