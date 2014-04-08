from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''Shows the stores'''

	stores = hmod.Store.objects.filter(isActive="TRUE").order_by('locationName').exclude(id=99999)

	tvars = {

	'stores':stores,

	}

	return templater.render_to_response(request, 'searchstores.html', tvars)