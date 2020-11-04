"""vaultspayAPI URL Configuration
"""
from dotenv import load_dotenv
import os
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja import Schema
from ninja.security import HttpBearer
import requests
import json

load_dotenv()
api = NinjaAPI()
version = "v1"

secret = str(os.getenv('secret'))


# #Endpoint # 1
# @api.get("/login") 
# def login(request, email:str = "", password:str = ""):
#     headers={f'Content-Type':'application/json'}
#     response = requests.get(f'https://vaultspay.com/api/v1/login?email={email}&password={password}', headers=headers)
#     mydata = response.json()
#     test = mydata
#     if test["response"]["status"] == 202:
#         secret = ""
#         return {"result": mydata}
#     else:
#          secret = test["response"]["token"]
#          t = 50
#          return {"result": mydata}


#Endpoint # 1
@api.post("/login") 
def login(request):
    headers={f'Content-Type':'application/json'}
    payload = {'email': 'user@test.com', 'password': 'Admin@123'}
    url = f'https://vaultspay.com/api/v1/login?'
    headers= {}
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    return {"result": mydata}


# Endpoint # 2

@api.post("/get-preference-settings") 
def getPreferenceSetting(request):
    # headers={f'Content-Type':'application/json', 'Authorization':'Bearer {secret}'}
    headers={f'Content-Type':'application/json'}
    payload = {'Authorization': f'Bearer {secret}'}
    url = f'https://vaultspay.com/api/v1/get-preference-settings?'
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    # print(secret)
    return {"result": mydata}

#Endpoint # 3
@api.post("/check-user-status") 
def checkUserStatus(request):
    headers={}
    payload = {'user_id': '12'}
    url = f'https://vaultspay.com/api/v1/check-user-status?'
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 4
@api.post("/check-login-via") 
def checkLoginVia(request):
    headers={}
    payload = {}
    url = f'https://vaultspay.com/api/v1/check-login-via'
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 5
@api.post("/check-merchant-user-role-existence") 
def checkMerchantUserRoleExistence(request):
    headers={}
    payload = {}
    url = f'https://vaultspay.com/api/v1/check-merchant-user-role-existence'
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 6 not working


#Endpoint # 7
@api.post("/registration/duplicate-email-check") 
def isEmailDup(request):
    headers = {}
    payload = {'email': 'user@test.com'}
    url = f'https://vaultspay.com/api/v1/registration/duplicate-email-check?'
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 8
@api.post("/registration/duplicate-phone-number-check") 
def isPhoneDup(request):
    headers= {}
    payload = {'phone': '9191919191'}
    url = f'https://vaultspay.com/api/v1/registration/duplicate-phone-number-check?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}



#APIs garded by User Session

#Endpoint # 8
@api.post("/get-default-wallet-balance") 
def getDefaultWalletBalance(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12'}
    url = f'https://vaultspay.com/api/v1/get-default-wallet-balance?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 10
@api.post("/get-user-profile") 
def getUserProfile(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13'}
    url = f'https://vaultspay.com/api/v1/get-user-profile?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 11
@api.post("/get-user-specific-details") 
def getUserSpecificDetails(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'email':'user@test.com'}
    url = f'https://vaultspay.com/api/v1/get-user-specific-details?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}
   

#Endpoint # 12
@api.post("/profile/duplicate-email-check") 
def profileDuplicateEmailCheck(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'email':'user@test.com'}
    url = f'https://vaultspay.com/api/v1/profile/duplicate-email-check?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 13
@api.post("/check-processed-by") 
def checkProcessedBy(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {}
    url = f'https://vaultspay.com/api/v1/check-processed-by?'
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code == 500):
        print("something went wrong")
    
    elif(response.status_code == 200):
        mydata = response.json()
     
        return {"result": mydata}
    else:
        return {"error": "something went wrong"} 

#Endpoint # 14
@api.post("/available-balance") 
def availableBalance(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13'}
    url = f'https://vaultspay.com/api/v1/available-balance?'
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code == 500):
        print("something went wrong")
    
    elif(response.status_code == 200):
        mydata = response.json()
     
        return {"result": mydata}
    else:
        return {"error": "something went wrong"} 

#Endpoint # 15
@api.post("/activityall") 
def activityall(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'type':'allTransactions'}
    url = f'https://vaultspay.com/api/v1/activityall?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 16
@api.post("/transaction-details") 
def transDetails(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'tr_id':'12'}
    url = f'https://vaultspay.com/api/v1/transaction-details?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 17
@api.post("/get-deposit-currency-list") 
def getDepositCurrList(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13'}
    url = f'https://vaultspay.com/api/v1/get-deposit-currency-list?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}
   


#Endpoint # 18
@api.post("/get-deposit-bank-list") 
def getDepositBankList(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13'}
    url = f'https://vaultspay.com/api/v1/get-deposit-bank-list?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}
    

#Endpoint # 19
@api.post("/get-deposit-details-with-amount-limit-check") 
def getDepositDetailsWithAmountLimitCheck(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'amount':'5', 'currency_id':'1', 'paymentMethodId': '3'}
    url = f'https://vaultspay.com/api/v1/get-deposit-details-with-amount-limit-check?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 20
@api.post("/deposit/get-bank-detail") 
def getBankDetail(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'bank':'1'}
    url = f'https://vaultspay.com/api/v1/deposit/get-bank-detail?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 21
@api.post("/deposit/bank-payment-store") 
def depositBankPaymentStore(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'amount':'5', 'currency_id':'1', 'deposit_payment_id':'6', 'deposit_payment_name':'Bank', 'bank_id':'1', 'totalFees':'2'}
    url = f'https://vaultspay.com/api/v1/deposit/bank-payment-store?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 22
@api.post("deposit/get-stripe-info") 
def getStripeInfo(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'currency_id':'1', 'method_id':'10'}
    url = f'https://vaultspay.com/api/v1/deposit/get-stripe-info?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 23
@api.post("deposit/get-paypal-info") 
def getPaypalInfo(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'currency_id':'1', 'method_id':'10'}
    url = f'https://vaultspay.com/api/v1/deposit/get-paypal-info?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 24
@api.post("/check-payout-settings") 
def checkPayoutSettings(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12'}
    url = f'https://vaultspay.com/api/v1/check-payout-settings?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 25
@api.post("/get-withdraw-payment-method") 
def getWithdrawPaymentMethod(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12'}
    url = f'https://vaultspay.com/api/v1/get-withdraw-payment-method?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 26
@api.post("/get-withdraw-currencies-based-on-payment-method") 
def getWithdrawCurrenciesBasedOnPaymentMethod(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'paymentMethodId':'1'}
    url = f'https://vaultspay.com/api/v1/get-withdraw-currencies-based-on-payment-method?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 27 [possible error in documentation]
@api.post("/get-withdraw-currencies-based-on-payment-method") 
def getWithdrawCurrenciesBasedOnPaymentMethod(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'amount':'5', 'currency_id':'1', 'payoutSetid':'1', 'paymentMethodId':'3'}
    url = f'https://vaultspay.com/api/v1/get-withdraw-currencies-based-on-payment-method?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 28
@api.post("/withdraw-money-pay") 
def withdrawMoneyPay(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'currency_id':'1', 'amount':'5', 'payout_setting_id':'1', 'totalFees':'2'}
    url = f'https://vaultspay.com/api/v1/withdraw-money-pay?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 29
@api.post("/send-money-email-check") 
def sendMoneyEmailCheck(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'receiverEmail': 'user@test.com'}
    # send to Own Email
    # payload = {'user_id':'12', 'receiverEmail': 'merchant@test.com'}
    url = f'https://vaultspay.com/api/v1/send-money-email-check?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 30
@api.post("/send-money-phone-check") 
def sendMoneyPhoneCheck(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'receiverPhone': '+97152345678'}
    url = f'https://vaultspay.com/api/v1/send-money-phone-check?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 31
@api.post("/get-send-money-currencies") 
def sendMoneyPhoneCheck(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12'}
    url = f'https://vaultspay.com/api/v1/get-send-money-currencies?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 32
@api.post("/check-send-money-amount-limit") 
def checkSendMoneyAmountLimit(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'sendCurrency':'1', 'amount':'5'}
    url = f'https://vaultspay.com/api/v1/check-send-money-amount-limit?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}




urlpatterns = [
    path('admin/', admin.site.urls),
     path(f"api/{version}/", api.urls),
]
