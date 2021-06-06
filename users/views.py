from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from twilio.rest import Client
import random
from django.conf import settings
from twilio.rest.api.v2010.account import message
from django.contrib.auth import logout



from users.forms import SignUpForm
from users.models import Users

import urllib.request
import urllib.parse



def register(request):
    data = request.POST
    otp = data.get('otp', None)
    if otp is not None :
        user_id = data.get('user_id', None)
        user = Users.objects.get(id=user_id)
        if user.token == otp:
           user.is_active = True
           user.save() 
           return JsonResponse({'success':True, 'message': 'Register successfully.','code':1})
        else:
            message = {'otp':'Not a valid otp.'}
            return JsonResponse({'success':False , 'message' : message,'code':0})

    elif  request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            token = generate_token()
            user.token = token
            user.save()
            data = {'user_id': user.id, 'success': True, 'code' : 0}
            sendSMS(token, user.phone_no)
            return JsonResponse(data)
        else:
            err=form.errors
            return JsonResponse({'success': False, 'message' : err, 'code': 0})
    else:
        message = {'otp':'Some problem occured.'}
        data = {'success': False, 'message' : message, 'code' : 0}
        return JsonResponse(data)   

def login_view(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    user = authenticate(username=email, password=password)
    
    if user is not None:
        login(request, user)
        data = {'success': True, 'message':'Logged in successfully.', 'code': 1}
        return JsonResponse(data)  
    else:
        data = {'success': False, 'message':'Not a valid credentials.', 'code': 0}
        return JsonResponse(data)  

def generate_token(length = 4):
    allowed_chars = "0123456789"
    return ''.join(random.choice(allowed_chars) for x in range(length))

 
def sendSMS(token, to = "8287353243"):
    account_sid = settings.TWILLIO_ACCOUNT_SID
    auth_token = settings.TWILLO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body = token,
                     from_ = settings.TWILLIO_FROM_NUMBER,
                     to = '+91'+ to
                 )

    print(message.sid)

def logout_view(request):
    logout(request)
    return redirect('/')



 
