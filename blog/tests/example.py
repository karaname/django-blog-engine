from django.test import TestCase

class TestClass(TestCase):
	@classmethod
	def setUpTestData(cls):
		print('\nsetUpTestData: Run once to set up non-modified data for all class method')

	def setUp(self):
		print('setUp: Run once for every test method to setup clean data')

	def test_true(self):
		print('Method: True Method')
		self.assertTrue(True)

	def test_math(self):
		print('Method: Math Method')
		self.assertEqual(1 + 1, 2)

	def tearDown(self):
		print('tearDown: After method')
