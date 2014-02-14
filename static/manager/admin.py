from django.db import models
from django.contrib import admin
from .models import *

# register any models here

admin.site.register(Category)
admin.site.register(CatalogItem)
admin.site.register(Condition)
admin.site.register(SerializedItem)
admin.site.register(Store)

