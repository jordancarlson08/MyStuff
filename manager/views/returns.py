from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from catalog.models import *
from . import templater
from datetime import *
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(employee_check)
def process_request(request):
	'''Shows the open rentals'''

	#FixLater -- Make the date due yellow if its almost due!

	rentalInfo_list=[]

	rentalItems_list = SerializedItem.objects.filter(isActive=True).filter(isRented=True)
	for i in rentalItems_list:
		rentalItem = RentalItem.objects.filter(item=i)
		for r in rentalItem:
			rental = r.rental
			trans_list = Transaction.objects.filter(revenue=rental)
			for t in trans_list:
				user = t.user
				ri = RentalInfo(i, rental, t, user)
				rentalInfo_list.append(ri)

	tvars = {

	'rentalInfo_list':rentalInfo_list,

	}

	return templater.render_to_response(request, 'returns.html', tvars)


class RentalInfo(object):
	'''Rental Info'''
	def __init__(self, item, rental, transaction, user):
		'''Constructor'''
		self.item = item
		self.rental = rental
		self.transaction = transaction
		self.user = user
		self.isLate = False
		if (rental.dateDue < date.today()):
			self.isLate = True

	def __str__(self): #FixLater
		return '%s %s: Out: %s Due: %s' %(self.item.manufacturer, self.item.name, self.rental.dateOut, self.rental.dateDue)
