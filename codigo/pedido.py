from menu import Menu
try:
    with open('pedido.txt','r') as f:
        pedido = f.readlines()
except:
    with open('pedido.txt','w') as f:
        f.write('')

class Pedido(Menu):
    def __init__(self):
        pass
    
    def Mostra_Menu(self):
        print()
    
    def Realiza_Pedido(self):
        print('Deseja realizar o pedido?')
        self.resposta = input('Digite 1 para SIM e 2 para NÃO: ')
        self.resposta2 = 0
        if self.resposta == '1':
            while self.resposta2 != '4' :
                self.mesa = int(input('Porfavor digite o número de sua mesa: '))
                self.nome = input('Porfavor digite o seu nome: ')
                self.codigo = input('Porfavor digite o código do produto: ')
                self.qnt = input('Por favor digite a quantidade do produto ')
                print('Deseja fazer mais algum pedido?')  
                self.resposta2 = input('Digite 3 para ADICIONAR e 4 para SAIR: ')

cliente = Pedido()
cliente.Mostra_Menu()

            

        
        
