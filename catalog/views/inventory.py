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

	cart = request.session.get('cart', {})
	if request.urlparams[0] in cart:
		addbutton = 'Added to Cart!'
	else:
		addbutton = ''

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
		#records in database if logged in
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
		#records in session if not logged in
	else:
		history = request.session.get('history', {})
		history[item.id] = datetime.now().isoformat()
		request.session['history'] = history
				
	#Views - BI stuff
	item.views += 1
	item.save()

	tvars = {

	'addbutton':addbutton,
	'item':item,
	'item_count':item_count,
	'rental_count':rental_count,
	'form':form,

	}

	return templater.render_to_response(request, 'inventory.html', tvars)

def process_request__getcart(request):
	'''gets the current cart length'''

	cart = request.session.get('cart', {})
	rent = request.session.get('rent', {})
	repair = request.session.get('repair', {})
	cart_length = len(cart.keys()) + len(rent.keys()) + len(repair.keys())

	return HttpResponse (cart_length)


class AddCartForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity',}))
