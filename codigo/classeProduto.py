path = 'C:\\Users\\20211174010002\\Documents\\GitHub\\poo-restaurante\\codigo\\estoque.txt'
try:
    with open(path, 'r') as f:
        estoque = f.readlines()
except:
    with open(path, 'w') as f:
        f.write('')

class Produto:
    def __init__(self):
        print('Bem-Vindo, deseja adicionar produtos no seu estoque? ')
        resposta1 = int(input(' Para adicionar tecle: 1,  Para sair tecle: 2 >  '))
        if resposta1 == 1:
            resposta2 = 0
            while  resposta2 != 4 :
                self.codigo = str(input('Codigo: '))
                self.nomeProduto = str(input('Nome do seu produto: '))
                self.precoProduto = str(input('coloque o preço: '))
                resposta2 = int(input('Deseja adicionar outro produto?\n SIM: 3 NÃO: 4 > '))

                with open(path, 'a') as f:
                    f.write(f'{self.codigo} :: {self.nomeProduto} :: R${self.precoProduto}\n')

        else:
            print('Você saiu da função de adicionar produtos! ')

   
##################################################################################################  
produtos = Produto()

