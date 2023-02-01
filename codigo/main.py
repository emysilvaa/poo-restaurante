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
        pass
    
    else:
        break
