from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from . import templater
from manager.views.newcatalogitem import CatalogItemForm
from manager.views.newserializeditem import SerializedItemForm
from datetime import *



def process_request(request):
	'''Shows a catalog item to the user'''

 	#Display Function
	item = CatalogItem.objects.get(id=request.urlparams[0])
	item_count = SerializedItem.objects.filter(catalogItem=item).exclude(isRental=True).exclude(isSold=True).exclude(isActive=False).count()
	rental_count = SerializedItem.objects.filter(catalogItem=item).exclude(isRental=False).count()

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

	#History - Recently Viewed Item

	#Basic - working
	if request.user.is_authenticated()==True:
		user = request.user
		isRecorded = False
		history = History.objects.filter(user=user)
		for h in history:
			if h.catalogItem == item:
				isRecorded = True
				h.save()

		if isRecorded!=True:
			h = History()
			h.user = user
			h.catalogItem = item
			h.save()
	else:
		#advanced - in progress
		history = request.session.get('history', {})
		history[item.id] = datetime.now().isoformat()
		request.session['history'] = history
				

	tvars = {
	
	'item':item,
	'item_count':item_count,
	'rental_count':rental_count,
	'form':form,

	}

	return templater.render_to_response(request, 'inventory.html', tvars)



class AddCartForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity',}))
