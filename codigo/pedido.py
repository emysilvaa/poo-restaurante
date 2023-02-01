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

    
    def Mostra_Menu(self):
        Menu()
    
    def Realiza_Pedido(self):
        mesa = str(input('Número da mesa -> '))
        nomeCliente = str(input('Nome do cliente -> '))
        codigoProduto = str(input('codigo do produto desejado -> '))

        
a = Pedido('', '', '', '')
a.Realiza_Pedido()


            

        
        
