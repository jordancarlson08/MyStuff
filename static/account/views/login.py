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



	form = LoginForm()
	if request.method =='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], 
				password=form.cleaned_data['password'])
			if user is not None:
			    if user.is_active:
			        login(request, user)
			        if form.cleaned_data['remember'] == True:
			        	# The user is logged out after 'x' seconds
			        	request.session.set_expiry(300)
			        else:
			        	# The user is logged out upon closing the browser
			        	request.session.set_expiry(0)
			        # Redirect to a success page.
			        return HttpResponseRedirect('/')
			    else:
			        # Return a 'disabled account' error message
			        return HttpResponseRedirect('/manager/searchinventory/')
			else:
			    # Return an 'invalid login' error message.
			    return HttpResponseRedirect('/manager/searchstores/')



	tvars = {

	'form':form,

	}


	return templater.render_to_response(request, 'login.html', tvars)



class LoginForm(forms.Form):
	'''Login Form'''
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
	password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
	remember = forms.BooleanField(required = False, label='Remember me', widget=forms.CheckboxInput())

	#I need to get this error to show up in my custom form. non_field_errors doesnt work
	def clean(self):
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		if user == None:
			raise forms.ValidationError('Incorrect Username or Password')
		return self.cleaned_data