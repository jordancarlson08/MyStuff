from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from manager.views.stores import StoreForm
from django.contrib.auth import authenticate, login

def process_request(request):
	'''Login Page'''


	form = ForgotForm()

	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			#time to save the data
			#return HttpResponseRedirect('/account/searchusers/')
			return


	tvars = {

	'form':form,

	}


	return templater.render_to_response(request, 'forgotpassword.html', tvars)



class ForgotForm(forms.Form):
	'''Login Form'''
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

	#I need to get this error to show up in my custom form. non_field_errors doesnt work
	def clean(self):
		user = amod.User.objects.get(email=self.cleaned_data['email'])
		if user == None:
			raise forms.ValidationError('Incorrect Username')
		return self.cleaned_data