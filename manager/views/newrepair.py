from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from account.models import *
from catalog.models import *
from . import templater
from django_summernote.widgets import SummernoteWidget
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(employee_check)
def process_request(request):
	'''Create a new Repair'''

	form = RepairForm()
	if request.method == 'POST':
		form = RepairForm(request.POST)
		if form.is_valid():

			r = Repair()
			r.user = form.cleaned_data['user']
			r.itemName = form.cleaned_data['itemName']
			r.description = form.cleaned_data['description']
			r.estComplete = form.cleaned_data['estComplete']
			r.estCost = form.cleaned_data['estCost']
			r.status = form.cleaned_data['status']
			r.save()

			email = r.user.email
			url = 'http://www.digitallifemyway.com/account/myrepairs/'

			tvars= { 'r': r, 'url':url,  }
			html_content = templater.render(request, 'email_repair.html', tvars)
			subject, from_email= 'Repair Request', 'webmaster@digitallifemyway.com'
			text_content = 'Thank you for your request to repair your %s. We will let you know as soon as we are finished fixing it up.' %(r.itemName)
			msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

			return HttpResponseRedirect('/index/')

	tvars = {
		'form':form,
	}

	return templater.render_to_response(request, 'newrepair.html', tvars)


class RepairForm(forms.Form):
	'''A form for new Repairs'''
	user = forms.ModelChoiceField(label='User', queryset=get_users_only(), widget=forms.Select(attrs={'class': 'form-control',}))
	itemName = forms.CharField(label='Item Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name',}))
	description = forms.CharField(widget=SummernoteWidget()) #Special Rich Text Field
	estComplete = forms.DateField(label='Est. Complete Date', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Est. Complete Date',}))
	estCost = forms.DecimalField(label='Est. Cost', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Est. Cost',}))
	status = forms.CharField(label='Status', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status',}))

	# dateComplete = forms.DateField(label='Hire Date', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Hire Date',}))
	# hours = forms.DecimalField(label='List Price', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'List Price',}))
	# datePickup = forms.DateField(label='Hire Date', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Hire Date',}))
	# amount = forms.DecimalField(label='List Price', max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'List Price',}))
