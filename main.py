# Script du jeu le juste prix
import random

if __name__ == '__main__':
    prix = random.randint(1, 10)
    r = True
    while r:
        _input = input('Entrez un prix en 1 et 10 :')
        try:
            if int(_input) == prix:
                r = False
            else:
                print(f'{_input} est trop grand !') if int(_input) > prix else print(f'{_input} est trop Petit !')
        except:
            print(f'{_input} n\'est pas un nombre entre 1 et 10 !')
    else:
        print(f'Vous avez trouvé le bon prix ! c\'était bien {_input}')
