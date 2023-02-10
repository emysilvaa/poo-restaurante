from menu import Menu
from produto import Produto

class Pedido:
    def __init__(self, mesa, nomeCliente, codigoProduto, quantidade):
        self.mesa = mesa
        self.nomeCliente = nomeCliente
        self.codigoProduto = codigoProduto
        self.quantidade = quantidade
    
    def mostrarCardapio(self):
        Menu()


    def fazerPedido(self, mesa, nomeCliente):
        resposta2 = 0
        valorFinal = 0
        self.mesa = int(input('Mesa -> '))
        self.nomeCliente = str(input('Nome -> '))
        while resposta2 != '0':
            tipoProduto = int(input('O que você deseja pedir?\n1 - PRATOS\n2 - BEBIDAS\n3 - SOBREMESAS\n ->  '))
            codigoProduto = str(input('Código -> '))
            quantidade = int(input('Quantidade -> '))
            if tipoProduto == 1:
                with open('pratos.txt' , 'r') as f:
                    pratos = f.readlines()
                    for c in pratos:
                        linha = c.split('::')
                        if codigoProduto == linha[0]:
                            pedido = float(linha[2])
                            valorFinal += pedido * quantidade
                            resposta = str(input('1 - Continuar Pedido\n2 - Fechar Pedido\n ->  '))
                            if resposta == '2':
                                print(f' Valor final do pedido: R${valorFinal}')
                                resposta2 = str(input('0 - Encerrar\n -> '))  
                            elif resposta == '1':
                                continue

            elif tipoProduto == 2:
                with open('bebidas.txt' , 'r') as f:
                    bebidas = f.readlines()
                    for c in bebidas:
                        linha = c.split('::')
                        if codigoProduto == linha[0]:
                            pedido = linha[2]
                            pedido = float(pedido)
                            valorFinal += pedido * quantidade
                            resposta = str(input('1 - Continuar Pedido\n2 - Fechar Pedido\n ->  '))
                            if resposta == '2':
                                print(f' Valor final do pedido: R${valorFinal}')
                                resposta2 = str(input('0 - Encerrar\n -> '))  
                            elif resposta == '1':
                                continue
    
            elif tipoProduto == 3:
                with open('sobremesas.txt', 'r') as f:
                    sobremesas = f.readlines()
                    for c in sobremesas:
                        linha = c.split('::')
                        if codigoProduto == linha[0]:
                            pedido = linha[2]
                            pedido = float(pedido)
                            valorFinal += pedido * quantidade
                            resposta = str(input('1 - Continuar Pedido\n2 - Fechar Pedido\n ->  '))
                            if resposta == '2':
                                print(f'Valor final do pedido: R${valorFinal}')
                                resposta2 = str(input('0 - Encerrar\n -> '))  
                            elif resposta == '1':
                                continue



            

        
        
