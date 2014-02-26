from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from django.contrib.auth.decorators import login_required


def process_request(request):
	'''Shows the catalog items'''

	catItems = hmod.CatalogItem.objects.all()
	brands = hmod.CatalogItem.objects.distinct('manufacturer')
	tvars = {

	'brands':brands,
	'catItems':catItems,

	}

	return templater.render_to_response(request, 'search.html', tvars)


def process_request__results(request):
	#Determines if the filter is for ALL or a specific brand
	if request.urlparams[0] != 'All':
		catItems = hmod.CatalogItem.objects.filter(manufacturer=request.urlparams[0])
	elif request.urlparams[0] == 'All':
		catItems = hmod.CatalogItem.objects.all()

	tvars = {

	'catItems':catItems,

	}

	return templater.render_to_response(request, 'search_results.html', tvars)