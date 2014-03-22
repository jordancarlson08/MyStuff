from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from account.views.login import LoginForm
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
			        return HttpResponseRedirect(request.GET['next'])
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


