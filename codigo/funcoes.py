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