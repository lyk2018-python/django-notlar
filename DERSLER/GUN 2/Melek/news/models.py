from django.db import models

# Create your models here.

class NewsItem(models.Model):
	"""docstring for NewsItem"""
	title = models.CharField(max_length = 255)
	date_creation = models.DateTimeField(auto_now_add = True)
	date_publish = models.DateTimeField(blank = True, null = True)
	content = models.TextField()
	
	def __str__(self):
		return self.title
		