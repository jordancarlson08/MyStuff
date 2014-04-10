from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from manager.views.newcatalogitem import CatalogItemForm
from manager.views.newserializeditem import SerializedItemForm
import datetime
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''Shows the serialized item'''

	if request.urlparams[1] == 'delete':
		s = hmod.SerializedItem.objects.get(id=request.urlparams[0])
		s.isActive = False
		s.save()
		return HttpResponseRedirect('/manager/inventory/' + str(s.catalogItem.id))
 

	# get the serialized item
	s = hmod.SerializedItem.objects.get(id=request.urlparams[0])
	

	form = SerializedItemForm(initial={		
		'store': s.store,
		'catalogItem': s.catalogItem,
		'listPrice':s.listPrice,
		'cost':s.cost,
		'commissionRate': s.commissionRate,
		'serialNum':s.serialNum,
		'shelfLocation':s.shelfLocation,
		'condition':s.condition,
		'conditionDetails':s.conditionDetails,
		'isRental':s.isRental,

		})

	if request.method == 'POST':
		form = SerializedItemForm(request.POST)
		if form.is_valid():
			#time to save the data
			s.store = form.cleaned_data['store']
			s.catalogItem = form.cleaned_data['catalogItem']
			s.listPrice = form.cleaned_data['listPrice']
			s.cost = form.cleaned_data['cost']
			s.commissionRate = form.cleaned_data['commissionRate']
			s.serialNum = form.cleaned_data['serialNum']
			s.shelfLocation = form.cleaned_data['shelfLocation']
			s.condition = form.cleaned_data['condition']
			s.conditionDetails = form.cleaned_data['conditionDetails']
			s.isRental = form.cleaned_data['isRental']

			s.save()
			return HttpResponse('<script> window.location.href="";</script>')





	tvars = {

	's': s,
	'form':form,

	}

	return templater.render_to_response(request, 'item.html', tvars)




