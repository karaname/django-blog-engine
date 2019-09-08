from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
	# main
	path('', views.index, name='index'),
	path('post/<pk>', views.show, name='show'),
	path('post/create/', views.create, name='create'),
	path('post/update/<pk>', views.update, name='update'),
	path('post/del/<pk>', views.delete, name='delete'),

	# auth
	path('login/', auth_views.LoginView.as_view(template_name='blog/auth/login.html'), name='login'),
	path('logout/', views.logout_view, name='logout'),
]