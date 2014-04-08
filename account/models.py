from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser


	
#this is inheritance
class User(AbstractUser):
	'''This adds custom fields to the User'''
	#### Inherited from AbstractUser ####
	# is_active
	# is_superuser
	# is_staff
	# first_name
	# last_name
	# username
	# password
	# email
	phone = models.TextField(blank=True, null=True)
	security_question = models.TextField(blank=True, null=True)
	security_answer = models.TextField(blank=True, null=True)
	street1 = models.TextField(blank=True, null=True)
	street2 = models.TextField(blank=True, null=True)
	city = models.TextField(blank=True, null=True)
	state = models.TextField(blank=True, null=True)
	zipCode = models.IntegerField(blank=True, null=True)
	passwordResetCode = models.TextField(blank=True, null=True)
	passwordResetExp = models.DateTimeField(blank=True, null=True)
	
	def __str__(self):
  		return '%s %s - %s' %(self.first_name, self.last_name, self.username)

  
class Employee(models.Model):
	'''Employee specific info'''
	user = models.OneToOneField(User)
	hireDate = models.DateField(blank=True, null=True)
	salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)


	def __str__(self):
		return '%s %s - %s' %(self.user.first_name, self.user.last_name, self.user.username)


