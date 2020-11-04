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


#Endpoint # 6  original API not working at this endpoint
@api.post("/registration") 
def isEmailDup(request):
    headers = {}
    payload = {'first_name': 'manjet', 'last_name':'sin', 'email':'manjet@test.com', 'phone':'919191911'}
    url = f'registration?'
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    return {"result": mydata}


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


#Endpoint # 33
@api.post("/send-money-pay") 
def sendMoneyPay(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'12', 'currency_id':'1', 'amount':'5', 'totalFees':'2', 'note':'test', 'emailorPhone':'user@test.com'}
    url = f'https://vaultspay.com/api/v1/send-money-pay?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 34
@api.post("/request-money-email-check") 
def requestMoneyEmailCheck(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'receiverEmail':'merchant@test.com'}
    # request money from own account
    # payload = {'user_id':'13', 'receiverEmail':'merchant@test.com'}
    url = f'https://vaultspay.com/api/v1/request-money-email-check?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 35
@api.post("/request-money-phone-check") 
def requestMoneyPhoneCheck(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'receiverPhone':'+97112345678'}
    url = f'https://vaultspay.com/api/v1/request-money-phone-check?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 36
@api.post("/get-request-currency") 
def getRequestCurrency(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13'}
    url = f'https://vaultspay.com/api/v1/get-request-currency?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 37
@api.post("/request-money-pay") 
def requestMoneyPay(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'currencyId':'1', 'amount':'5', 'totalFees':'2', 'emailOrPhone':'merchant@test.com', 'note':'test'}
    url = f'https://vaultspay.com/api/v1/request-money-pay?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 38
@api.post("/accept-request-email-phone") 
def acceptRequestEmailPhone(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'tr_ref_id':'15'}
    url = f'https://vaultspay.com/api/v1/accept-request-email-phone?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 39
@api.post("/get-accept-fees-details") 
def getAcceptFeesDetails(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'amount':'15', 'currency_id':'1'}
    url = f'https://vaultspay.com/api/v1/get-accept-fees-details?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 40
@api.post("/accept-request-payment-pay") 
def acceptRequestPaymentPay(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'currency_id':'1', 'tr_ref_id':'15', 'totalFees':'1', 'tr_email_or_phone':'merchant@test.com'}
    url = f'https://vaultspay.com/api/v1/accept-request-payment-pay?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 41
@api.post("/cancel-request") 
def cancelRequest(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'tr_email_or_phone':'merchant@test.com', 'tr_id':'61' }
    url = f'https://vaultspay.com/api/v1/cancel-request?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 42
@api.post("/cancel-request") 
def cancelRequestt(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13' }
    url = f'https://vaultspay.com/api/v1/cancel-request?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 43
@api.post("/exchange-review") 
def exchangeReview(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'amount':'5', 'currency_id':'1'}
    url = f'https://vaultspay.com/api/v1/exchange-review?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 44
@api.post("/getBalanceOfFromAndToWallet") 
def getBalanceOfFromAndToWallet(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'currency_id':'1'}
    url = f'https://vaultspay.com/api/v1/getBalanceOfFromAndToWallet?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 45
@api.post("/getBalanceOfFromAndToWallet") 
def getBalanceOfFromAndToWallet(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'currency_id':'1'}
    url = f'https://vaultspay.com/api/v1/getBalanceOfFromAndToWallet?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 46
@api.post("/getBalanceOfFromAndToWallet") 
def getBalanceOfFromAndToWallet(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'user_id':'13', 'currency_id':'1'}
    url = f'https://vaultspay.com/api/v1/getBalanceOfFromAndToWallet?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}



urlpatterns = [
    path('admin/', admin.site.urls),
     path(f"api/{version}/", api.urls),
]
