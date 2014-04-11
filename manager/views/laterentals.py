from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from catalog.models import *
from . import templater
from datetime import *
from django.core.mail import send_mail
from base_app.user_util import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(manager_check)
def process_request(request):
	'''Shows the late rentals'''

	rental30_info_list=[]
	rental60_info_list=[]
	rental90_info_list=[]
	thirty_days_late = date.today() - timedelta(days=30)
	sixty_days_late = date.today() - timedelta(days=60)
	ninty_days_late = date.today() - timedelta(days=90)
	rental_list_30 = Rental.objects.filter(dateDue__lte = thirty_days_late).filter(dateDue__gte = sixty_days_late)
	rental_list_60 = Rental.objects.filter(dateDue__lte = sixty_days_late).filter(dateDue__gte = ninty_days_late)
	rental_list_90 = Rental.objects.filter(dateDue__lte = ninty_days_late)

	for r in rental_list_30:
		ri = RentalItem.objects.filter(rental=r)
		t = Transaction.objects.get(revenue=r)
		u = t.user
		for x in ri:
			i = x.item
			info = RentalInfo(i, r, t, u)
			rental30_info_list.append(info)

	for r in rental_list_60:
		ri = RentalItem.objects.filter(rental=r)
		t = Transaction.objects.get(revenue=r)
		u = t.user
		for x in ri:
			i = x.item
			info = RentalInfo(i, r, t, u)
			rental60_info_list.append(info)

	for r in rental_list_90:
		ri = RentalItem.objects.filter(rental=r)
		t = Transaction.objects.get(revenue=r)
		u = t.user
		for x in ri:
			i = x.item
			info = RentalInfo(i, r, t, u)
			rental90_info_list.append(info)


	tvars = {

	'rental30_info_list':rental30_info_list,
	'rental60_info_list':rental60_info_list,
	'rental90_info_list':rental90_info_list,

	}

	return templater.render_to_response(request, 'laterentals.html', tvars)

class RentalInfo(object):
	'''Rental Info'''
	def __init__(self, item, rental, transaction, user):
		'''Constructor'''
		self.item = item
		self.rental = rental
		self.transaction = transaction
		self.user = user
		self.isLate = False
		self.daysLate = (date.today() - rental.dateDue).days
		if (rental.dateDue < date.today()):
			self.isLate = True

	def __str__(self):
		return '%s %s: Out: %s Due: %s' %(self.item.manufacturer, self.item.name, self.rental.dateOut, self.rental.dateDue)


@login_required
def process_request__email(request):

	rental_list = Rental.objects.filter(dateDue__lt = date.today())
	for r in rental_list:
		ri = RentalItem.objects.filter(rental=r)
		t = Transaction.objects.get(revenue=r)
		u = t.user
		for x in ri:
			i = x.item
			info = RentalInfo(i, r, t, u)

			#HTML/TXT Email
			
			email = u.email
			url = 'http://www.digitallifemyway.com/locations/'
			tvars = {'url':url}
			html_content = templater.render(request, 'email_late.html', tvars)
			subject, from_email= 'Reset Your Password', 'webmaster@digitallifemyway.com'
			text_content = 'Please use this link to reset your password %s, for security purposes this link will only be valid for the next 3 hours.' %(url)
			msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

			send_mail(
				'Outstanding Rental', #Subject
				'The %s %s you rented was due %s days ago! Please return the item as soon as possible to avoid additional late penalties.' %(i.catalogItem.manufacturer, i.catalogItem.name, info.daysLate), #Body
				'rentals@digitallifemyway.com', #From
				['jordancarlson08@gmail.com'],  #To u.email
				fail_silently=False
				)


	return HttpResponseRedirect('/index/mailsent')