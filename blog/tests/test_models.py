from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Post.objects.create(title='Main Title', body='Big random text')
		cls.post = Post.objects.first()

	def test_created_at_label(self):
		field_label = self.post._meta.get_field('created_at').verbose_name
		self.assertEquals(field_label, 'created at')

	def test_title_max_length(self):
		max_length = self.post._meta.get_field('title').max_length
		self.assertEquals(max_length, 100)
