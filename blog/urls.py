from django.contrib.auth import views as auth_views
from blog.views import MainView, AuthView
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
	# MainView
	url(r'^$', MainView.index, name='index'),
	url(r'^post/(?P<pk>[0-9A-Fa-f-]+)$', MainView.show, name='show'),
	url(r'^post/new$', MainView.new, name='new'),
	url(r'^post/update/(?P<pk>[0-9A-Fa-f-]+)$', MainView.update, name='update'),
	url(r'^post/del/(?P<pk>[0-9A-Fa-f-]+)$', MainView.delete, name='delete'),

	# AuthView
	url(r'^login/$', auth_views.LoginView.as_view(template_name='blog/auth/login.html'), name='login'),
	url(r'^logout/$', AuthView.logout_view, name='logout'),
]