from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the catalog items'''

	catItems = hmod.CatalogItem.objects.all()
	rental = hmod.SerializedItem.objects.filter(isRental=True)

	tvars = {

	'catItems':catItems,
	'rental':rental,

	}

	return templater.render_to_response(request, 'searchinventory.html', tvars)