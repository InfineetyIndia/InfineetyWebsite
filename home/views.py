from django.shortcuts import render, redirect

# from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from django.template import loader
# from django.contrib import messages
#from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from home.forms import SignUpForm

# Create your views here.

def index(request):
    form = SignUpForm()
    return render(request, "base.html", {'form': form})

def videos(request):
    return render(request,"videos.html")


def syllabus(request):
    return render(request,"syllabus.html")


def features(request):
    return render(request,"features.html")


def subscription(request):
    return render(request,"subscription.html")


def testimonial(request):
    return render(request,"testimonial.html")


    

