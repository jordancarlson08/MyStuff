from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from django_summernote.widgets import SummernoteWidget
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the stores'''

	c = hmod.CatalogItem()
	form = CatalogItemForm()
	#form = StoreForm(empty_permitted=True)

	if request.method == 'POST':
		form = CatalogItemForm(request.POST)
		if form.is_valid():
			#time to save the data
			c.name = form.cleaned_data['name'] 
			c.manufacturer = form.cleaned_data['manufacturer'] 
			c.listPrice = form.cleaned_data['listPrice'] 
			c.cost = form.cleaned_data['cost']
			c.commissionRate = form.cleaned_data['commissionRate'] 
			c.description = form.cleaned_data['description'] 
			c.techSpecs = form.cleaned_data['techSpecs'] 
			c.sku = form.cleaned_data['sku'] 
			c.fillPoint = form.cleaned_data['fillPoint'] 
			c.leadTime = form.cleaned_data['leadTime'] 
			c.isRental = form.cleaned_data['isRental'] 
			c.pricePerDay = form.cleaned_data['pricePerDay'] 
			c.replacementFee = form.cleaned_data['replacementFee'] 
			c.lateFee = form.cleaned_data['lateFee'] 
			c.categoryID = form.cleaned_data['categoryID']
			c.createdBy = amod.Employee.objects.get(id=request.user.id)
			#c.createdBy = form.cleaned_data['Employee'] #### The manager that is currently logged in ####

			c.dateCreated = datetime.datetime.now().date() #Auto asigns todays date
						
			c.save()
			return HttpResponseRedirect('/manager/searchinventory/')


	tvars = {

	'form':form,

	}


	return templater.render_to_response(request, 'newcatalogitem.html', tvars)


class CatalogItemForm(forms.Form):
	'''A form for new stores'''
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name',}))
	manufacturer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manufacturer',}))
	categoryID = forms.ModelChoiceField(label='Category' ,queryset=hmod.Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
	listPrice = forms.DecimalField(label='List Price', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'List Price',}))
	cost = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cost',}))
	commissionRate = forms.DecimalField(label='Commission Rate', max_digits=2, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Commission Rate',}))
	#description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',}))
	#techSpecs = forms.CharField(label='Tech Specs', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Technical Specifications',}))

	#Special Rich Text Fields
	description = forms.CharField(widget=SummernoteWidget())
	techSpecs = forms.CharField(label='Tech Specs', widget=SummernoteWidget())

	sku = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU',}))
	fillPoint = forms.IntegerField(label='Fill Point', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fill Point',}))
	leadTime = forms.CharField(label='Avg. Lead Time', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lead Time ex. 2 Weeks',}))
	#NullBooleanSelect may not work, CheckboxInput does but it looks a little weird (https://docs.djangoproject.com/en/dev/ref/forms/widgets/#checkboxinput)
	#isRental = forms.BooleanField(label='Rentable Item?', widget=forms.NullBooleanSelect(attrs={'class': 'form-control',}))
	isRental = forms.BooleanField(label='Rentable Item?', widget=forms.CheckboxInput(), required=False)

	pricePerDay = forms.DecimalField(label='Price Per Day', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price Per Day',}))
	replacementFee = forms.DecimalField(label='Replacement Fee', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Replacement Fee',}))
	lateFee = forms.DecimalField(label='Late Fee', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Late Fee',}))

	#I want to auto add these fields not put them in the form...
	#dateCreated = forms.DateField(label='Date Created', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Created',}))
	#createdBy = forms.ForeignKey(Employee)
