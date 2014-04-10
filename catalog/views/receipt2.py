from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from catalog.models import *
from account.models import *
from . import templater
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


def process_request(request):
	'''Shows the transaction receipt'''

	try:
		t = Transaction.objects.get(id=request.urlparams[0])
	except:
		return HttpResponseRedirect('/index')

	# Get basic Transaction info
	isWalkin = True
	if t.user.id != 99998:
		isWalkin=False

	sale=''
	sci_list=''
	ssi_list=''
	rental=''
	ri_list=''
	days=''
	rentalreturn=''
	ri_return_list=''
	repair=''

	# Gets a list of all revenue objects that are associated with the transaction
	revenue_list = t.revenue.all()
	for r in revenue_list:

		if r in Sale.objects.all():
			print("Sale")
			sale = r
			sci_list = SaleCatItem.objects.filter(sale=sale)
			ssi_list = SaleSerialItem.objects.filter(sale=sale)

		if r in Rental.objects.all():
			print("Rental")
			rental = r
			days = rental.dateDue - rental.dateOut
			days = days.days
			print(days)
			ri_list = RentalItem.objects.filter(rental=rental)

		if r in RentalReturn.objects.all():
			print("Rental Return")
			rentalreturn = r
			rental = rentalreturn.rental
			ri_return_list = RentalItem.objects.filter(rental=rental)

		if r in Repair.objects.all():
			print("Repair")
			repair = r

	showShip = False
	if rental=='' and rentalreturn=='' and repair=='' and isWalkin==False:
		showShip = True


	form = EmailReceiptForm()
	if request.method == 'POST':
		form = EmailReceiptForm(request.POST)
		if form.is_valid():
			print('valid')
			email = form.cleaned_data['email']

			send_mail('Receipt for transaction number %s' %(str(t.id)), 'This is your transaction: ', 'sales@digitallifemyway.com',
			[email], fail_silently=False)

			return HttpResponseRedirect('/index')

	tvars = {

	't':t,
	'sale':sale,
	'sci_list':sci_list,
	'ssi_list':ssi_list,
	'rental':rental,
	'ri_list':ri_list,
	'days':days,
	'rentalreturn':rentalreturn,
	'ri_return_list':ri_return_list,
	'repair':repair,
	'isWalkin':isWalkin,
	'showShip':showShip,
	'form':form,

	}

	return templater.render_to_response(request, 'email_receipt.html', tvars)

class EmailReceiptForm(forms.Form):
	email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address',}))
