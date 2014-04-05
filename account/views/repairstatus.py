from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the users repairs'''

	repairs = Repair.objects.filter(user=request.user)

	tvars = {

	'repairs':repairs,

	}

	return templater.render_to_response(request, 'repairstatus.html', tvars)