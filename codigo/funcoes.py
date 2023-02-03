def arquivoPratos():
    try:
        with open('pratos.txt', 'r' ) as f:
            pratos = f.readlines()
    except:
        with open('pratos.txt', 'w' ) as f:
            f.write('')

    
def arquivoBebidas():
    try:
        with open('bebidas.txt', 'r' ) as f:
            bebidas = f.readlines()
    except:
        with open('bebidas.txt', 'w' ) as f:
            f.write('')

def arquivoSobremesas():
    try:
        with open('sobremesas.txt', 'r' ) as f:
            sobremesas = f.readlines()
    except:
        with open('sobremesas.txt', 'w' ) as f:
            f.write('')

def verificaCodigo(arquivo, codigo):
    existe = False
    with open(arquivo , 'r') as f:
        pratos = f.readlines()
        for c in pratos:
            linha = c.split('::')
            if linha[0] == codigo:
                print(f'''== Já existe um produto cadastrado com este código {codigo}! == ''')
                existe = True
                break
    return existe