from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from home.forms import SignUpForm

# Create your views here.

def index(request):
    form = SignUpForm()
    return render(request, "index.html", {'form': form})

def subscription(resquest):
    return HttpResponse('hi')
    

