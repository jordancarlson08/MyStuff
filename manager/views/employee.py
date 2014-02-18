from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from django.contrib.auth.decorators import login_required

@login_required
def process_request(request):
	'''Shows the stores'''

	if request.urlparams[1] == 'delete':
		u = amod.User.objects.get(id=request.urlparams[0])
		u.is_active = False
		u.save()
		return HttpResponseRedirect('/manager/searchusers/')

	u = amod.User.objects.get(id=request.urlparams[0])
	e = amod.Employee.objects.get(id=request.urlparams[0])
	user = u

	if u.is_active == False:
		return Http404()


	form = UserForm(initial={
		'username' : u.username,
		'first_name' : u.first_name,
		'last_name' : u.last_name,
		'email' : u.email,
		'phone' : u.phone,
		'security_question' : u.security_question,
		'security_answer' : u.security_answer,
		'is_staff' : u.is_staff,
		'street1' : u.street1,
		'street2' : u.street2,
		'city' : u.city,
		'state' : u.state,
		'zipCode' : u.zipCode,
		'hireDate':e.hireDate,
		'salary':e.salary,
		})

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			#time to save the data
			u.username = form.cleaned_data['username']
			# u.set_password(form.cleaned_data['password'])
			u.first_name = form.cleaned_data['first_name']
			u.last_name = form.cleaned_data['last_name']
			u.email = form.cleaned_data['email']
			u.phone = form.cleaned_data['phone']
			u.security_question = form.cleaned_data['security_question']
			u.security_answer = form.cleaned_data['security_answer']	
			u.is_staff = form.cleaned_data['is_staff'] 
			u.street1 = form.cleaned_data['street1']
			u.street2 = form.cleaned_data['street2']
			u.city = form.cleaned_data['city']
			u.state = form.cleaned_data['state']
			u.zipCode = form.cleaned_data['zipCode']
			u.save()
			e.hireDate = form.cleaned_data['hireDate']
			e.salary = form.cleaned_data['salary']
			e.save()

	passwordForm = UserPasswordForm()

	if request.method == 'POST':
		passwordForm = UserPasswordForm(request.POST)
		if passwordForm.is_valid():
			#time to save the data
			if u.check_password(passwordForm.cleaned_data['password']):
				if passwordForm.cleaned_data['newpassword1'] == passwordForm.cleaned_data['newpassword2']:
					u.set_password(passwordForm.cleaned_data['newpassword1'])
					u.save()


	tvars = {
	'user':user,
	'form':form,
	'passwordForm':passwordForm,
	}
 	
	return templater.render_to_response(request, 'employee.html', tvars)

class UserForm(forms.Form):
	
	username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',}))
	#password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
	last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
	email = forms.CharField(max_length=25, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'me@example.com',}))
	phone = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	security_question = forms.CharField(label='Security Question', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your mother\'s maiden name?',}))
	security_answer = forms.CharField(label='Answer', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smith',}))	
	is_staff = forms.BooleanField(label='Employee?', widget=forms.CheckboxInput(), required=False, )
	street1 = forms.CharField(label = "Street 1", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	street2 = forms.CharField(label = "Street 2", required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	city = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	state = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	zipCode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))
	hireDate = forms.DateField(label='Hire Date', widget=forms.DateInput(attrs={'class': 'form-control'}))
	salary= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))

class UserPasswordForm(forms.Form):
	password = forms.CharField(label='Current Password', max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	newpassword1 = forms.CharField(label='New Password',max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	newpassword2 = forms.CharField(label='Repeat Password',max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))

	def clean(self):
	    if (self.cleaned_data.get('newpassword1') !=
	        self.cleaned_data.get('newpassword2')):

	        raise forms.ValidationError("New password does not match.")

	    return self.cleaned_data