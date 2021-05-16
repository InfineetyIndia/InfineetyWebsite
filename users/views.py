from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.http import JsonResponse
from twilio.rest import Client
import random


from users.forms import SignUpForm
from users.models import Users

import urllib.request
import urllib.parse



def register(request):
    data = request.POST
    otp = data.get('otp', None)
    print(otp)
    if otp is not None :
        print(1)
        user_id = data.get('user_id', None)
        print(user_id)
        user = Users.objects.get(id=user_id)
        if user.token == otp:
           user.is_active = True
           user.save() 
           return JsonResponse({'success':True, 'message': 'Register successfully.','code':1})
        else:
            return JsonResponse({'success':False , 'message' : 'Not a valid otp.','code':0})

    elif  request.method == 'POST':
        print(2)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            token = generate_token()
            user.token = token
            user.save()
            data = {'user_id': user.id, 'success': True, 'code' : 0}
            sendSMS(token)
            return JsonResponse(data)
        else:
            err=form.errors
            return JsonResponse({'success': False, 'message' : err, 'code': 0})
    else:
        data = {'success': False, 'message' : 'Some problem occured.', 'code' : 0}
        return JsonResponse(data)   

def login(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    user = authenticate(username=email, password=password)
    
    if user is not None:
        data = {'success': True, 'message':'Logged in successfully.', 'code': 1}
        return JsonResponse(data)  
    else:
        data = {'success': False, 'message':'Not a valid credentials.', 'code': 0}
        return JsonResponse(data)  

def generate_token(lenght = 4):
    allowed_chars = "0123456789"
    return ''.join(random.choice(allowed_chars) for x in range(lenght))

 
def sendSMS(token, to = "918287353243"):
    account_sid = "AC9a5170da1100f4cc31c63370603b1b4e"
    auth_token = "d9b47a8be68f09bc2a82a97b33a23c8e"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body = token,
                     from_ = '+12673968299',
                     to = '+918287353243'
                 )

    print(message.sid)



 
