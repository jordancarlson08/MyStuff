from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  
from account.models import User, Employee

class Store(models.Model):
  '''Basic Store Model'''
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
  '''Category used for grouping like items'''
  categoryName = models.TextField()
  sort = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return self.categoryName

class SubCategory(models.Model):
  '''Sub Category used for grouping more specific like items'''
  subName = models.TextField()
  category = models.ForeignKey(Category)

  def __str__(self):
    return '%s - %s' %(self.category, self.subName)


class Condition(models.Model):
  '''Describes the condition of an item'''
  condition = models.TextField()

  def __str__(self):
    return self.condition


class CatalogItem(models.Model):
  '''Catalog Item'''
  name = models.TextField()
  manufacturer = models.TextField(blank=True, null=True)
  listPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  commissionRate = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  techSpecs = models.TextField(blank=True, null=True)
  sku = models.TextField(blank=True, null=True)
  fillPoint = models.IntegerField(blank=True, null=True)
  leadTime = models.TextField(blank=True, null=True)
  created = models.DateField(auto_now=True)
  createdBy = models.ForeignKey(Employee)
  category = models.ForeignKey(SubCategory)
  isActive = models.BooleanField(default=True)
  img = models.ImageField(blank=True, null=True, upload_to='products/')
  isSerial = models.BooleanField(default=True)
  views = models.IntegerField(default=0)

  def __str__(self):
    return '%s %s' %(self.manufacturer, self.name)


class SerializedItem(models.Model):
  '''Serialized Item: A rental item or a high value item'''
  store = models.ForeignKey(Store)
  catalogItem = models.ForeignKey(CatalogItem)
  listPrice = models.DecimalField(max_digits=8, decimal_places=2)
  cost = models.DecimalField(max_digits=8, decimal_places=2)
  commissionRate = models.DecimalField(max_digits=3, decimal_places=2)
  serialNum = models.TextField()
  shelfLocation = models.TextField(blank=True, null=True)
  condition = models.ForeignKey(Condition)
  conditionDetails = models.TextField()
  created = models.DateField(auto_now=True)
  createdBy = models.ForeignKey(Employee)
  isActive = models.BooleanField(default=True)
  isRental = models.BooleanField(default=False)
  pricePerDay = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  replacementFee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  lateFee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  isSold = models.BooleanField(default=False)
  isRented = models.BooleanField(default=False)


  def __str__(self):
    return '%s %s - %s' %(self.catalogItem.manufacturer, self.catalogItem.name, self.serialNum)


class Image(models.Model):
  title= models.TextField()
  img = models.ImageField(blank=True, null=True, upload_to='products/')


class History(models.Model):
  user = models.ForeignKey(User)
  catalogItem = models.ForeignKey(CatalogItem)
  last = models.DateTimeField(auto_now=True)

  def __str__(self):
    return 'User: %s; Item: %s %s;' %(self.user.username, self.catalogItem.manufacturer, self.catalogItem.name)



# class ImageFolder(models.Model):
#   catalogItem = models.ForeignKey(CatalogItem, blank=True, null=True)
#   serializedItem = models.ForeignKey(SerializedItem, blank=True, null=True)
#   folderPath = models.TextField()

# class Image(models.Model):
#   imageFolder = models.ForeignKey(ImageFolder)
#   imgPath = models.TextField()

