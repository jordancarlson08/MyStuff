from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account.models import *
from . import templater
from uuid import *
from datetime import *
from django.utils import timezone
from django.utils.timezone import localtime

def process_request(request):
	'''Login Page'''

	error = None

	try:
		u = User.objects.get(passwordResetCode= request.urlparams[0])
		form = ResetForm()
		if request.method == 'POST':
			form = ResetForm(request.POST)
			if form.is_valid():
				#time to save the data
				normalizedExp = localtime(u.passwordResetExp)
				normalizedNow = localtime(timezone.now())
				if normalizedExp > normalizedNow:
					#reset the password
					u.set_password(form.cleaned_data['password1'])
					u.passwordResetCode = ''
				else:
					#Throw error
					error = 'We are sorry for the inconvenience, but this link is invalid or expired. Please go to our "Forgot Password" page to generate a new link.'

				u.save()

				return HttpResponseRedirect('/index/')

	except User.DoesNotExist:
		form = ResetForm()
		error = 'We are sorry for the inconvenience, but this link is invalid or expired. Please go to our "Forgot Password" page to generate a new link.'
		tvars = {
		'form':form,
		'error':error,
		}
		return templater.render_to_response(request, 'resetpassword.html', tvars)


	tvars = {

	'form':form,
	'error':error,

	}

	return templater.render_to_response(request, 'resetpassword.html', tvars)


class ResetForm(forms.Form):
	'''Login Form'''
	password1 = forms.CharField(label='Enter New Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
	password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

	def clean(self):
	    if (self.cleaned_data['password1'] != self.cleaned_data['password2']):
	        raise forms.ValidationError("New password does not match.")
	    return self.cleaned_data
