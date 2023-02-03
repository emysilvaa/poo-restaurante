from produto import Produto
from menu import Menu
from funcoes import arquivoBebidas, arquivoPratos, arquivoSobremesas, verificaCodigo
from pedido import Pedido

while True:
    opcao = int(input('DIGITE UMA OPÇÃO:\n1 - ADICIONAR PRODUTOS  \n2 - ENTRAR NO MENU\n3 - PEDIDO\n0 - SAIR DO PROGRAMA\n --> '))
    if opcao == 1:
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
            produto = Produto(codigo, nomeProduto, precoProduto)
        

    elif opcao == 2:
        Menu()

            

    elif opcao == 3:
        mesa = int(input('Mesa -> '))
        nomeCliente = str(input('Nome -> '))
        Menu()
        resposta2 = 0
        valorFinal = 0
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
          
        pedido = Pedido(mesa, nomeCliente, codigoProduto, quantidade)
        # with open('pedido.txt', 'a') as f:
            # f.write(f'{mesa}::{nomeCliente}::{linha[1]}::{valorFinal}::\n')

    elif opcao == 0:
        break

    else:
        continue

'''
PROPOSTA DE CARDÁPIOS:
1) PRATOS:
001 - Fetuccine - R$ 30.00
002 - Parmegiana - R$ 35.00
003 - Strogonoff - R$ 25.00

2) BEBIDAS:
001 - Coca-cola - R$ 5.00
002 - Suco de laranja - R$ 5.00
003 - Chá gelado - R$ 7.00

3) SOBREMESA:
001 - Mousse de chocolate - R$ 10.00
002 - Torta de limão - R$ 10.00
003 - Bolo de cenoura - R$ 10.00

'''
