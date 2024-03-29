from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account.models import *
from account.views.login import *
from django.contrib.auth import authenticate, login
from . import templater
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail



def process_request(request):
	'''New User Page'''

	u = User()
	form = UserForm()

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			#time to save the data
			u.username = form.cleaned_data['username']
			u.set_password(form.cleaned_data['password'])
			u.first_name = form.cleaned_data['first_name']
			u.last_name = form.cleaned_data['last_name']
			u.email = form.cleaned_data['email']
			u.phone = form.cleaned_data['phone']
			# u.security_question = form.cleaned_data['security_question']
			# u.security_answer = form.cleaned_data['security_answer']
			u.street1 = form.cleaned_data['street1']
			u.street2 = form.cleaned_data['street2']
			u.city = form.cleaned_data['city']
			u.state = form.cleaned_data['state']
			u.zipCode = form.cleaned_data['zipCode']
			u.is_staff = False
			u.save()

			#Welcome Email
			#HTML/TXT Email
			
			email = u.email

			tvars = {}
			html_content = templater.render(request, 'email_welcome.html', tvars)
			subject, from_email= 'Welcome to Digital Life My Way', 'webmaster@digitallifemyway.com'
			text_content = 'Welcome to Digital Life My Way'
			msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()


			user = authenticate(username=form.cleaned_data['username'], 
				password=form.cleaned_data['password'])
			if user is not None:
			    if user.is_active:
			        login(request, user)
			        #converts session to database -- see below
			        add_history_to_database(request, user)

			        request.session.set_expiry(0)
			        # Redirect to a success page.

			        return HttpResponse('<script> window.location.href="/index/";</script>')


			    else:
			        # Return a 'disabled account' error message
			        return HttpResponseRedirect('/manager/searchinventory/')
			else:
			    # Return an 'invalid login' error message.
			    return HttpResponseRedirect('/manager/searchstores/')



	tvars = {


	'form':form,

	}


	return templater.render_to_response(request, 'newuser.html', tvars)

class UserForm(forms.Form):
	
	username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',}))
	password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
	email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'me@example.com',}))
	phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	# security_question = forms.CharField(label='Security Question', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your mother\'s maiden name?',}))
	# security_answer = forms.CharField(label='Answer', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smith',}))	
	street1 = forms.CharField(label = "Street 1", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	street2 = forms.CharField(label = "Street 2", required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	state = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	zipCode = forms.IntegerField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))
	

	def clean_username(self):
	   username = self.cleaned_data.get('username')
	   if username and User.objects.filter(username=username).count() > 0:
	       raise forms.ValidationError('This username is already registered.')
	   return username