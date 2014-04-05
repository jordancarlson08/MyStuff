from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from account.admin import manager_check
from django.contrib.auth.decorators import login_required, user_passes_test



@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''New Employee Page'''

	u = amod.User()
	e = amod.Employee()
	
	form = UserForm()
	#form = StoreForm(empty_permitted=True)

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
			u.security_question = form.cleaned_data['security_question']
			u.security_answer = form.cleaned_data['security_answer']
			u.is_staff = form.cleaned_data['is_staff']
			u.street1 = form.cleaned_data['street1']
			u.street2 = form.cleaned_data['street2']
			u.city = form.cleaned_data['city']
			u.state = form.cleaned_data['state']
			u.zipCode = form.cleaned_data['zipCode']
			u.save()
			e.user = u
			e.hireDate = form.cleaned_data['hireDate']
			e.salary = form.cleaned_data['salary']
			# e.store = form.cleaned_data['store']
			e.save()
			return HttpResponseRedirect('/manager/searchusers/')


	tvars = {

	'form':form,

	}


	return templater.render_to_response(request, 'newemployee.html', tvars)

class UserForm(forms.Form):
	
	username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',}))
	password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}))
	email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'me@example.com',}))
	phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '801-555-1234',}))
	security_question = forms.CharField(label='Security Question', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your mother\'s maiden name?',}))
	security_answer = forms.CharField(label='Answer', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smith',}))	
	is_staff = forms.BooleanField(label='Manager?', widget=forms.CheckboxInput(), required=False, )
	street1 = forms.CharField(label = "Street 1", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Center St.',}))
	street2 = forms.CharField(label = "Street 2", required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#242',}))
	city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provo',}))
	state = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UT',}))
	zipCode = forms.IntegerField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '84601',}))
	hireDate = forms.DateField(label='Hire Date', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Hire Date',}))
	salary= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Salary',}))
	# store = forms.ModelChoiceField(label='Store', queryset=hmod.Store.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))

	def clean_username(self):
	   username = self.cleaned_data.get('username')
	   if username and amod.User.objects.filter(username=username).count() > 0:
	       raise forms.ValidationError('This username is already registered.')
	   return username