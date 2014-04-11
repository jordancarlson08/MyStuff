from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater


def process_request(request):

	stores = hmod.Store.objects.all().exclude(id=99999)
	
	tvars = {
	
    'stores': stores,
	
    }

	return templater.render_to_response(request, 'locations.html', tvars)