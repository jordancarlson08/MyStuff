from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the inventory'''

	catItems = hmod.CatalogItem.objects.all()
	serial = hmod.SerializedItem.objects.exclude(isRental=True).order_by('catalogItem__id')
	rental = hmod.SerializedItem.objects.filter(isRental=True).order_by('catalogItem__id')

	tvars = {

	'catItems':catItems,
	'serial':serial,
	'rental':rental,

	}

	return templater.render_to_response(request, 'searchinventory.html', tvars)