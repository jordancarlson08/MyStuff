from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account.models import *
from . import templater
from uuid import *
from datetime import *
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail

def process_request(request):
	'''Login Page'''

	form = ForgotForm()

	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			u = User.objects.get(username=form.cleaned_data['username'])
			email = u.email
			hours3 = datetime.now() + timedelta(hours=3)
			# Generate Code and Expiration
			u.passwordResetCode = uuid4()
			u.passwordResetExp = hours3
			u.save()

			url = 'http://localhost:8000/account/resetpassword/'+str(u.passwordResetCode)

			#HTML/TXT Email

			email= 'jordancarlson08@gmail.com' #TestingPurposes

			tvars = {'url':url}
			html_content = templater.render(request, 'email_forgot_password.html', tvars)
			subject, from_email= 'Reset Your Password', 'webmaster@digitallifemyway.com'
			text_content = 'Please use this link to reset your password %s, for security purposes this link will only be valid for the next 3 hours.' %(url)
			msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

			#Display confirmation page
			isSent=True
			tvars = {'isSent':isSent}
			return templater.render_to_response(request, 'logout.html', tvars)


	tvars = {

	'form':form,

	}

	return templater.render_to_response(request, 'forgotpassword.html', tvars)



class ForgotForm(forms.Form):
	'''Forgot Password Form'''
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))

	def clean(self):
		try:
			user = User.objects.get(username=self.cleaned_data['username'])
		except:
			user = None

		if user == None:
			raise forms.ValidationError("That user doesn't exist in our system")
		return self.cleaned_data
