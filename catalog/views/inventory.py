from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from manager.views.newcatalogitem import CatalogItemForm
from manager.views.newserializeditem import SerializedItemForm
import datetime



def process_request(request):
	'''Shows a catalog item to the user'''


 	#Display Function
	item = hmod.CatalogItem.objects.get(id=request.urlparams[0])
	item_count = hmod.SerializedItem.objects.filter(catalogItem=item).exclude(isRental=True).exclude(isSold=True).exclude(isActive=False).count()
	rental_count = hmod.SerializedItem.objects.filter(catalogItem=item).exclude(isRental=False).count()

	#Add to cart function
	form = AddCartForm()
	form = AddCartForm(initial={		
		'quantity': 1,
		})

	if request.method == 'POST':
		form = AddCartForm(request.POST)
		if form.is_valid():
			#time to save the data
			quantity = form.cleaned_data['quantity']

			a = '/catalog/cart__add/'
			b = str(item.id)+'/'
			c = str(quantity)+'/'
			url = a+b+c
			return HttpResponseRedirect(url)


	tvars = {
	
	'item':item,
	'item_count':item_count,
	'rental_count':rental_count,
	'form':form,

	}

	return templater.render_to_response(request, 'inventory.html', tvars)



class AddCartForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity',}))
