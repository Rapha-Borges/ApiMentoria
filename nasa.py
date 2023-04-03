import requests

# API para consultar astronautas no espaço 

# URL da API
url = 'http://api.open-notify.org/astros.json'

# GET

response = requests.get(url)
number = str(response.json()['number'])
print('Número de astronautas no espaço: ' + number)