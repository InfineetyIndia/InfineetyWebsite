from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Plan, Transaction
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
import json


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'payments/callback.html', context=received_data)
        
        transaction_obj = str(received_data)
        transaction = Transaction.objects.get(order_id= received_data['ORDERID'][0])
        status = received_data['STATUS'][0]
        if(status == 'TXN_FAILURE'):
            transaction.active_status = 0
        
        elif status == 'TXN_SUCCESS' :
            transaction.active_status = 1
        
        elif status == 'PENDING' :
            transaction.active_status = 2
         	   
        transaction.transaction_obj = transaction_obj
        transaction.save()
        context = {'success':"Subscription completed."}
        # return redirect('subscription?success=')
        return render(request, 'subscription.html', context=context)



def initiate_payment(request):
    try:
        if request.user.is_authenticated:
            order_id = get_random_string(length=10)
            user = request.user
            amount_plan_id = request.POST['amount']
            amtplan = amount_plan_id.split("_")
            amount = float(amtplan[0])
            plan_id = amtplan[1]
            plan = Plan.objects.get(id=plan_id)
            transaction = Transaction.objects.create(made_by=user, amount=amount, plan=plan,order_id=order_id )
            transaction.save()
            amount = str(amount)
        else:
            error = 'Login session expired.'
            return redirect('/subscription?error='+error)
        # return render(request, 'home/subscription.html', context={'error': 'Wrong Accound Details or amount'})

    except:
        error = 'Try after sometimes'
        return redirect('/subscription?error='+error)
        # return render(request, 'subscription.html', context={'error': 'Try after sometimes'})

    merchant_key = settings.PAYTM_SECRET_KEY
    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', order_id),
        ('CUST_ID', 'mukrjha@gmail.com'),
        ('TXN_AMOUNT', amount),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', 'mukrjha@gmail.com'),
        # ('MOBILE_N0', '8287353243'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', settings.CALLBACK_URL),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    # transaction.checksum = checksum
    # transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    # print('SENT: ', checksum)
    return render(request, 'payments/redirect.html', context=paytm_params)



# 1. plan_type : mothly, yearly

# 2. plan : plan_type_id, price


# 3. Subscription :user_id plan_id, valid_from, valid_to

# 4. subscription_payment: user_id, amount, date, status, 
# transaction_id, payments details

# 5.