from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from manager.views.newcatalogitem import CatalogItemForm
from manager.views.newserializeditem import SerializedItemForm
import datetime
from django.contrib.auth.decorators import login_required

############
#FixLater --- Does this page do anything??? i don't think so... double check and then delete
#############
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
		'storeID': s.storeID,
		'catalogItem': s.catalogItem,
		'listPrice':s.listPrice,
		'cost':s.cost,
		'commissionRate': s.commissionRate,
		'serialNum':s.serialNum,
		'shelfLocation':s.shelfLocation,
		'conditionID':s.conditionID,
		'conditionDetails':s.conditionDetails,
		'isRental':s.isRental,
		'dateReceived': s.dateReceived,

		})

	if request.method == 'POST':
		form = SerializedItemForm(request.POST)
		if form.is_valid():
			#time to save the data
			s.storeID = form.cleaned_data['storeID']
			s.catalogItem = form.cleaned_data['catalogItem']
			s.listPrice = form.cleaned_data['listPrice']
			s.cost = form.cleaned_data['cost']
			s.commissionRate = form.cleaned_data['commissionRate']
			s.serialNum = form.cleaned_data['serialNum']
			s.shelfLocation = form.cleaned_data['shelfLocation']
			s.conditionID = form.cleaned_data['conditionID']
			s.conditionDetails = form.cleaned_data['conditionDetails']
			s.isRental = form.cleaned_data['isRental']
			s.dateReceived = form.cleaned_data['dateReceived']

			s.save()
			return HttpResponseRedirect('/manager/inventory/'+str(s.catalogItem.id))





	tvars = {

	's': s,
	'form':form,

	}

	return templater.render_to_response(request, 'item.html', tvars)




