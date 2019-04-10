from django.test import TestCase
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
