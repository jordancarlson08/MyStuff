from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(employee_check)
def process_request(request):
	'''Shows the inventory'''

	catItems = hmod.CatalogItem.objects.all()
	serial = hmod.SerializedItem.objects.exclude(isRental=True).order_by('catalogItem__id').exclude(isSold=True)
	rental = hmod.SerializedItem.objects.filter(isRental=True).order_by('isRented').order_by('catalogItem__id').exclude(isRented=True)

	tvars = {

	'catItems':catItems,
	'serial':serial,
	'rental':rental,

	}

	return templater.render_to_response(request, 'searchinventory.html', tvars)