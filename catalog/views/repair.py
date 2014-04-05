from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from account.models import *
from . import templater
from manager.views.newcatalogitem import CatalogItemForm
from manager.views.newserializeditem import SerializedItemForm
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Checkout process'''

	##### Everything to handle the 'cart' on the checkout page #####
	cart = request.session.get('cart', {})
	cart_list =[]
	cart_all =[]
	for p in cart.keys():
		item = hmod.CatalogItem.objects.get(id=p)
		cart_item = CartItem(item, int(cart[p]))
		cart_list.append(cart_item)
		cart_all = Cart(cart_list)
	##### Cart End #####


	##### Checkout Form Stuff ######

	# Get User existing info #
	customer = User.objects.get(id=request.user.id)

	# Prefill with existing info #
	form = CheckoutForm(initial={
		'bill_first_name': customer.first_name,
		'bill_last_name': customer.last_name,
		'bill_phone': customer.phone,
		'bill_email': customer.email,
		'bill_street1': customer.street1,
		'bill_street2': customer.street2,
		'bill_city': customer.city,
		'bill_state': customer.state,
		'bill_zipCode': customer.zipCode,
		})

	if request.method == 'POST':
		form = CheckoutForm(request.POST)
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

	'form':form,
	'cart_all':cart_all,

	}

	return templater.render_to_response(request, 'repair.html', tvars)

class CheckoutForm(forms.Form):
	'''The form used for checkout'''

	#Billing Info
	bill_first_name = forms.CharField(label='First Name', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
	bill_last_name = forms.CharField(label='Last Name', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
	bill_phone = forms.CharField(label='Phone', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	bill_email = forms.CharField(label='Email', max_length=25, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'me@example.com',}))
	bill_street1 = forms.CharField(label='Street 1', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	bill_street2 = forms.CharField(label='Street 2', required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	bill_city = forms.CharField(label='City', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	bill_state = forms.CharField(label='State', max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	bill_zipCode = forms.IntegerField(label='Zip Code',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))
	#Payment
	card = forms.IntegerField(label='Credit Card', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1234 5678 9012 3456'}))
	code = forms.IntegerField(label='Security Code', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '445'}))
	exp_month = forms.IntegerField(label='Expiration Month', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MM'}))
	exp_year = forms.IntegerField(label='Expiration Year', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'YYYY'}))



