from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from account.admin import user_check, my_account
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@my_account
#Need other test to only allow user x to access his own account page
def process_request(request):
	'''Shows the specific user'''

	if request.urlparams[1] == 'delete':
		u = amod.User.objects.get(id=request.urlparams[0])
		u.is_active = False
		u.save()
		return HttpResponseRedirect('/manager/searchusers/')

	user = amod.User.objects.get(id=request.urlparams[0])


	if user.is_active == False:
		return Http404()


	tvars = {
	'user':user,
	}
 	
	return templater.render_to_response(request, 'user.html', tvars)






def process_request__edit(request):
	'''Edit the user'''

	user = amod.User.objects.get(id=request.urlparams[0])
	c = ''


	if user.is_active == False:
		return Http404()


	form = UserForm(initial={
		'username' : user.username,
		'first_name' : user.first_name,
		'last_name' : user.last_name,
		'email' : user.email,
		'phone' : user.phone,
		'security_question' : user.security_question,
		'security_answer' : user.security_answer,
		'street1' : user.street1,
		'street2' : user.street2,
		'city' : user.city,
		'state' : user.state,
		'zipCode' : user.zipCode,
		})

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			#time to save the data
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.phone = form.cleaned_data['phone']
			user.security_question = form.cleaned_data['security_question']
			user.security_answer = form.cleaned_data['security_answer']	
			user.is_staff = False
			user.street1 = form.cleaned_data['street1']
			user.street2 = form.cleaned_data['street2']
			user.city = form.cleaned_data['city']
			user.state = form.cleaned_data['state']
			user.zipCode = form.cleaned_data['zipCode']
			user.save()
			c = 'Changes Saved'
			#return HttpResponse('<script> setTimeout(function() {window.location.href = "/index/";}, 2000);</script>')


	
	tvars = {
	'user':user,
	'form':form,
	'c':c,
	}
 	
	return templater.render_to_response(request, 'edit_user.html', tvars)



def process_request__password(request):
	'''Edit the password'''

	user = amod.User.objects.get(id=request.urlparams[0])
	c = ''

	if user.is_active == False:
		return Http404()


	passwordForm = UserPasswordForm()

	if request.method == 'POST':
		passwordForm = UserPasswordForm(request.POST)
		if passwordForm.is_valid():
			#time to save the data
			if user.check_password(passwordForm.cleaned_data['password']):
				if passwordForm.cleaned_data['newpassword1'] == passwordForm.cleaned_data['newpassword2']:
					user.set_password(passwordForm.cleaned_data['newpassword1'])
					user.save()
					c = 'Changes Saved'
					#return HttpResponse('<meta http-equiv="refresh" content="2;url=/index/">')


	tvars = {
	'user':user,
	'passwordForm':passwordForm,
	'c':c,
	}
		
	return templater.render_to_response(request, 'edit_password.html', tvars)





class UserForm(forms.Form):
	
	username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',}))
	#password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
	last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
	email = forms.CharField(max_length=25, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'me@example.com',}))
	phone = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	security_question = forms.CharField(label='Security Question', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your mother\'s maiden name?',}))
	security_answer = forms.CharField(label='Answer', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smith',}))	
	street1 = forms.CharField(label = "Street 1", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	street2 = forms.CharField(label = "Street 2", required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	city = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	state = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	zipCode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))


class UserPasswordForm(forms.Form):
	password = forms.CharField(label='Current Password', max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	newpassword1 = forms.CharField(label='New Password',max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	newpassword2 = forms.CharField(label='Repeat Password',max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))

	def clean(self):
	    if (self.cleaned_data.get('newpassword1') !=
	        self.cleaned_data.get('newpassword2')):

	        raise forms.ValidationError("New password does not match.")

	    return self.cleaned_data

	# def clean_password(self):
		# I need to get the user some how so i can run the check_password
		# check_password(passwordForm.cleaned_data['password'])