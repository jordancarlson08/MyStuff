from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from catalog.models import *
from . import templater
from django.contrib.auth.decorators import login_required
from datetime import *

@login_required
def process_request(request):
	'''Records Damage and Late Fees'''

	if (request.urlparams[1] == 'late'):
		r = Rental.objects.get(id=request.urlparams[0])
		daysLate = date.today() - r.dateDue
		daysLate = daysLate.days
		r_items = RentalItem.objects.filter(rental=r)
		rental_fee_list=[]
		for i in r_items:
			rental_fee_list.append(i.item.lateFee * daysLate)
		sum_fees = sum(rental_fee_list)
		form = FeeForm(initial={
			'lateFee': sum_fees,
			})
	else:
		form = FeeForm()

	if request.method == 'POST':
		form = FeeForm(request.POST)
		if form.is_valid():
			a = ''
			b = ''
			if (request.urlparams[1] == 'late'):
				lf = Late()
				lf.daysLate = daysLate
				lf.waived = form.cleaned_data['waiveLateFee']
				if (lf.waived == True):
					lf.amount = 0
				else:
					lf.amount = form.cleaned_data['lateFee']
				lf.save()
				b = lf.id

			df = Damage()
			df.description = form.cleaned_data['description']
			df.waived = form.cleaned_data['waiveDamageFee']
			if (df.waived == True):
				df.amount = 0
			else:
				df.amount = form.cleaned_data['damageFee']
			df.save()
			a = df.id 

			params = '%s/%s' %(a, b)
			url = '/catalog/checkout/' +str(params)
			return HttpResponseRedirect(url) 

	tvars = {

	'form':form,
	'late':request.urlparams[1],

	}

	return templater.render_to_response(request, 'fees.html', tvars)


class FeeForm(forms.Form):
	'''The form used for damage and late fees'''
	lateFee = forms.DecimalField(required=False, label='Late Fee', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Late Fee',}))
	waiveLateFee = forms.BooleanField(required=False, label='Waive Late Fee')
	damageFee = forms.DecimalField(label='Damage Fee', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Damage Fee',}))
	waiveDamageFee = forms.BooleanField(required=False, label='Waive Damage Fee')
	description = forms.CharField(required=False, label='Damage Description', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Condition Details',}))


		### Use in checkout.py ###
			# rr = RentalReturn()
			# rr.rental = t.rental
			# rr.dateIn = date.today()
			# rr.fee
			# rr.save()