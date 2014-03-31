from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from . import templater


def process_request(request):
	'''Gets the cart'''

	cart_all =[]
	rent_list =[]
	cart_list =[]

	# Shopping Cart
	cart = request.session.get('cart', {})

	for p in cart.keys():
		item = hmod.CatalogItem.objects.get(id=p)
		cart_item = CartItem(item, int(cart[p]))
		cart_list.append(cart_item)
		cart_all = Cart(cart_list, rent_list)
		
	# Rental Cart
	rent = request.session.get('rent', {})

	for p in rent.keys():
		item = hmod.SerializedItem.objects.get(id=p)
		rent_item = RentalCartItem(item)
		rent_list.append(rent_item)
		cart_all = Cart(cart_list, rent_list)
		

	tvars = {

	'cart_all':cart_all,

	}

	return templater.render_to_response(request, 'cart.html', tvars)


def process_request__add(request):
	'''Adds an item to the cart'''

	#---Example URL: /catalog/cart__add/1/12/---#

	## Gets the Product ID and the Quantity from URL
	pid = str(request.urlparams[0])
	quantity = int(request.urlparams[1])

	## This gets the current shopping cart ('current', or empty)
	cart = request.session.get('cart', {})
	## Rental Cart
	rent = request.session.get('rent', {})

	if(request.urlparams[2] != 'rental'):
		if pid in cart:
			cart[pid] += quantity
		else:
			cart[pid] = quantity

	if(request.urlparams[2] == 'rental'):
		if pid in rent:
			rent[pid] += quantity
		else:
			rent[pid] = quantity

	## This gives django the new carts
	request.session['rent'] = rent
	request.session['cart'] = cart

	return HttpResponse('<script> window.location.href="/catalog/inventory/";</script>')



def process_request__delete(request):
	'''Removes an item from the cart'''

	# Remove from shopping cart
	cart = request.session.get('cart', {})
	pid = str(request.urlparams[0])

	if pid in cart:
		del cart[pid]
	else: 
		#raise ItemNotFoundException
		print('Item not found in this cart')

	request.session['cart'] = cart

	# Remove from rental cart
	rent = request.session.get('rent', {})
	pid = str(request.urlparams[0])

	if pid in rent:
		del rent[pid]
	else: 
		#raise ItemNotFoundException
		print('Item not found in this rent')

	request.session['rent'] = rent


	return HttpResponse('<script> window.location.href="/catalog/category/";</script>')



class AddCartForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity',}))
