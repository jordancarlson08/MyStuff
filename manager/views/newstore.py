from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from manager.views.stores import StoreForm
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''Shows the stores'''

	s = hmod.Store()
	form = StoreForm()
	#form = StoreForm(empty_permitted=True)

	if request.method == 'POST':
		form = StoreForm(request.POST)
		if form.is_valid():
			#time to save the data
			s.locationName = form.cleaned_data['locationName']
			s.street1 = form.cleaned_data['street1']
			s.street2 = form.cleaned_data['street2']
			s.city = form.cleaned_data['city']
			s.state = form.cleaned_data['state']
			s.zipCode = form.cleaned_data['zipCode']
			s.phone = form.cleaned_data['phone']
			s.manager = form.cleaned_data['manager']
			s.save()
			return HttpResponseRedirect('/manager/searchstores/')


	tvars = {

	'form':form,

	}


	return templater.render_to_response(request, 'newstore.html', tvars)



