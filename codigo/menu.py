try:
    with open('menu.txt', 'r') as f:
        menu = f.readlines()
except:  
    with open('menu.txt', 'w') as f:
        f.write('')

class Menu:
    def __init__(self):
        with open('estoque.txt', 'r') as f:
            estoque = f.readlines()

        try:
            existe = estoque[0]
        except:
            print('Estoque está vazio')
        
        print(estoque)