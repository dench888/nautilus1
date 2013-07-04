# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext
from django.http import Http404
from django.conf import settings

def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def auth_login(request):
    email = ''
    password = ''    
    try:
        email = request.POST['email']
        password = request.POST['password']
    except:
        pass    
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            messages.error(request, _('User is disabled'))
    else:
        messages.error(request, _("The username and password were incorrect"))
    return redirect('/')

def auth_logout(request):
    logout(request)
    return redirect('/')
