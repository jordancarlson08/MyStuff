from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  
from account.models import User, Employee

class Store(models.Model):
  locationName = models.TextField()
  street1 = models.TextField()
  street2 = models.TextField(blank=True, null=True)
  city = models.TextField()
  state = models.TextField()
  zipCode = models.IntegerField()
  phone = models.TextField()
  isActive = models.BooleanField(default=True)
  manager = models.ForeignKey(Employee)

  def __str__(self):
  	return '%s, %s' %(self.locationName, self.state)


class Category(models.Model):
  categoryName = models.TextField()

  def __str__(self):
    return self.categoryName


class CatalogItem(models.Model):
  name = models.TextField()
  manufacturer = models.TextField(blank=True, null=True)
  listPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  commissionRate = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  techSpecs = models.TextField(blank=True, null=True)
  sku = models.TextField(blank=True, null=True)
  fillPoint = models.IntegerField(blank=True, null=True)
  leadTime = models.TextField(blank=True, null=True)
  isRental = models.BooleanField(default=False)
  pricePerDay = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  replacementFee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  lateFee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  dateCreated = models.DateField(blank=True, null=True)
  createdBy = models.ForeignKey(Employee)
  categoryID = models.ForeignKey(Category)
  isActive = models.BooleanField(default=True)

  def __str__(self):
    return '%s %s' %(self.manufacturer, self.name)


class Condition(models.Model):
  condition = models.TextField()

  def __str__(self):
    return self.condition



class SerializedItem(models.Model):
  storeID = models.ForeignKey(Store)
  catalogItem = models.ForeignKey(CatalogItem)
  listPrice = models.DecimalField(max_digits=8, decimal_places=2)
  cost = models.DecimalField(max_digits=8, decimal_places=2)
  commissionRate = models.DecimalField(max_digits=2, decimal_places=2)
  serialNum = models.TextField()
  shelfLocation = models.TextField(blank=True, null=True)
  conditionID = models.ForeignKey(Condition)
  conditionDetails = models.TextField()
  isRental = models.BooleanField(default=False)
  dateReceived = models.DateField(blank=True, null=True)
  dateCreated = models.DateField(blank=True, null=True)
  createdBy = models.ForeignKey(Employee)
  isActive = models.BooleanField(default=True)


  def __str__(self):
    return '%s %s - %s' %(self.catalogItem.manufacturer, self.catalogItem.name, self.serialNum)

