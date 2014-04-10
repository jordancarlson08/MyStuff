from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import *
from account.models import *
from catalog.models import *
from . import templater
from datetime import *
from django.core.mail import send_mail
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''Shows the commissions for a user'''

	form = CommissionsForm()


	c_list = Commission.objects.all()

	tvars = {

	'form':form,

	}

	return templater.render_to_response(request, 'commissions.html', tvars)

@login_required
@user_passes_test(manager_check)
def process_request__get(request):
	'''Shows the commissions for a user'''



	c_list = Commission.objects.filter(transaction__employee__id=request.urlparams[0])

	tvars = {

	'c_list':c_list,

	}

	return templater.render_to_response(request, 'commissions_list.html', tvars)




class CommissionsForm(forms.Form):
	'''A form for new stores'''	
	emp = forms.ModelChoiceField(label='Employee' ,queryset=get_employees(), widget=forms.Select(attrs={'class': 'form-control', 'id':'emp'}))


