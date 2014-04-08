from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(employee_check)
def process_request(request):
	'''Shows the dashboard'''


	tvars = {

	}

	return templater.render_to_response(request, 'dash.html', tvars)