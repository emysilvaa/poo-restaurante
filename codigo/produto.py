from funcoes import *

class Produto:
    def __init__(self, codigo, nomeProduto, precoProduto):
        self.codigo = codigo
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto
    
    def addProdutos(self):
        resposta2 = 0
        while  resposta2 != 4:
            print('1 - Pratos\n2 - Bebidas\n3 - Sobremesas')
            tipoProduto = int(input('--> '))
            codigo = str(input('Codigo: '))
            nomeProduto = str(input('Digite o nome do seu produto: '))
            precoProduto = str(input('Digite o preço do seu produto: R$'))

            if tipoProduto == 1:
                arquivoPratos()
                veri = verificaCodigo('pratos.txt', codigo)
                if veri == False:      
                    with open('pratos.txt', 'a') as f:
                        f.write(f'{codigo}::{nomeProduto}::{precoProduto}::\n')
                
            elif tipoProduto == 2:
                arquivoBebidas()
                veri = verificaCodigo('bebidas.txt', codigo)
                if veri == False:      
                    with open('bebidas.txt', 'a') as f:
                        f.write(f'{codigo}::{nomeProduto}::{precoProduto}::\n')
    
                

            elif tipoProduto == 3:
                arquivoSobremesas()
                veri = verificaCodigo('sobremesas.txt', codigo)
                if veri == False:      
                    with open('sobremesas.txt', 'a') as f:
                        f.write(f'{codigo}::{nomeProduto}::{precoProduto}::\n')
                
            resposta2 = int(input('Deseja adicionar outro produto?\n3 - SIM\n4 - NÃO\n -> '))


