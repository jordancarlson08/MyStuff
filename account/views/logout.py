from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager import models as hmod
from account import models as amod
from . import templater
from manager.views.stores import StoreForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def process_request(request):
    logout(request)

    tvars = {}
    
    return templater.render_to_response(request, 'logout.html', tvars)