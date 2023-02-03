from menu import Menu
try:
    with open('pedido.txt','r') as f:
        pedido = f.readlines()
except:
    with open('pedido.txt','w') as f:
        f.write('')

class Pedido():
    def __init__(self, mesa, nomeCliente, codigoProduto, quantidade):
        self.mesa = mesa
        self.nomeCliente = nomeCliente
        self.codigoProduto = codigoProduto
        self.quantidade = quantidade

    

            

        
        
