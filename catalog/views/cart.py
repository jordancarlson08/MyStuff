from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from . import templater
from manager.views.newcatalogitem import CatalogItemForm
from manager.views.newinventoryitem import SerializedItemForm
import datetime



def process_request(request):
	'''Gets the cart'''


	# cart = request.session.get('cart', {})

	# #products = hmod.CatalogItem.objects.filter(id__in=cart.keys())


	# item_dict = {}

	# for p in cart.keys():
	# 	item = hmod.CatalogItem.objects.get(id=p)
	# 	item_dict[item] = cart[p]

	# tvars = {
	
	# 'item_dict': item_dict,


	# }


	cart = request.session.get('cart', {})

	cart_list =[]
	cart_all =[]

	for p in cart.keys():
		item = hmod.CatalogItem.objects.get(id=p)

		cart_item = CartItem(item, int(cart[p]))
		cart_list.append(cart_item)

		cart_all = Cart(cart_list)


	tvars = {

	'cart_all':cart_all,

	}

	return templater.render_to_response(request, 'cart.html', tvars)


def process_request__add(request):

	#Example URL: /catalog/cart__add/1/12/

	## Gets the Product ID and the Quantity from URL
	pid = str(request.urlparams[0])
	quantity = int(request.urlparams[1])

	##this gets the current cart ('current', or empty)
	cart = request.session.get('cart', {})

	if pid in cart:
		cart[pid] += quantity
	else:
		cart[pid] = quantity

	##this gives django the new cart
	request.session['cart'] = cart
	return HttpResponse('<script> window.location.href="/catalog/inventory/";</script>')



def process_request__delete(request):
	#remove from cart
	cart = request.session.get('cart', {})
	pid = str(request.urlparams[0])

	if pid in cart:
		del cart[pid]
	else: 
		#raise ItemNotFoundException
		print('Item not found in this cart')

	request.session['cart'] = cart
	return HttpResponse('<script> window.location.href="/catalog/category/";</script>')





class AddCartForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity',}))
