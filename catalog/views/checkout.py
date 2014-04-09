from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from catalog.models import *
from account.models import *
from base_app.user_util import get_users_only
from catalog.accounting import record_sale
from . import templater
from datetime import *
from decimal import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import requests

#TestingPurposes -- Find and remove all print statments

@login_required
def process_request(request):
	'''Checkout process'''

	## Constants ##
	SALES_TAX = 0.065

	##### Everything to handle the 'cart' on the checkout page #####
	cart_all =[]
	cart_list =[]
	rent_list =[]
	repair_list=[]
	subtotal_list = []
	skip_list = []

	isCartEmpty=True
	isRentEmpty=True
	isRepairEmpty=True

	cart = request.session.get('cart', {})
	rent = request.session.get('rent', {})
	repair = request.session.get('repair', {})

	for p in cart.keys():
		item = CatalogItem.objects.get(id=p)
		cart_item = CartItem(item, int(cart[p]))
		cart_list.append(cart_item)
		cart_all = Cart(cart_list, rent_list, repair_list)
		isCartEmpty=False

	for p in rent.keys():
		item = SerializedItem.objects.get(id=p)
		rent_item = RentalCartItem(item)
		rent_list.append(rent_item)
		cart_all = Cart(cart_list, rent_list, repair_list)
		isRentEmpty=False

	for p in repair.keys():
		repair_item = RepairCartItem(p)
		repair_list.append(repair_item)
		cart_all = Cart(cart_list, rent_list, repair_list)
		isRepairEmpty=False
	##### Cart End #####

	isEmployee = 'NotSet'
	try:
		# Get employee
		currentEmployee = Employee.objects.get(user__id=request.user.id)
		isEmployee = True
	except:
		# Get User
		currentCustomer = User.objects.get(id=request.user.id)
		isEmployee = False

	### Checks if its a Rental Return ###
	isRentalReturn = False
	if(request.urlparams[0] != ''):
		isRentalReturn = True

	### CREATE the skip list used for layout of fields ###
	skip_ship = ['use_bill', 'ship_first_name', 'ship_last_name', 'ship_phone', 'ship_email', 'ship_street1', 'ship_street2', 'ship_city', 'ship_state', 'ship_zipCode', 'shipping']
	skip_rent = ['days', 'username']
	skip_repair = ['dateComplete', 'description', 'hours', 'status', 'amount']

	if isEmployee==True:
		skip_list = skip_list + skip_ship
	if isRentEmpty == True:
		skip_list = skip_list + skip_rent
	if isRepairEmpty == True:
		skip_list = skip_list + skip_repair

	#Error Handling: If its a user that has rentals in his cart (should be impossible) redirect to the homepage and clear cart
	if (isEmployee == False and isRentEmpty == False):
		request.session['rent'] = {}
		return HttpResponseRedirect('/catalog/category')

	if (isEmployee==False):
		# Prefill with existing info --- Remove card info later ---
		form = CheckoutForm(initial={
			'bill_first_name': currentCustomer.first_name,
			'bill_last_name': currentCustomer.last_name,
			'bill_phone': currentCustomer.phone,
			'bill_email': currentCustomer.email,
			'bill_street1': currentCustomer.street1,
			'bill_street2': currentCustomer.street2,
			'bill_city': currentCustomer.city,
			'bill_state': currentCustomer.state,
			'bill_zipCode': currentCustomer.zipCode,
			'card': '4732817300654',
			'code': '411',
			'exp_month': '10',
			'exp_year': '14',
			})
	else:
		# Prefill only card info --- Remove later --- #TestingPurposes
		form = CheckoutForm(initial={
			'card': '4732817300654',
			'code': '411',
			'exp_month': '10',
			'exp_year': '14',
			})

	#TestingPurposes
	# At this point we know if there are sale items and rentals in the checkout and if its an employee or a user
	#case 1 - User - Sale Items
		#need Shipping
		#dont display days or username
	#case 2 - Employee - Sale Items
		#dont display days
	#case 3 - Employee - Rental Items
	#case 4 - Employee - Sale & Rental Items

	if request.method == 'POST': #Only execute if the form has been submitted #FixLater #100 --- Execute only if form is valid --- remove from below
	# form = CheckoutForm(request.POST)
	# if form.is_valid():
		t = Transaction() #Create one transaction for the entire checkout
		t.user = User.objects.get(id=99998)
		t.employee = Employee.objects.get(id=99998)    #Online Sales Employee (Commissionless)
		t.store = Store.objects.get(id=99999) 
		t.subtotal = 0
		t.tax = 0
		t.total = 0
		t.save()


		################################################
		###############  SALE REVENUE  #################
		################################################

		if (isCartEmpty==False):
			# if request.method == 'POST': #FixLater --- Remove once FixLater #100 has been addressed
			form = CheckoutForm(request.POST) #FixLater --- Remove once FixLater #100 has been addressed
			if form.is_valid(): #FixLater --- Remove once FixLater #100 has been addressed

				r = Sale()
				r.amount = 0
				r.save()
				items_list=[]
				cost_list=[]
				ssi = ''
				sci = ''
				for i in cart.keys():
					item = CatalogItem.objects.get(id=i)
					if item.isSerial == True:
						# Get the serialized items for the given cat item excluding already sold and rentals ---------------------# This part should only give new items (not tested)
						actual_list = SerializedItem.objects.filter(catalogItem=item).exclude(isRental=True).filter(isSold=False) #.filter(condition=Condition.objects.get(id=1))
						actual = actual_list[0] #get the first of the list, bad practice... #FixLater --- the part just above this might not make it so bad
						actual.isSold = True
						actual.save()
						ssi = SaleSerialItem()
						ssi.item = actual
						ssi.sale = r
						ssi.save()
						items_list.append(actual.listPrice)
						cost_list.append(actual.cost)

					else:
						sci = SaleCatItem()
						sci.qty = cart[i]
						sci.item = item
						sci.sale = r
						sci.save()
						items_list.append(item.listPrice * sci.qty)
						cost_list.append(actual.cost * sci.qty)


				r.amount = sum(items_list) #updates the Revenue(Sale).amount to the subtotal of all items in cart
				r.save()

				if(isEmployee!=True):
					t.user = currentCustomer 					   #Logged In User
					t.employee = Employee.objects.get(id=99998)    #Online Sales Employee (Commissionless)
					t.store = Store.objects.get(id=99999) 		   #Online Sales Store
				else: # Case 2
					t.user = User.objects.get(id=99998) 		   #Walk-in Customer
					t.employee = currentEmployee				   #Logged In Employee
					t.store = Store.objects.get(id=99999)		   #Whatever Store ----- #FixLater

				#### Add shipping cost ####
				ship_price = 0
				if isEmployee == False:
					try:
						ship_option = form.cleaned_data['shipping']
					except:
						ship_option = None

					if ship_option != None:
						ship_price = ship_option.price
						subtotal_list.append(ship_price)
						cost_list.append(ship_price)

				t.save()
				t.revenue.add(r)
				t.save()

				subtotal_list.append(r.amount)

				t.subtotal = r.amount
				t.tax = r.amount * Decimal(SALES_TAX)
				t.total = t.subtotal + t.tax
				t.save()

				# sum of the cost of the items in the sale
				c = sum(cost_list)

				# Creates the accounting entries for the sale of inventory
				record_sale(t, c)

				################################################
				############ END: SALE REVENUE  ################
				################################################


		################################################
		############## RENTAL REVENUE  #################
		################################################

		if (isRentEmpty==False):
			if request.method == 'POST': #FixLater --- Remove once FixLater #100 has been addressed
				form = CheckoutForm(request.POST) #FixLater --- Remove once FixLater #100 has been addressed
				if form.is_valid(): #FixLater --- Remove once FixLater #100 has been addressed

					#Revenue Source --- Rental
					r = Rental()
					r.dateOut = date.today()
					r.dateDue = datetime.now() + timedelta(days=form.cleaned_data['days'])
					r.amount = 0
					r.save()

					items_list=[]

					for i in rent.keys():
						item = SerializedItem.objects.get(id=i)
						item.isRented = True
						item.save()

						ri = RentalItem()
						ri.item = item
						ri.rental = r
						ri.save()
						items_list.append(item.pricePerDay * form.cleaned_data['days'])

					r.amount = sum(items_list)
					r.save()


					try:
						t.user = form.cleaned_data['username']
						# t.user = User.objects.get(username=form.cleaned_data['username']) #TestingPurposes
					except:
						t.user = User.objects.get(id=99998)
						print('Could not find user, used user_id 99998')

					t.employee = currentEmployee
					t.store = Store.objects.get(id=1) #FixLater -- don't hardcode the store
					t.save()
					t.revenue.add(r)
					t.save()

					subtotal_list.append(r.amount)

					################################################
					########### END: RENTAL REVENUE  ###############
					################################################

		################################################
		############## RENTAL RETURN   #################
		################################################

		form = CheckoutForm(request.POST)
		if form.is_valid():
			if (isRentalReturn==True):
				rental = Rental.objects.get(id=request.urlparams[0])
				damage = Damage.objects.get(id=request.urlparams[1])
				try:
					late = Late.objects.get(id=request.urlparams[2])
				except:
					late = ''

				rental_items = RentalItem.objects.filter(rental=rental)
				for ri in rental_items:
					ri.item.isRented = False
					ri.item.save()

				fee_list = []
				rr = RentalReturn()
				rr.rental = rental
				rr.dateIn = datetime.now()
				rr.save()
				rr.fee.add(damage)
				rr.save()
				fee_list.append(damage.amount)
				if late != '':
					rr.fee.add(late)
					rr.save()
					fee_list.append(late.amount)

				lastT = Transaction.objects.get(revenue=rental)
				t.user = lastT.user
				t.employee = currentEmployee
				t.store = lastT.store
				t.save()
				t.revenue.add(rr)
				t.save()
				subtotal_list.append(sum(fee_list))

			################################################
			############# END RENTAL RETURN ################
			################################################


		################################################
		############## REPAIR REVENUE  #################
		################################################

		if (isRepairEmpty==False):
			if request.method == 'POST': #FixLater --- Remove once FixLater #100 has been addressed
				form = CheckoutForm(request.POST) #FixLater --- Remove once FixLater #100 has been addressed
				if form.is_valid(): #FixLater --- Remove once FixLater #100 has been addressed

					#Get existing Repair and update the crap out of it
					user = ''
					rev_list=[]
					for a in repair.keys():
						r = Repair.objects.get(id=a)
						r.datePickup = datetime.now()
						r.dateComplete = form.cleaned_data['dateComplete']
						r.description  = form.cleaned_data['description']
						r.hours = form.cleaned_data['hours']
						r.status = form.cleaned_data['status']
						r.amount = form.cleaned_data['amount']
						r.isOpen = False
						rev_list.append(r.amount)
						r.save()
						user = r.user
						t.save()
						t.revenue.add(r)
						t.save()

					if (user!=''):
						t.user = user
					else:
						t.user = User.objects.get(id=99998) #TestingPurposes --- should never happen -- #FixLater
					t.employee = currentEmployee
					t.store = Store.objects.get(id=1) #FixLater -- don't hardcode the store
					t.save()

					subtotal_list.append(sum(rev_list))

					################################################
					########### END: REPAIR REVENUE  ###############
					################################################

				
		t.subtotal = sum(subtotal_list)
		t.tax = t.subtotal * Decimal(SALES_TAX)
		t.total = t.subtotal + t.tax

		if (isEmployee !=True):
			t.paymentType = "CC"
		else:
			t.paymentType = "CC" #FixLater --- Could add a drop down to checkout page for CC or Cash payment --- Maybe should leave it

		t.save()


		################################################
		######### SEND CHARGE TO REST SERVER ###########
		################################################

		# send the request with the data
		API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
		API_KEY = 'b5559636bffb4c3d6896c1fd169da803'
		amount = str(t.total)
		description = 'Transaction: %s; Charge for %s' %(t.id, t.user.email)
		r = requests.post(API_URL, data={
		  'apiKey': API_KEY,
		  'currency': 'usd',
		  'amount': amount,
		  'type': 'Visa',
		  'number': form.cleaned_data['card'],
		  'exp_month': form.cleaned_data['exp_month'],
		  'exp_year': form.cleaned_data['exp_year'],
		  'cvc': form.cleaned_data['code'],
		  'name': 'Cosmo Limesandal',
		  'description': description,
		})

		# just for debugging, print the response text
		print(r.text)

		# parse the response to a dictionary
		resp = r.json()
		print(resp['ID'])


		################################################
		################# SEND EMAIL ###################
		################################################

		# Sends a receipt - maybe put this into a special redirect.py page or something
		send_mail('Receipt for transaction number %s' %(str(t.id)), 'This is your transaction: %s' %(r.text), 'webmaster@digitallifemyway.com',
		['jordancarlson08@gmail.com'], fail_silently=False)

		# Clear out shopping cart
		request.session['cart'] = {}	
		request.session['rent'] = {}
		request.session['repair'] = {}

		return HttpResponseRedirect('/catalog/receipt/'+str(t.id))
			
	tvars = {

	'form':form,
	'cart_all':cart_all,
	'isEmployee': isEmployee,
	'isCartEmpty':isCartEmpty,
	'isRentEmpty':isRentEmpty,
	'isRepairEmpty': isRepairEmpty,
	'skip_list':skip_list,

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
	shipping = forms.ModelChoiceField(required=False, label='Shipping Method', queryset=Shipping.objects.all().order_by('price'), widget=forms.Select(attrs={'class': 'form-control',}))
	# Rental stuff
	days = forms.IntegerField(required= False, label='Days to Rent', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2'}))
	# username = forms.ModelChoiceField(label='User', queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
	username = forms.ModelChoiceField(required =False, label='User', queryset=get_users_only(), widget=forms.Select(attrs={'class': 'form-control',}))
	# Repair Stuff
	dateComplete = forms.DateField(required=False, label='Date Complete', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Complete',}))
	hours = forms.DecimalField(required=False, label='Hours', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hours',}))
	status = forms.CharField(required=False, label='Status', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status',}))
	amount = forms.DecimalField(required=False, label='Cost', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cost',}))
	description = forms.CharField(required=False, label='Description', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',}))
	#Payment
	card = forms.IntegerField(label='Credit Card', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1234 5678 9012 3456'}))
	code = forms.IntegerField(label='Security Code', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '445'}))
	exp_month = forms.IntegerField(label='Expiration Month', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'MM'}))
	exp_year = forms.IntegerField(label='Expiration Year', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'YYYY'}))






	