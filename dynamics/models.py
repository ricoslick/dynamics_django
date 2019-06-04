from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
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


# Create model Contributions which has a many-to-one relationship with model User
# Foreign key member
class Contribution(models.Model):
	member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	Contribution_date = models.DateField()

	




		