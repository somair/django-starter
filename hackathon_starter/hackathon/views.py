# Django
from hackathon.models import *
from django.shortcuts import render
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Django REST Framework
from rest_framework import viewsets, mixins

# Python
import oauth2 as oauth
import simplejson as json
import requests

# Models
from hackathon.serializers import SnippetSerializer
from hackathon.forms import UserForm


profile_track = None

def index(request):
    print "index: " + str(request.user)

    if request.GET.items():
        user = User.objects.get(username = request.user.username)

    return render(request, 'hackathon/index.html', {})


###################
#  Subscriptions  #
###################

def subscriptions(request):
    user = request.user
    accountNum = user.profile.accountNum
    if accountNum:
        return render(request, 'hackathon/subscriptions.html', {})

    else:
        return render(request, 'hackathon/accountNumber.html', {})   

##################################
#  Get The Users Account Number  #
##################################

def accountNumber(request):
    if request.method == 'POST':
        accountNum = request.POST.get('accountNum')
        userProfile = UserProfile.objects.get(user=request.user)
        print userProfile.accountNum
        userProfile.accountNum = accountNum
        userProfile.save()
        print userProfile.accountNum
        return HttpResponseRedirect('/hackathon/subscriptions/')

    else:
        return render(request, 'hackathon/accountNumber.html', {})

#########################
# Snippet RESTful Model #
#########################

class CRUDBaseView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass

class SnippetView(CRUDBaseView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()


######################
# Registration Views #
######################

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('/hackathon/login/')
        else:
            print user_form.errors
    else:
        user_form = UserForm()


    return render(request,
            'hackathon/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/hackathon/subscriptions/')
            else:
                return HttpResponse("Your Django Hackathon account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'hackathon/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/hackathon/login/')
