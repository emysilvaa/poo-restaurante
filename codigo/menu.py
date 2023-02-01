from funcoes import arquivoBebidas, arquivoPratos, arquivoSobremesas
try:
    with open('menu.txt', 'r') as f:
        menu = f.readlines()
except:  
    with open('menu.txt', 'w') as f:
        f.write('')

try:

    with open('pratos.txt','r') as f:
        pratos = f.readlines()
            
    with open('bebidas.txt','r') as f:
        bebidas = f.readlines()
            
    with open('sobremesas.txt','r') as f:
        sobremesas = f.readlines()
    
    with open('menu.txt','a') as f:
        f.write('PRATOS:\n')
        for c in pratos:
            if c:
                f.write(c)
        f.write('BEBIDAS:\n')
        for c in bebidas:
            if c:
                f.write(c)
        f.write('SOBREMESAS:\n')
        for c in sobremesas:
            if c:
                f.write(c)
except:
    arquivoBebidas()
    arquivoPratos()
    arquivoSobremesas()



class Menu:
    def __init__(self):
            with open('pratos.txt','r') as f:
                    pratos = f.readlines()
            
            with open('bebidas.txt','r') as f:
                    bebidas = f.readlines()
            
            with open('sobremesas.txt','r') as f:
                    sobremesas = f.readlines()
            
            print('PRATOS:')
            for c in pratos:
                if c:
                    print(c)
            print('BEBIDAS:')
            for c in bebidas:
                if c:
                    print(c)
            print('SOBREMESAS:')
            for c in sobremesas:
                if c:
                    print(c)
            
        

        