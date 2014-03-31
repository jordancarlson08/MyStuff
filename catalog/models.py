from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  
from account.models import User, Employee
from manager.models import CatalogItem, SerializedItem, Store
from decimal import *
from polymorphic import PolymorphicModel



class Revenue(PolymorphicModel):
	'''Class for Revenue sorce'''
	amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

class Sale(Revenue):
	'''Class revenue from sale of goods'''
	#amount: DecimalField
	created = models.DateField(auto_now=True)

class SaleCatItem(models.Model):
	sale = models.ForeignKey(Sale)
	item = models.ForeignKey(CatalogItem)
	qty = models.IntegerField()

class SaleSerialItem(models.Model):
	sale = models.ForeignKey(Sale)
	item = models.ForeignKey(SerializedItem)
	qty = 1

class Repair(Revenue):
	'''Class for repairs'''
	#amount: DecimalField
	dateStart = models.DateField()
	dateComplete = models.DateField()
	description = models.TextField()
	hours = models.DecimalField(max_digits=16, decimal_places=2)
	datePickup = models.DateField()

class Rental(Revenue):
	'''Class for rentals'''
	#amount: DecimalField
	dateOut = models.DateField()
	dateDue = models.DateField()
	dateIn = models.DateField()
	item = models.ForeignKey(SerializedItem)

class Fee(PolymorphicModel):
	'''Class for fees'''
	amount = models.DecimalField(max_digits=16, decimal_places=2)
	waived = models.BooleanField()

class Late(Fee):
	'''Class for late fee'''
	daysLate = models.DecimalField(max_digits=16, decimal_places=2)

class Damage(Fee):
	'''Class for damage fee'''
	description = models.TextField()


class Shipping(models.Model):
	'''The available Shipping options'''
	name = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return '%s - $ %s' %(self.name, self.price)


class Transaction(models.Model):
  '''Describes the condition of an item'''
  created = models.DateField(auto_now=True)
  revenue = models.ManyToManyField(Revenue)
  user = models.ForeignKey(User)
  store = models.ForeignKey(Store)
  employee = models.ForeignKey(Employee)
  subtotal = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
  tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  total =models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
  paymentType = models.TextField()


# class Payment(models.Model):
# 	'''Class for payments'''
# 	amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
	


class Commission(models.Model):
	'''Class for commissions'''
	created = models.DateField(auto_now=True)


class Ledger(models.Model):
	'''Class for the different accounting ledgers'''
	name = models.TextField()

	def __str__(self):
		return self.name

class AccountEntry(models.Model):
	'''Class for accounting entries'''
	isDebit = models.BooleanField()
	amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
	ledger = models.ForeignKey(Ledger)

class JournalEntry(models.Model):
	'''Class for Journal Entries'''
	created = models.DateField(auto_now=True)
	note = models.TextField()



#Classes to handle the cart more effectively
class RentalCartItem(object):
	def __init__(self, serializedItem):

		self.item = serializedItem


#Classes to handle the cart more effectively
class CartItem(object):
	def __init__(self, catalogItem, qty):

		self.item = catalogItem
		self.qty = qty

		if catalogItem.isSerial == True:
			self.available= len(SerializedItem.objects.filter(catalogItem=catalogItem))

			if self.available < self.qty:
				self.error = "We are sorry, but we only have %s %s %s in stock at the moment. We have editted the quantity in your cart and will notify you when more become available. Thank You." %(len(SerializedItem.objects.filter(catalogItem=catalogItem)), catalogItem.manufacturer, catalogItem.name)
				self.extended= catalogItem.listPrice * int(len(SerializedItem.objects.filter(catalogItem=catalogItem)))
				self.qty = len(SerializedItem.objects.filter(catalogItem=catalogItem))
			else:
				self.error = ''
				self.extended= catalogItem.listPrice * qty 
		else:
			self.available = qty
			self.error = ''
			self.extended= catalogItem.listPrice * qty 


class Cart(object):
	def __init__(self, cartItem_list, rentalItem_list):
		self.cartItem_list = cartItem_list
		self.rentalItem_list = rentalItem_list
		extend = []
		if self.cartItem_list:
			for c in cartItem_list:
				extend.append(c.extended)


		TWOPLACES = Decimal(10) ** -2

		tax_percent = Decimal(.07)
		extended_sum = 0
		if sum(extend)!=0:
			extended_sum = (sum(extend)).quantize(TWOPLACES)
		tax = (tax_percent * sum(extend)).quantize(TWOPLACES)
		total = (tax + sum(extend)).quantize(TWOPLACES)

		self.extended_sum = extended_sum
		self.tax = tax
		self.total = total



