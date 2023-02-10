from funcoes import arquivoBebidas, arquivoPratos, arquivoSobremesas

class Menu:
    try:
        with open('menu.txt', 'r') as f:
            menu = f.readlines()
    except:
        with open('menu.txt', 'w') as f:
            f.write('')

    try:
        with open('pratos.txt','r') as f:
            pratos = f.readlines()
    
        with open('bebidas.txt', 'r' ) as f:
            bebidas = f.readlines()
    
        with open('sobremesas.txt','r') as f:
            sobremesas = f.readlines()
    except:
        arquivoBebidas()
        arquivoPratos()
        arquivoSobremesas()
    def __init__(self):

        with open('pratos.txt','r') as f:
            pratos = f.readlines()
        
        with open('bebidas.txt','r') as f:
            bebidas = f.readlines()

        with open('sobremesas.txt','r') as f:
            sobremesas = f.readlines()
    
        with open('menu.txt','w') as f:
            f.write('')
        
        with open('menu.txt','a') as f:
            f.write('====PRATOS====:\n')
            for c in pratos:
                if c:
                    f.write(c)
            f.write('====BEBIDAS====:\n')
            for c in bebidas:
                if c:
                    f.write(c)
            f.write('====SOBREMESAS====:\n')
            for c in sobremesas:
                if c:
                    f.write(c)

            print('====PRATOS====')
            for c in pratos:
                linha = c.split("::")
                print(f"{linha[0]}  ||  {linha[1]}  ||  R${linha[2]}")

            print('====BEBIDAS====')
            for c in bebidas:
                linha = c.split("::")
                print(f"{linha[0]}  ||  {linha[1]}  ||  R${linha[2]}")

            print('====SOBREMESAS====')
            for c in sobremesas:
                linha = c.split("::")
                print(f"{linha[0]}  ||  {linha[1]}  ||  R${linha[2]}")


'''
=========BEBIDAS========
CODIGO | NOME         | PREÇO
001    | COLA-COLA    | 5.00
002    | SUCO DE UVA  | 3.00

'''