"""vaultspayAPI URL Configuration
"""

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja import Schema
from ninja.security import HttpBearer
import requests

api = NinjaAPI()
version = "v1"

secret = ""

#Endpoint # 1
@api.get("/login") 
def login(request, email:str, password:str):
    headers={f'Content-Type':'application/json'}
    # response = requests.get(f'https://vaultspay.com/api/v1/login?email={email}&password={password}')
    response = requests.get(f'https://vaultspay.com/api/v1/login?email={email}&password={password}', headers=headers)
    mydata = response.json()
    test = mydata
    secret = test["response"]["token"]
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
@api.get("/check-login-via") 
def checkLoginVia(request):
    response = requests.get(f'https://vaultspay.com/api/v1/check-login-via')
    mydata = response.json()
    return {"result": mydata}

#Endpoint # 4
@api.get("/check-merchant-user-role-existence") 
def checkMerchantUserRoleExistence(request):
    response = requests.get(f'https://vaultspay.com/api/v1/check-merchant-user-role-existence')
    mydata = response.json()
    return {"result": mydata}





urlpatterns = [
    path('admin/', admin.site.urls),
     path(f"api/{version}/", api.urls),
]
