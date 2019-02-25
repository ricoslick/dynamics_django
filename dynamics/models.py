from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.forms import ModelForm
from django.template.defaultfilters import slugify

# Create your models here.
# Extend inbuilt User model by subclassing AbstractUser and adding custom fields 
class CustomUser(AbstractUser):
	post = models.CharField(max_length=30)
	password_confirm = models.CharField(max_length=500)
	slug = models.SlugField(max_length=500, unique=True, blank=True)


	def __str__(self):
		return self.username

	def save(self, *args, **kwargs):
		self.slug=slugify(self.username)
		super(CustomUser, self).save(*args, **kwargs)




		