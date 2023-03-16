import requests

endpoint = 'http://127.0.0.1:5000/users'
responde = requests.post(endpoint)
print(responde.text)

# Para testar a API, execute o arquivo server.py e depois execute o arquivo client.py
# Exemplo: python client.py