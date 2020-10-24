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


@api.get("/login") 
def login(request, email:str, password:str):
    headers={f'Content-Type':'application/json'}
    # response = requests.get(f'https://vaultspay.com/api/v1/login?email={email}&password={password}')
    response = requests.get(f'https://vaultspay.com/api/v1/login?email={email}&password={password}', headers=headers)
    mydata = response.json()
    test = mydata
    secret = test["response"]["token"]
    return {"result": mydata}

@api.get("/get-preference-settings") 
def prs(request):
    headers={f'Content-Type':'application/json', 'Authorization':'Bearer {secret}'}
    response = requests.get(f'https://vaultspay.com/api/v1/get-preference-settings', headers=headers)
    mydata = response.json()
    print(secret)
    return {"result": mydata}



urlpatterns = [
    path('admin/', admin.site.urls),
     path(f"api/{version}/", api.urls),
]
