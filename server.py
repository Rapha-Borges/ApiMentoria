from flask import Flask, Response, request

# API REST com Flask e Python com 5 métodos HTTP (GET, POST, PUT, DELETE) e 2 rotas (users e orders)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    if request.method == 'GET':
        return Response('Método GET')
    elif request.method == 'POST':
        return Response('Método POST')
    elif request.method == 'PUT':
        return Response('Método PUT')
    elif request.method == 'DELETE':
        return Response('Método DELETE')

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        return Response('Lista de usuários')
    elif request.method == 'POST':
        return Response('Usuário criado')
    elif request.method == 'PUT':
        return Response('Usuário atualizado')
    elif request.method == 'DELETE':
        return Response('Usuário excluído')
    
@app.route('/orders', methods=['GET', 'POST', 'PUT', 'DELETE'])
def orders():
    if request.method == 'GET':
        return Response('Lista de pedidos')
    elif request.method == 'POST':
        return Response('Pedido criado')
    elif request.method == 'PUT':
        return Response('Pedido atualizado')
    elif request.method == 'DELETE':
        return Response('Pedido excluído')
    
if __name__ == '__main__':  
    app.run()

# Para testar a API, execute o arquivo server.py e depois execute o arquivo client.py
# Exemplo: python server.py