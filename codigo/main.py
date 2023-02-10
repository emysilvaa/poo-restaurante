from produto import Produto
from menu import Menu
from pedido import Pedido

while True:
    opcao = int(input('DIGITE UMA OPÇÃO:\n1 - ADICIONAR PRODUTOS  \n2 - ENTRAR NO MENU\n3 - PEDIDO\n0 - SAIR DO PROGRAMA\n --> '))

    if opcao == 1:
        produto = Produto('000', 'produtos', '00.00')
        produto.addProdutos()


    elif opcao == 2:
        Menu()

            

    elif opcao == 3:
        pedido = Pedido('00', 'clientes', '000', 'quantidade')
        pedido.mostrarCardapio()
        pedido.fazerPedido('00', 'Cliente')   

    elif opcao == 0:
        break

    else:
        continue



'''
PROPOSTA DE CARDÁPIO:
1) PRATOS:
001 - Lasanha - R$ 30.00
002 - Parmegiana - R$ 35.00

2) BEBIDAS:
001 - Coca-cola - R$ 5.00
002 - Suco de laranja - R$ 5.00

3) SOBREMESA:
001 - Torta de Morango - R$ 10.00
002 - Bolo de cenoura - R$ 10.00

'''
