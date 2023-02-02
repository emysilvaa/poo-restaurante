from produto import Produto
from menu import Menu
from funcoes import arquivoBebidas, arquivoPratos, arquivoSobremesas, verificaCodigo


while True:
    opcao = int(input('DIGITE UMA OPÇÃO\n1 - ADICIONAR PRODUTOS  \n2 - ENTRAR NO MENU\n3 - PEDIDO\n0 - SAIR DO PROGRAMA\n --> '))
    if opcao == 1:
        resposta2 = 0
        while  resposta2 != 4:
            print('1 - Pratos\n2 - Bebidas\n3 - Sobremesas')
            tipoProduto = int(input('--> '))
            codigo = str(input('Codigo: '))
            nomeProduto = str(input('Nome do seu produto: '))
            precoProduto = str(input('Coloque o preço: '))

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
                
            resposta2 = int(input('Deseja adicionar outro produto?\n SIM: 3 NÃO: 4 > '))
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
            tipoProduto = int(input('O que deseja pedir?\n1 - PRATOS\n2 - BEBIDAS\n3 - SOBREMESAS\n ->  '))
            codigoProduto = str(input('Informe o codigo do seu pedido -> '))
            quantidade = int(input('Quantidade -> '))
            if tipoProduto == 1:
                with open('pratos.txt' , 'r') as f:
                    pratos = f.readlines()
                    for c in pratos:
                        linha = c.split('::')
                        if codigoProduto == linha[0]:
                            pedido = float(linha[2])
                            valorFinal += pedido * quantidade
                            resposta = str(input('Continuar Pedido: 1\n Fechar Pedido: 2\n ->  '))
                            if resposta == '2':
                                print(valorFinal)
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
                            resposta = str(input('Continuar Pedido: 1\n Fechar Pedido: 2\n ->  '))
                            if resposta == '2':
                                print(valorFinal)
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
                            resposta = str(input('Continuar Pedido: 1\n Fechar Pedido: 2\n ->  '))
                            if resposta == '2':
                                print(valorFinal)
                            elif resposta == '1':
                                continue
                
    elif opcao == 0:
        break

    else:
        continue

'''- mostrar menu - ok
    - falar nome e mesa
    - escolher qual é o tipo de cardapio
    - escolher o produto
    - falar a quantidade 
    - encerrar pedido
    - mostrar valor do pedido final3

'''