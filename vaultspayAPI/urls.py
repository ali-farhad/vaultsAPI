"""vaultspayAPI URL Configuration
"""

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja import Schema
from ninja.security import HttpBearer
import requests
import json

api = NinjaAPI()
version = "v1"

secret = ""

#Endpoint # 1
@api.get("/login") 
def login(request, email:str = "", password:str = ""):
    headers={f'Content-Type':'application/json'}
    # response = requests.get(f'https://vaultspay.com/api/v1/login?email={email}&password={password}')
    response = requests.get(f'https://vaultspay.com/api/v1/login?email={email}&password={password}', headers=headers)
    mydata = response.json()
    test = mydata
    if test["response"]["status"] == 202:
        secret = ""
        return {"result": mydata}
    else:
         secret = test["response"]["token"]
         t = 50
         return {"result": mydata}


#Endpoint # 2
@api.get("/get-preference-settings") 
def prs(request):
    headers={f'Content-Type':'application/json', 'Authorization':'Bearer {secret}'}
    response = requests.get(f'https://vaultspay.com/api/v1/get-preference-settings', headers=headers)
    mydata = response.json()
    # print(secret)
    return {"result": mydata}

#Endpoint # 3
@api.get("/check-user-status") 
def checkUserStatus(request, user_id:int = ""):
    response = requests.get(f'https://vaultspay.com/api/v1/check-user-status?user_id={user_id}')
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 4
@api.get("/check-login-via") 
def checkLoginVia(request):
    response = requests.get(f'https://vaultspay.com/api/v1/check-login-via')
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 5
@api.get("/check-merchant-user-role-existence") 
def checkMerchantUserRoleExistence(request):
    response = requests.get(f'https://vaultspay.com/api/v1/check-merchant-user-role-existence')
    mydata = response.json()
    return {"result": mydata}


#Endpoint # 6 not working


#Endpoint # 7
@api.post("/registration/duplicate-email-check") 
def isEmailDup(request, email:str):
    # response = requests.post(f'https://vaultspay.com/api/v1/registration/duplicate-email-check?email={email}', data={'email': 'test@test.com'})
    # req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
    url = f'https://vaultspay.com/api/v1/registration/duplicate-email-check?email={email}'
    payload = {'email': f'{email}'}
    headers= {}
    response = requests.request("POST", url, headers=headers, data = payload)
    mydata = response.json()
    return {"result": mydata}


#APIs garded by User Session

@api.get("/get-default-wallet-balance") 
def getDefaultWalletBalance(request, user_id:int = "", token:str = ""):
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(f'https://vaultspay.com/api/v1/get-default-wallet-balance?user_id=12', headers=headers)
    # if(response.status_code == 500):
    #     print("something went wrong")
    if(response.status_code == 200):
        mydata = response.json()
        x = mydata["success"]["status"]
        # print(x)
        return {"result": mydata}
    else:
        return {"error": "something went wrong"}
  


urlpatterns = [
    path('admin/', admin.site.urls),
     path(f"api/{version}/", api.urls),
]
