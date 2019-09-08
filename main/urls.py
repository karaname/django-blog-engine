from blog.sitemaps import PostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

sitemaps = {
	'static': StaticViewSitemap,
	'posts': PostSitemap,
}

urlpatterns = [
	path('', include('blog.urls')),
	path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
]