from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as mmod
from account import models as amod
from . import templater
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Create a new catalog item'''

	
	form = CatalogItemForm()

	if request.method == 'POST':
		form = CatalogItemForm(request.POST, request.FILES)
		if form.is_valid():

			c = mmod.CatalogItem()

			c.name = form.cleaned_data['name'] 
			c.manufacturer = form.cleaned_data['manufacturer'] 
			c.listPrice = form.cleaned_data['listPrice'] 
			c.cost = form.cleaned_data['cost']
			c.commissionRate = form.cleaned_data['commissionRate'] 
			c.description = form.cleaned_data['description'] 
			c.techSpecs = form.cleaned_data['techSpecs'] 
			c.sku = form.cleaned_data['sku']
			c.createdBy = amod.Employee.objects.get(user_id=request.user.id)
			c.fillPoint = form.cleaned_data['fillPoint'] 
			c.leadTime = form.cleaned_data['leadTime'] 
			c.category = form.cleaned_data['category']
			c.isSerial = form.cleaned_data['isSerial']
			img = request.FILES.get('img', None)
			c.img = '/static/catalog/images/products/'+str(img)
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
	category = forms.ModelChoiceField(label='Category' ,queryset=mmod.SubCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
	listPrice = forms.DecimalField(label='List Price', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'List Price',}))
	cost = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cost',}))
	commissionRate = forms.DecimalField(label='Commission Rate', max_digits=2, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Commission Rate',}))
	description = forms.CharField(widget=SummernoteWidget()) #Special Rich Text Field
	techSpecs = forms.CharField(label='Tech Specs', widget=SummernoteWidget()) #Special Rich Text Field
	sku = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU',}))
	fillPoint = forms.IntegerField(label='Fill Point', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fill Point',}))
	leadTime = forms.CharField(label='Avg. Lead Time', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lead Time ex. 2 Weeks',}))
	isSerial = forms.BooleanField(label='Serial Numbers?', required=False )
	img = forms.ImageField(label='Select a image', help_text='max. 42 megabytes', required=False)