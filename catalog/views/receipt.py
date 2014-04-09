from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from catalog.models import *
from account.models import *
from . import templater
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
	rental=''
	rentalreturn=''
	repair=''

	# Gets a list of all revenue objects that are associated with the transaction
	revenue_list = t.revenue.all()
	for r in revenue_list:

		if r in Sale.objects.all():
			print("Sale")
			sale = r

		if r in Rental.objects.all():
			print("Rental")
			rental = r

		if r in RentalReturn.objects.all():
			print("Rental Return")
			rentalreturn = r

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
			###SEND MAIL HERE!!!!
			return HttpResponseRedirect('/index')

	tvars = {

	't':t,
	'sale':sale,
	'rental':rental,
	'rentalreturn':rentalreturn,
	'repair':repair,
	'isWalkin':isWalkin,
	'showShip':showShip,
	'form':form,

	}

	return templater.render_to_response(request, 'receipt.html', tvars)

class EmailReceiptForm(forms.Form):
	email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address',}))
