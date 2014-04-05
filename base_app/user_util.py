
from django.http import HttpResponseRedirect
from account.models import *
from manager.models import *
from catalog.models import *


#custom decorators
def manager_check(user):
	return user.is_staff == True

def user_check(user):
	return user.id

def my_account(function):
    '''Decorator that restricts access to the account page to the owner of that page and all managers'''
    def wrapper(request, *args, **kw):
        user=request.user
        userid = user.id
        url=request.urlparams[0]
        if user.id == int(url) or user.is_staff==True:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect('/account/user/'+str(userid))
    return wrapper



def get_users_only():
    '''Returns list of users withouth any employees'''
    employee_list = Employee.objects.filter(user__is_active='True').order_by('user__first_name').exclude(user__id=99997)
    emp_id = []
    for e in employee_list:
        emp_id.append(e.user.id)

    emp_id.append(99997)
    emp_id.append(99998)
    user_list = User.objects.filter(is_active=True).exclude(id__in=emp_id)
    return user_list