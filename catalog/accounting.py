
from django.http import HttpResponseRedirect
from account.models import *
from manager.models import *
from catalog.models import *

def record_sale(transaction, cost):
  '''Creates the journal entries in the DB for a sale'''
  je = JournalEntry()
  je.transaction = transaction
  je.note = ''
  je.save()

  cash = AccountEntry()
  cash.isDebit = True
  cash.amount = transaction.total
  cash.ledger = Ledger.objects.get(name='Cash')
  cash.journalEntry = je
  cash.save()

  cogs = AccountEntry()
  cogs.isDebit = True
  cogs.amount = cost
  cogs.ledger = Ledger.objects.get(name='Cost of Goods Sold')
  cogs.journalEntry = je  
  cogs.save()

  tax = AccountEntry()
  tax.isDebit = False
  tax.amount = transaction.tax
  tax.ledger = Ledger.objects.get(name='Tax Payable')
  tax.journalEntry = je  
  tax.save()

  sale = AccountEntry()
  sale.isDebit = False
  sale.amount = transaction.subtotal
  sale.ledger = Ledger.objects.get(name='Sale')
  sale.journalEntry = je 
  sale.save()

  inventory = AccountEntry()
  inventory.isDebit = False
  inventory.amount = cost
  inventory.ledger = Ledger.objects.get(name='Inventory')
  inventory.journalEntry = je  
  inventory.save() 