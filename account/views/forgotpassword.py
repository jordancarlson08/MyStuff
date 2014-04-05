from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account.models import *
from . import templater
from manager.views.stores import StoreForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from uuid import *
from datetime import *

def process_request(request):
	'''Login Page'''

	form = ForgotForm()

	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			u = User.objects.get(username=form.cleaned_data['username'])
			email = u.email
			hours3 = datetime.now() + timedelta(hours=3)
			#generate code and expiration date
			u.passwordResetCode = uuid4()
			u.passwordResetExp = hours3
			print(hours3)
			u.save()

			url = 'http://localhost:8000/account/resetpassword/'+str(u.passwordResetCode)

			send_mail('Reset your password', 'Please use this link to reset your password %s, you have until %s to reset your password' %(url ,hours3), 'webmaster@digitallifemyway.com',[email], fail_silently=False)

			return HttpResponseRedirect('/index/')


	tvars = {

	'form':form,

	}

	return templater.render_to_response(request, 'forgotpassword.html', tvars)



class ForgotForm(forms.Form):
	'''Login Form'''
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
