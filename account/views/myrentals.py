from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the users repairs'''

	rentals = []
	t_list = Transaction.objects.filter(user=request.user)

	for t in t_list:
		r_list = t.revenue.all()
		for r in r_list:
			if r in Rental.objects.all():
				# rental = r
				# days = rental.dateDue - rental.dateOut
				# days = days.days
				rentals.append(r)

	rentals = Rental.objects.filter()

	tvars = {

	'rentals':rentals,

	}

	return templater.render_to_response(request, 'myrentals.html', tvars)