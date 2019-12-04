import requests

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

first_url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
ids = []
for page in range(1, 11):
    data = {
        "on": "true",
        "page": str(page),
        "pageSize": "15",
        "productName": "",
        "conditionType": "1",
        "applyname": "",
        "applysn": ""
    }
    response = requests.post(url=first_url, data=data, headers=headers)
    if response.headers['Content-Type'] == 'application/json;charset=UTF-8':
        json_obj = response.json()
        for dic in json_obj['list']:
            ids.append(dic['ID'])

detail_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
for _id in ids:
    data = {
        'id': _id
    }
    company_text = requests.post(url=detail_url, data=data, headers=headers).text
    print(company_text)
