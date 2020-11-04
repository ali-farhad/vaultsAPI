#Endpoint # 20
@api.post("/deposit/get-bank-detail") 
def getBankDetail(request):
    headers = {'Authorization': f'Bearer {secret}'}
    payload = {'bank':'1'}
    url = f'https://vaultspay.com/api/v1/deposit/get-bank-detail?'
    response = requests.request("POST", url, headers=headers, data=payload)
    mydata = response.json()
    return {"result": mydata}