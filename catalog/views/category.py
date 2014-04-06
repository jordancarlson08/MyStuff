from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from . import templater
from django.contrib.auth.decorators import login_required


def process_request(request):
	'''Shows the catalog items'''

	items = []
	category = ''
	subCategory = ''

	form = SearchForm()
	if request.method == 'GET':
		form = SearchForm(request.GET)
		if form.is_valid():
			search = form.cleaned_data['search']
			items = hmod.CatalogItem.objects.filter(manufacturer__icontains=search)
			if not items:
				items = hmod.CatalogItem.objects.filter(name__icontains=search)




	if request.urlparams[0] != '':
		category = hmod.Category.objects.get(id=request.urlparams[0])
		items = hmod.CatalogItem.objects.filter(category__category__id=request.urlparams[0])

	if request.urlparams[1] != '':
		subCategory = hmod.SubCategory.objects.get(id=request.urlparams[1])
		items = hmod.CatalogItem.objects.filter(category=request.urlparams[1])

	if request.urlparams[0] != '':
		if not items:
			message = "Sorry, it looks like there aren't any items here. Try another category!"
		else:
			message = ''
	else:
		if not items:
			message = "Welcome! Select a category from the menu on the left to get started."
		else:
			message = ''


	catItems = hmod.CatalogItem.objects.all()
	brands = hmod.CatalogItem.objects.distinct('manufacturer')
	category_list = hmod.Category.objects.all().order_by('id')

	if request.user.is_authenticated()==True:
		history= hmod.History.objects.filter(user=request.user).order_by('-last')
	else:
		history=''

	tvars = {

	'history':history,
	'category':category,
	'subCategory':subCategory,
	'message': message,
	'items': items,
	'category_list':category_list,
	'brands':brands,
	'catItems':catItems,
	'form':form,

	}

	return templater.render_to_response(request, 'category.html', tvars)



class SearchForm(forms.Form):
	search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search',}))








