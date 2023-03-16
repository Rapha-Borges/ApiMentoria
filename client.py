import requests

user_url = 'http://127.0.0.1:5000/users'
order_url = 'http://127.0.0.1:5000/orders'
payload = {'key1': 'value1', 'key2': 'value2'}


# GET

response = requests.get(user_url)
print(response.text)

response = requests.get(order_url)
print(response.text)

# POST

response = requests.post(user_url, data=payload)
print(response.text)

response = requests.post(order_url, data=payload)
print(response.text)

# PUT

response = requests.put(user_url, data=payload)
print(response.text)

response = requests.put(order_url, data=payload)
print(response.text)

# DELETE

response = requests.delete(user_url, data=payload)
print(response.text)

response = requests.delete(order_url, data=payload)
print(response.text)





# Para testar a API, execute o arquivo server.py e depois execute o arquivo client.py
# Exemplo: python client.py