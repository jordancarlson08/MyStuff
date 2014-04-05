from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''Shows the employees and users'''


	emps = amod.Employee.objects.filter(user__is_active='True').order_by('user__first_name').exclude(user__id=99997)
	user_list = get_users_only()

	tvars = {

	'emps':emps,
	'user_list':user_list,

	}

	return templater.render_to_response(request, 'searchusers.html', tvars)