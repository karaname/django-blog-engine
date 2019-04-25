from django.conf.urls import include, url

from blog.sitemaps import PostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
	'static': StaticViewSitemap,
	'posts': PostSitemap,
}

urlpatterns = [
	url(r'', include('blog.urls')),
	url(r'^sitemap\.xml/$', sitemap, {'sitemaps':sitemaps})
]
