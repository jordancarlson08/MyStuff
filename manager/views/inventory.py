from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from manager.views.newcatalogitem import CatalogItemForm
from manager.views.newinventoryitem import SerializedItemForm
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows a catalog item and its associated serialized items'''

 	#Display Function
	item = hmod.CatalogItem.objects.get(id=request.urlparams[0])
	#This should get the serialized items that are tied to the catalog item
	serial = hmod.SerializedItem.objects.filter(catalogItem=item.id).filter(isActive=True)
	c = hmod.CatalogItem.objects.get(id=request.urlparams[0])

	conditions_list = hmod.Condition.objects.all()
	stores_list = hmod.Store.objects.filter(isActive="TRUE").order_by('locationName')
	rentals = hmod.SerializedItem.objects.filter(catalogItem=item.id).filter(isRental=True)

	form = CatalogItemForm(initial={
		'name': c.name,
		'manufacturer': c.manufacturer,
		'listPrice': c.listPrice,
		'cost': c.cost,
		'commissionRate': c.commissionRate,
		'description': c.description,
		'techSpecs': c.techSpecs,
		'sku': c.sku,
		'fillPoint': c.fillPoint,
		'leadTime': c.leadTime,
		'category':c.category,


		})



	if request.method == 'POST':
		form = CatalogItemForm(request.POST)
		if form.is_valid():
			#time to save the data
			c.name = form.cleaned_data['name'] 
			c.manufacturer = form.cleaned_data['manufacturer'] 
			c.listPrice = form.cleaned_data['listPrice'] 
			c.cost = form.cleaned_data['cost']
			c.commissionRate = form.cleaned_data['commissionRate'] 
			c.description = form.cleaned_data['description'] 
			c.techSpecs = form.cleaned_data['techSpecs'] 
			c.sku = form.cleaned_data['sku'] 
			c.fillPoint = form.cleaned_data['fillPoint'] 
			c.leadTime = form.cleaned_data['leadTime'] 
			c.category = form.cleaned_data['category']
			c.save()
			return HttpResponseRedirect('/manager/inventory/' + str(request.urlparams[0]))
			



	tvars = {
	
	'item':item,
	'form':form,
	'serial':serial,
	'conditions_list':conditions_list,
	'stores_list': stores_list,
	'rentals':rentals,

	}

	return templater.render_to_response(request, 'inventory.html', tvars)




def process_request__delete(request):
	#Delete Function

	c = hmod.CatalogItem.objects.get(id=request.urlparams[0])
	c.isActive = False
	c.save()
	return HttpResponseRedirect('/manager/searchinventory/')