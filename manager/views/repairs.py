from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from . import templater
from django.contrib.auth.decorators import login_required
from datetime import *
from django.core.mail import send_mail

@login_required
def process_request(request):
	'''Shows the users repairs'''

	repairs = Repair.objects.filter(isOpen=True)

	tvars = {

	'repairs':repairs,

	}

	return templater.render_to_response(request, 'repairs.html', tvars)


@login_required
def process_request__complete(request):
	'''Shows the users repairs'''

	r = Repair.objects.get(id=request.urlparams[0])
	r.dateComplete = datetime.now()
	r.save()



@login_required
def process_request__email(request):

	repairs = Repair.objects.filter(isOpen=True)
	for r in repairs:
		if(r.dateComplete!=''):
			send_mail(
				'Repair Complete', #Subject
				'Your %s is ready for pickup!' %(r.itemName), #Body
				'repairs@digitallifemyway.com', #From
				['jordancarlson08@gmail.com'],  #To u.email
				fail_silently=False
				)

	return HttpResponseRedirect('/index/mailsent')