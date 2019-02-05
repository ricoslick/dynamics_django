from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50, unique=True)
	email = models.CharField(max_length=100)
	position = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	password_confirm = models.CharField(max_length=50)

	def __str__(self):
		return self.username

class Contribution(models.Model):
	member = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	balance = models.DecimalField(max_digits=9, decimal_places=2, default=0)
	contrib_date = models.DateField('date_published')

class Investments(models.Model):
	investment_name = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	returns = models.DecimalField(max_digits=9, decimal_places=2)
	profit = models.DecimalField(max_digits=9, decimal_places=2)
	status = models.CharField(max_length=10)
	invest_date = models.DateField('date_invested')


		