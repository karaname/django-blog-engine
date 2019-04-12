from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from blog.models import Post

class PostListViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		number_of_posts = 8
		for num_post in range(number_of_posts):
			Post.objects.create(title='Title', body='Text')

	def test_creation_check(self):
		self.assertEqual(len(Post.objects.all()), 8)

	def test_view_url_exists_at_desired_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_accessible_by_name(self):
		resp = self.client.get(reverse('blog:index'))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('blog:index'))
		self.assertEqual(resp.status_code, 200)

		self.assertTemplateUsed(resp, 'blog/main/index.html')

	def test_pagination_is_eight_first_p(self):
		resp = self.client.get(reverse('blog:index'))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('posts' in resp.context)
		self.assertEqual(len(resp.context['posts']), 4)
		self.assertTrue(resp.context['posts'], 4)

	def test_pagination_is_eight_second_p(self):
		resp = self.client.get(reverse('blog:index')+'?page=2')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('posts' in resp.context)
		self.assertEqual(len(resp.context['posts']), 4)
		self.assertTrue(resp.context['posts'], 4)

	def test_auth_url_new(self):
		user = User.objects.create_user('testuser', '', 'foobario')
		self.client.login(username='testuser', password='foobario')

		resp = self.client.get('/post/new')
		self.assertEqual(resp.status_code, 200)

		self.assertEqual(str(resp.context['user']), 'testuser')

		self.assertTemplateUsed(resp, 'blog/main/new.html')

	def test_redirect_if_not_logged(self):
		resp = self.client.get('/post/new')
		self.assertEqual(resp.status_code, 302)
		self.assertRedirects(resp, '/accounts/login/?next=/post/new', status_code=302, target_status_code=404)
