from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from base_app.user_util import get_managers
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the stores'''

	if request.urlparams[1] == 'delete':
		s = hmod.Store.objects.get(id=request.urlparams[0])
		s.isActive = False
		s.save()
		return HttpResponseRedirect('/manager/searchstores/')


	s = hmod.Store.objects.get(id=request.urlparams[0])


	form = StoreForm(initial={
		'locationName': s.locationName,
		'street1': s.street1,
		'street2': s.street2,
		'city':s.city,
		'state':s.state,
		'zipCode':s.zipCode,
		'phone':s.phone,
		'manager':s.manager,
		})

	if request.method == 'POST':
		form = StoreForm(request.POST)
		if form.is_valid():
			#time to save the data
			s.locationName = form.cleaned_data['locationName']
			s.street1 = form.cleaned_data['street1']
			s.street2 = form.cleaned_data['street2']
			s.city = form.cleaned_data['city']
			s.state = form.cleaned_data['state']
			s.zipCode = form.cleaned_data['zipCode']
			s.phone = form.cleaned_data['phone']
			s.manager = form.cleaned_data['manager']
			s.save()

	urlStore = hmod.Store.objects.get(id=request.urlparams[0])

	items = hmod.SerializedItem.objects.filter(store=urlStore.id)
	itemcount = hmod.SerializedItem.objects.filter(store=urlStore.id).count()

	tvars = {
	'items':items,
	'form':form,
	'urlStore':urlStore,
	'itemcount':itemcount,
	}

	return templater.render_to_response(request, 'stores.html', tvars)


class StoreForm(forms.Form):
	'''A form for new stores'''
	locationName = forms.CharField(label = "Location Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Downtown Provo',}))
	street1 = forms.CharField(label = "Street 1", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	street2 = forms.CharField(label = "Street 2", required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	city = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	state = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	zipCode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))
	phone = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	manager = forms.ModelChoiceField(label='Manager', queryset=get_managers(), widget=forms.Select(attrs={'class': 'form-control'}))