from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the stores'''

	s = hmod.SerializedItem()
	form = SerializedItemForm()
	#form = SerializedItemForm(empty_permitted=True)

	if request.method == 'POST':
		form = SerializedItemForm(request.POST)
		if form.is_valid():
			#time to save the data
			s.storeID = form.cleaned_data['storeID']
			s.catalogItem = form.cleaned_data['catalogItem']
			s.listPrice = form.cleaned_data['listPrice']
			s.cost = form.cleaned_data['cost']
			s.commissionRate = form.cleaned_data['commissionRate']
			s.serialNum = form.cleaned_data['serialNum']
			s.shelfLocation = form.cleaned_data['shelfLocation']
			s.conditionID = form.cleaned_data['conditionID']
			s.conditionDetails = form.cleaned_data['conditionDetails']
			s.isRental = form.cleaned_data['isRental']
			s.dateReceived = form.cleaned_data['dateReceived']
			s.dateCreated = datetime.datetime.now().date() #Automaticlly asignned todays date
			s.createdBy = amod.Employee.objects.get(id=request.user.id)
			s.save()
			return HttpResponseRedirect('/manager/searchinventory/')



	tvars = {

	'form':form,

	}


	return templater.render_to_response(request, 'newinventoryitem.html', tvars)

class SerializedItemForm(forms.Form):
	'''A form for new serialized item'''
	storeID = forms.ModelChoiceField(label='Store', queryset=hmod.Store.objects.filter(isActive="TRUE").order_by('locationName'), widget=forms.Select(attrs={'class': 'form-control',}))
	catalogItem = forms.ModelChoiceField(label='Catalog Item', queryset=hmod.CatalogItem.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
	listPrice = forms.DecimalField(label='List Price', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'List Price',}))
	cost = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cost',}))
	commissionRate = forms.DecimalField(label='Commission Rate', max_digits=2, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Commission Rate',}))
	serialNum = forms.CharField(label='Serial Number',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serial Number',}))
	shelfLocation = forms.CharField(label='Shelf Location', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shelf Location',}))
	conditionID = forms.ModelChoiceField( label='Condition', queryset=hmod.Condition.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
	conditionDetails = forms.CharField(required=False, label='Condition Details', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Condition Details',}))
	isRental = forms.BooleanField(label='Rentable Item?', required=False )
	dateReceived = forms.DateField(label='Date Received', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Received',}))

	#add these automaticly
	#dateCreated = forms.DateField()
	#createdBy = forms.ForeignKey(Employee)
