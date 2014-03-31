from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from catalog.models import *
from account.models import *
from . import templater
import datetime
from decimal import *
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Checkout process'''

	##### Everything to handle the 'cart' on the checkout page #####
	cart_all =[]
	rent_list =[]
	cart_list =[]

	# Shopping Cart
	cart = request.session.get('cart', {})

	for p in cart.keys():
		item = CatalogItem.objects.get(id=p)
		cart_item = CartItem(item, int(cart[p]))
		cart_list.append(cart_item)
		cart_all = Cart(cart_list, rent_list)
		
	# Rental Cart
	rent = request.session.get('rent', {})

	for p in rent.keys():
		item = SerializedItem.objects.get(id=p)
		rent_item = RentalCartItem(item)
		rent_list.append(rent_item)
		cart_all = Cart(cart_list, rent_list)
		
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
			t = Transaction()
			revenue = Sale()
			items_list=[]
			ssi = ''
			sci = ''
			for i in cart.keys():
				item = CatalogItem.objects.get(id=i)
				if item.isSerial == True:
					# Get the serialized items for the given cat item excluding already sold and rentals
					actual_list = SerializedItem.objects.filter(catalogItem=item)
					# get the first of the list, bad practice... fix later
					print(actual_list)
					actual = actual_list[0]

					#Mark Item as sold
					actual.isSold = True
					actual.save()

					ssi = SaleSerialItem()
					ssi.item = actual


					items_list.append(actual.listPrice)

				else:
					sci = SaleCatItem()
					sci.qty = cart[i]
					sci.item = item

					items_list.append(item.listPrice * sci.qty)


			revenue.amount = sum(items_list)
			revenue.save()

			if ssi != '':
				ssi.sale = revenue
				ssi.save()
			if sci != '':
				sci.sale=revenue
				sci.save()





			if Employee.objects.get(user=request.user): #Should execute as true if the logged in user is an employee
				t.user = User.objects.get(id=99999) 					#Walk-in (Dummy)
				t.employee = Employee.objects.get(user=request.user)	#Actual Employee
				t.store = Store.objects.get(id=1) 						#Store
			else:
				t.user = User.objects.get(id=request.user.id)  #Actual User
				t.employee = Employee.objects.get(id=99999)    #Online (Dummy)
				t.store = Store.objects.get(id=99999) 		   #Online (Dummy)

			

			t.subtotal = revenue.amount
			t.tax = revenue.amount * Decimal(.065)
			t.total = t.subtotal + t.tax
			t.paymentType = "CC"

			t.save()
			t.revenue.add(revenue)
			t.save()

			request.session['cart'] = {}

			return HttpResponseRedirect('/catalog/category')
			




	tvars = {

	'form':form,
	'cart_all':cart_all,

	}

	return templater.render_to_response(request, 'checkout.html', tvars)




@login_required
def process_request__rental(request):
	'''Checkout process'''

	##### Everything to handle the 'cart' on the checkout page #####
	cart_all =[]
	rent_list =[]
	cart_list =[]

	# Shopping Cart
	cart = request.session.get('cart', {})

	for p in cart.keys():
		item = CatalogItem.objects.get(id=p)
		cart_item = CartItem(item, int(cart[p]))
		cart_list.append(cart_item)
		cart_all = Cart(cart_list, rent_list)
		
	# Rental Cart
	rent = request.session.get('rent', {})

	for p in rent.keys():
		item = SerializedItem.objects.get(id=p)
		rent_item = RentalCartItem(item)
		rent_list.append(rent_item)
		cart_all = Cart(cart_list, rent_list)
		
	##### Cart End #####

	##### Checkout Form Stuff ######

	# Get User existing info #
	# customer = User.objects.get(id=request.user.id)
	# Prefill with existing info #
	# form = CheckoutForm(initial={
	# 	'bill_first_name': customer.first_name,
	# 	'bill_last_name': customer.last_name,
	# 	'bill_phone': customer.phone,
	# 	'bill_email': customer.email,
	# 	'bill_street1': customer.street1,
	# 	'bill_street2': customer.street2,
	# 	'bill_city': customer.city,
	# 	'bill_state': customer.state,
	# 	'bill_zipCode': customer.zipCode,
	# 	})

	form = CheckoutForm()

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

	return templater.render_to_response(request, 'checkout.html', tvars)












class CheckoutForm(forms.Form):
	'''The form used for checkout'''

	#Billing Info
	bill_first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
	bill_last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
	bill_phone = forms.CharField(label='Phone', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	bill_email = forms.CharField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'me@example.com',}))
	bill_street1 = forms.CharField(label='Street 1', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	bill_street2 = forms.CharField(label='Street 2', required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	bill_city = forms.CharField(label='City', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	bill_state = forms.CharField(label='State', max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	bill_zipCode = forms.IntegerField(label='Zip Code',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))
	#use_bill - True if shipping info is the same as billing info
	use_bill = forms.BooleanField(label='Same as Billing', required=False )
	#Shipping Info - If use_bill = True then auto assign these to be the same
	ship_first_name = forms.CharField(required=False, label='First Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
	ship_last_name = forms.CharField(required=False, label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
	ship_phone = forms.CharField(required=False, label='Phone', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	ship_email = forms.CharField(required=False, label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'me@example.com',}))
	ship_street1 = forms.CharField(required=False, label='Street 1', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	ship_street2 = forms.CharField(required=False, label='Street 2', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	ship_city = forms.CharField(required=False, label='City', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	ship_state = forms.CharField(required=False, label='State', max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	ship_zipCode = forms.IntegerField(required=False, label='Zip Code',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))
	#Shipping method
	shipping = forms.ModelChoiceField(label='Shipping Method', queryset=Shipping.objects.all().order_by('price'), widget=forms.Select(attrs={'class': 'form-control',}))
	#Payment
	card = forms.IntegerField(label='Credit Card', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1234 5678 9012 3456'}))
	code = forms.IntegerField(label='Security Code', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '445'}))
	exp_month = forms.IntegerField(label='Expiration Month', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MM'}))
	exp_year = forms.IntegerField(label='Expiration Year', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'YYYY'}))



