try:
    with open('estoque.txt', 'r') as f:
        estoque = f.readlines()
except:
    with open('estoque.txt', 'w') as f:
            f.write('')

class Produto:
    def __init__(self, codigo, nomeProduto, precoProduto):
        self.codigo = codigo
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto
