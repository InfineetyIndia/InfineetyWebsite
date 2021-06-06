from django.shortcuts import render, redirect

# from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from django.template import loader
# from django.contrib import messages
#from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from home.forms import SignUpForm

from  payments.models import PlanType, Plan
# Create your views here.

def index(request):
    form = SignUpForm()
    return render(request, "base.html", {'form': form})

def videos(request):
    form = SignUpForm()
    return render(request,"videos.html", {'form': form})


def syllabus(request):
    form = SignUpForm()
    return render(request,"syllabus.html", {'form': form})


def features(request):
    form = SignUpForm()
    return render(request,"features.html", {'form': form})


def subscription(request):
    form = SignUpForm()
    error = request.GET.get('error', None)

    plan_type = PlanType.objects.all()
    
    for type in plan_type:
       type.plans = Plan.objects.filter(type_id=type.id)
    
    context={
      'plan_type':plan_type,
      'error' : error,
      'form' : form
    }
    
    return render(request,"subscription.html", context)


def testimonial(request):
    return render(request,"testimonial.html")


    

