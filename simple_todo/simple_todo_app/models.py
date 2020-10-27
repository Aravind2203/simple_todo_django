from django.db import models

# Create your models here.
class Todolist(models.Model):
	task=models.CharField(max_length=9999)

	def __str__(self):
		return self.task