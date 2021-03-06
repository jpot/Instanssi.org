# -*- coding: utf-8 -*-

from common.auth import user_access_required
from django.shortcuts import render_to_response
from django.http import Http404,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.core.urlresolvers import reverse
from Instanssi.users.forms import OpenIDLoginForm, DjangoLoginForm, ProfileForm
from common.misc import get_url_local_path

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:profile'))
    
    # Get referer for redirect
    # Make sure that the referrer is a local path.
    if 'next' in request.GET:
        next = get_url_local_path(request.GET['next'])
    else:
        next = get_url_local_path(request.META.get('HTTP_REFERER', reverse('users:profile')))

    # Test django login form
    if request.method == "POST":
        djangoform = DjangoLoginForm(request.POST)
        if djangoform.is_valid():
            djangoform.login(request)
            return HttpResponseRedirect(djangoform.cleaned_data['next'])
    else:
        djangoform = DjangoLoginForm(next=next)
    
    # Openid login form
    # The form will be handled elsewhere; this is only for rendering the form.
    openidform = OpenIDLoginForm(next=next)
    
    # Render response
    return render_to_response("users/login.html", {
        'djangoform': djangoform,
        'openidform': openidform,
        'next': next,
    }, context_instance=RequestContext(request))

def loggedout(request):
    return render_to_response("users/loggedout.html")

@user_access_required
def profile(request):
    if request.method == "POST":
        profileform = ProfileForm(request.POST, instance=request.user, user=request.user)
        if profileform.is_valid():
            profileform.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        profileform = ProfileForm(instance=request.user, user=request.user)
    
    return render_to_response("users/profile.html", {
        'profileform': profileform,
    }, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:loggedout'))
