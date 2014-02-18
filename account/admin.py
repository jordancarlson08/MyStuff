from django.db import models
from django.contrib import admin
from .models import *

# register any models here

admin.site.register(User)
admin.site.register(Employee)


def manager_check(user):
	return user.is_staff == True

def user_check(user):
	return user.id
