from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from account.admin import manager_check
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''Shows the employees'''

	#users = amod.User.objects.filter(is_active="TRUE").order_by('first_name')
	emps = amod.Employee.objects.filter(user__is_active='True').order_by('user__first_name')

	tvars = {

	'emps':emps,

	}

	return templater.render_to_response(request, 'searchusers.html', tvars)