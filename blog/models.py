from django.db import models
import uuid

class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

'''
CharField() - для хранения коротких строк, принимает один дополнительный аргумент
максимальную длинну строки
TextField() - для большого кол-ва текстовой информации
DateTimeField(auto_now_add=False/True) - принимает дату и время, есть ещё DateField
только с датой
'''