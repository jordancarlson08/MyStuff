from django.db import models
from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect

# register any models here

admin.site.register(User)
admin.site.register(Employee)


#custom decorators
def manager_check(user):
	return user.is_staff == True

def user_check(user):
	return user.id

def my_account(function):
    def wrapper(request, *args, **kw):
        user=request.user
        url=request.urlparams[0]
        if user.id != int(url):
            return HttpResponseRedirect('/index/nice_try:)')
        else:
            return function(request, *args, **kw)
    return wrapper



