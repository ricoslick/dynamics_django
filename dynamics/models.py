from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50, unique=True)
	email = models.CharField(max_length=100)
	position = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	password_confirm = models.CharField(max_length=50)
	url= models.SlugField(max_length=500, unique=True, blank=True)

	def __str__(self):
		return self.username

	def save(self, *args, **kwargs):
		self.url=slugify(self.username)
		super(User, self).save(*args, **kwargs)


class Contribution(models.Model):
	member = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	balance = models.DecimalField(max_digits=9, decimal_places=2, default=0)
	contrib_date = models.DateField('date_published')
	url= models.SlugField(max_length=500, unique=True, blank=True)

	def save(self, *args, **kwargs):
		self.url=slugify(self.username)
		super(User, self).save(*args, **kwargs)

	
class Investments(models.Model):
	investment_name = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	returns = models.DecimalField(max_digits=9, decimal_places=2)
	profit = models.DecimalField(max_digits=9, decimal_places=2)
	status = models.CharField(max_length=10)
	invest_date = models.DateField('date_invested')
	url = models.SlugField(max_length=500, unique=True, blank=True)

	def save(self, *args, **kwargs):
		self.url=slugify(self.username)
		super(User, self).save(*args, **kwargs)


		