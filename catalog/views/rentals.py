from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from manager import models as hmod
from . import templater
from django.contrib.auth.decorators import login_required
import operator


def process_request(request):
	'''Shows the rental items'''

	items = []
	category = ''
	subCategory = ''
	history=''

	rental_ids = []
	all_rentals = hmod.SerializedItem.objects.filter(isRental=True)
	for a in all_rentals:
		rental_ids.append(a.catalogItem.id)

	form = SearchForm()
	print(rental_ids)

	items = hmod.CatalogItem.objects.filter(id__in=rental_ids)

	if not items:
		message = "Sorry, it looks like there aren't any items here. Try another category!"
	else:
		message = ''
	

	category_list = hmod.Category.objects.all().order_by('id')

	tvars = {

	'history':history,
	'category':category,
	'subCategory':subCategory,
	'message': message,
	'items': items,
	'category_list':category_list,
	'form':form,

	}

	return templater.render_to_response(request, 'rentals.html', tvars)



class SearchForm(forms.Form):
	search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search',}))








