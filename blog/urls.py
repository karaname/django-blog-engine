from django.contrib.auth import views as auth_views
from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<pk>[0-9A-Fa-f-]+)$', views.show, name='show'),

	url(r'^login/$', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
]
