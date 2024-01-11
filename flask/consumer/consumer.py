import json
import requests

URL = 'http://127.0.0.1:5000'
resposta_hoteis = requests.request('GET', URL + '/hoteis?cidade=Santos')
print(resposta_hoteis.status_code)
hoteis = resposta_hoteis.json()
print(hoteis['hoteis'])

# / POST CADASTRO

endpoint_cadastro = URL + '/cadastro'
body_cadastro = {
    'login': 'Neto',
    'senha': 'mudar123'
}

headers_cadastro = {
    'Content-Type': 'application/json'
}

resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)

print(resposta_cadastro.json())

# / POST LOGIN

endpoint_cadastro = URL + '/login'
body_cadastro = {
    'login': 'Neto',
    'senha': 'mudar123'
}

headers_cadastro = {
    'Content-Type': 'application/json'
}

resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)

token = resposta_cadastro.json()
print(token['access_token'])

endpoint_hotel_id = URL + '/hoteis/vchotel'
body_hotel_id = {
    'nome': 'VC Hotel alterado',
    'estrelas': 4.4,
    'diaria': 398.90,
    'cidade': 'Santos',
    "site_id": 2
}

headers_hotel_id = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token['access_token']
        
}

# resposta_hotel_id = requests.request('POST', endpoint_hotel_id, json=body_hotel_id, headers=headers_hotel_id)
resposta_hotel_id = requests.request('PUT', endpoint_hotel_id, json=body_hotel_id, headers=headers_hotel_id)
print(resposta_hotel_id)