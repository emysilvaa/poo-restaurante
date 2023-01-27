from produto import Produto
from menu import Menu


while True:
    opcao = int(input('''DIGITE UMA OPÇÃO -
1 - ENTRAR NO MENU
2 - ADICIONAR PRODUTO
3 - SAIR DO PROGRAMA
> '''))
    if opcao == 1:
        Menu()
    elif opcao == 2:
        resposta2 = 0
        while  resposta2 != 4 :
            tipoProduto = int(input('''Tipo produto:
            1 - Pratos
            2 - Bebidas
            3 - Sobremesas '''))
            codigo = str(input('Codigo: '))
            nomeProduto = str(input('Nome do seu produto: '))
            precoProduto = str(input('Coloque o preço: '))
            if tipoProduto == 1:









             resposta2 = int(input('Deseja adicionar outro produto?\n SIM: 3 NÃO: 4 > '))

            produto = Produto(codigo, nomeProduto, precoProduto)
    elif opcao == 3:
        break