from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  
from account.models import User, Employee
from manager.models import CatalogItem, SerializedItem, Store
from decimal import *

class Shipping(models.Model):
	'''The available Shipping options'''
	name = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return '%s - $ %s' %(self.name, self.price)


class Transaction(models.Model):
  '''Describes the condition of an item'''
  created = models.DateField(auto_now=True)
  user = models.ForeignKey(User)
  store = models.ForeignKey(Store)
  subtotal = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
  tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  total =models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

  def __str__(self):
    return self.created

class Commission(models.Model):
	created = models.DateField(auto_now=True)


class Ledger(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name

class DebitCredit(models.Model):
	isDebit = models.BooleanField()
	amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
	ledger = models.ForeignKey(Ledger)

class JournalEntry(models.Model):
	created = models.DateField(auto_now=True)
	note = models.TextField()



#Classes to handle the cart more effectively
class CartItem(object):
	def __init__(self, catalogItem, qty):

		self.item = catalogItem
		self.qty = qty
		self.available= len(SerializedItem.objects.filter(catalogItem=catalogItem))

		if self.available < self.qty:
			self.error = "We are sorry, but we only have %s %s %s in stock at the moment. We have editted the quantity in your cart and will notify you when more become available. Thank You." %(len(SerializedItem.objects.filter(catalogItem=catalogItem)), catalogItem.manufacturer, catalogItem.name)
			self.extended= catalogItem.listPrice * int(len(SerializedItem.objects.filter(catalogItem=catalogItem)))
			self.qty = len(SerializedItem.objects.filter(catalogItem=catalogItem))
		else:
			self.error = ''
			self.extended= catalogItem.listPrice * qty


class Cart(object):
	def __init__(self, cartItem_list):
		self.cartItem_list = cartItem_list
		extend = []
		if self.cartItem_list:
			for c in cartItem_list:
				extend.append(c.extended)

		TWOPLACES = Decimal(10) ** -2

		tax_percent = Decimal(.07)
		extended_sum = (sum(extend)).quantize(TWOPLACES)
		tax = (tax_percent * sum(extend)).quantize(TWOPLACES)
		total = (tax + sum(extend)).quantize(TWOPLACES)

		self.extended_sum = extended_sum
		self.tax = tax
		self.total = total
