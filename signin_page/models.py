from django.db import models
#after Create new models run this comands 
### python3 manage.py makemigrations ###
### python3 manage.py migrate ###
# Create your models here.
class blog(models.Model):
	title = models.CharField(max_length =100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title

	def shot(self):
		return (self.body[:65] + '...')
