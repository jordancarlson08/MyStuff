from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from manager.views.stores import StoreForm
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''simple manage page'''



	tvars = {

	}


	return templater.render_to_response(request, 'manageusers.html', tvars)



