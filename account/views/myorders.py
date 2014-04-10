from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the users transactions'''

	transactions = Transaction.objects.filter(user=request.user).order_by('created')

	tvars = {

	'transactions':transactions,

	}

	return templater.render_to_response(request, 'myorders.html', tvars)