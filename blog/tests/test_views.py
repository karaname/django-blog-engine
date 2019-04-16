from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.test import Client
from blog.models import Post

class PostListViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		number_of_posts = 8
		for num_post in range(number_of_posts):
			cls.post = Post.objects.create(title='Title', body='Text')

		cls.posts = Post.objects.all()
		cls.user = User.objects.create_user('testuser', '', 'foobario')

	def test_creation_obj(self):
		self.assertEqual(len(self.posts), 8)

	def test_url_index(self):
		resp = self.client.get(reverse('blog:index'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'blog/main/index.html')

	def test_pagination_first_page(self):
		resp = self.client.get(reverse('blog:index')+'?page=1')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('posts' in resp.context)
		self.assertTrue(resp.context['posts'], 4)
		self.assertEqual(len(resp.context['posts']), 4)

	def test_pagination_second_page(self):
		resp = self.client.get(reverse('blog:index')+'?page=2')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('posts' in resp.context)
		self.assertTrue(resp.context['posts'], 4)
		self.assertEqual(len(resp.context['posts']), 4)

	def test_url_show(self):
		resp = self.client.get(reverse('blog:show', kwargs={'pk':self.post.id}))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('post' in resp.context)
		self.assertTemplateUsed(resp, 'blog/main/show.html')

	def test_logged_user_url_new(self):
		self.client.login(username='testuser', password='foobario')
		resp = self.client.get(reverse('blog:new'))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(str(resp.context['user']), 'testuser')
		self.assertTrue('form' in resp.context)
		self.assertTemplateUsed(resp, 'blog/main/new.html')

	def test_redirect_if_user_not_auth_url_new(self):
		resp = self.client.get(reverse('blog:new'))
		self.assertEqual(resp.status_code, 302)
		self.assertRedirects(resp, '/accounts/login/?next=/post/new', status_code=302, target_status_code=404)

	def test_logged_user_url_update(self):
		self.client.login(username='testuser', password='foobario')
		resp = self.client.get(reverse('blog:update', kwargs={'pk':self.post.id}))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(str(resp.context['user']), 'testuser')
		self.assertTrue('form' in resp.context)
		self.assertTemplateUsed(resp, 'blog/main/update.html')

	def test_redirect_if_user_not_auth_url_update(self):
		resp = self.client.get(reverse('blog:update', kwargs={'pk':self.post.id}))
		self.assertEqual(resp.status_code, 302)
		self.assertRedirects(resp, '/accounts/login/?next=/post/update/' + str(self.post.id), status_code=302, target_status_code=404)

	def test_logged_user_url_delete(self):
		self.client.login(username='testuser', password='foobario')
		resp = self.client.get(reverse('blog:delete', kwargs={'pk':self.post.id}))
		self.assertEqual(resp.status_code, 302)
		self.assertRedirects(resp, reverse('blog:index'), status_code=302, target_status_code=200)

	def test_each_obj_uuid(self):
		for post in self.posts:
			post_id = str(post.id)
			self.assertEqual(len(post_id), 36)
