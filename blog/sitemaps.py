from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post

class StaticViewSitemap(Sitemap):
	def items(self):
		return ['blog:index']

	def location(self, item):
		return reverse(item)

class PostSitemap(Sitemap):
	def items(self):
		return Post.objects.all()
