from random import randint
import os
import time

def grille(plateau):
    '''
    Ecrit la grille dans le terminal
    '''
    template_grid = f"""
        A   B   C
      -------------
    1 | {plateau[0][0]} | {plateau[0][1]} | {plateau[0][2]} | 1
      -------------
    2 | {plateau[1][0]} | {plateau[1][1]} | {plateau[1][2]} | 2
      -------------
    3 | {plateau[2][0]} | {plateau[2][1]} | {plateau[2][2]} | 3
      -------------
        A   B   C"""
    print(template_grid)


def position_victoire(plateau):
    if (plateau[0][0]==plateau[0][1]) and (plateau[0][0]==plateau[0][2]) and (plateau[0][0]!=' '):
        return plateau[0][0]
    elif plateau[1][0]==plateau[1][1] and plateau[1][0]==plateau[1][2] and plateau[1][0]!=' ':
        return plateau[1][0]
    elif plateau[2][0]==plateau[2][1] and plateau[2][0]==plateau[2][2] and plateau[2][0]!=' ':
        return plateau[2][0]
    elif plateau[0][0]==plateau[1][0] and plateau[0][0]==plateau[2][0] and plateau[0][0]!=' ':
        return plateau[0][0]
    elif plateau[0][1]==plateau[1][1] and plateau[0][1]==plateau[2][1] and plateau[0][1]!=' ':
        return plateau[0][1]
    elif plateau[0][2]==plateau[1][2] and plateau[0][2]==plateau[2][2] and plateau[0][2]!=' ':
        return plateau[0][2]
    elif plateau[0][0]==plateau[1][1] and plateau[0][0]==plateau[2][2] and plateau[0][0]!=' ':
        return plateau[0][0]
    elif plateau[0][2]==plateau[1][1] and plateau[0][2]==plateau[2][0] and plateau[0][2]!=' ':
        return plateau[0][2]
    else:
        return ' '
          
          
def nombre_case_libre(plateau):
    cpt = 0
    for i in range(3):
        for j in range(3):
            if plateau[i][j]==' ':cpt+=1
    return cpt


def modif_plateau(plateau, joueur, jeu_inversion=False):
    """
    Modifie le plateau et le renvoie
    """
    if jeu_inversion:
        selection_item = randint(0, 1)
    else:
        selection_item=joueur
    
    if selection_item==0:
        item = 'x'
    else:
        item = 'o'
    
    coup_incorrect = True
    
    while coup_incorrect:
        if jeu_inversion:
            print(f"\nLe symbole joué est {item}.")
        coup = input(f'\nTour du joueur {joueur}. Donner le coup (format [ColonneLigne]).\n')
        if coup=='A1' and plateau[0][0]==' ':
            plateau[0][0] = item
            coup_incorrect = False
        elif coup=='A2' and plateau[1][0]==' ':
            plateau[1][0] = item
            coup_incorrect = False
        elif coup=='A3' and plateau[2][0]==' ':
            plateau[2][0] = item
            coup_incorrect = False
        elif coup=='B1' and plateau[0][1]==' ':
            plateau[0][1] = item
            coup_incorrect = False
        elif coup=='B2' and plateau[1][1]==' ':
            plateau[1][1] = item
            coup_incorrect = False
        elif coup=='B3' and plateau[2][1]==' ':
            plateau[2][1] = item
            coup_incorrect = False
        elif coup=='C1' and plateau[0][2]==' ':
            plateau[0][2] = item
            coup_incorrect = False
        elif coup=='C2' and plateau[1][2]==' ':
            plateau[1][2] = item
            coup_incorrect = False
        elif coup=='C3' and plateau[2][2]==' ':
            plateau[2][2] = item
            coup_incorrect = False
        else:
            print("\nMauvais format ou emplacement déjà utilisé, recommencer avec le bon format (ex : \"A1\") sur une case vide.")
    return plateau
        


def partie_normal():
    """
    Défini la partie et renvoie le vainqueur
    """
    plateau = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # Choix du premier joueur
    while True :
        type_premier_joueur = input('\nPremier joueur ? [0/1/rd]\n\n')
        if type_premier_joueur == '0':
            joueur_tour = 0
            break
        elif type_premier_joueur == '1':
            joueur_tour = 1
            break
        elif type_premier_joueur == 'rd':
            joueur_tour = randint(0, 1)
            break
        else:
            continue
    while position_victoire(plateau)==' ' and nombre_case_libre(plateau)>0:
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        plateau = modif_plateau(plateau, joueur_tour)
        joueur_tour = 1-joueur_tour
    if position_victoire(plateau)=='x':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 0 a gagné.")
        return 0
    elif position_victoire(plateau)=='o':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 1 a gagné.")
        return 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nMatch nul.")
        return -1


def partie_aveugle():
    """
    Défini la partie et renvoie le vainqueur
    """
    plateau = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # Choix du premier joueur
    while True :
        type_premier_joueur = input('\nPremier joueur ? [0/1/rd]\n\n')
        if type_premier_joueur == '0':
            joueur_tour = 0
            break
        elif type_premier_joueur == '1':
            joueur_tour = 1
            break
        elif type_premier_joueur == 'rd':
            joueur_tour = randint(0, 1)
            break
        else:
            continue
    while position_victoire(plateau)==' ' and nombre_case_libre(plateau)>0:
        plateau = modif_plateau(plateau, joueur_tour)
        joueur_tour = 1-joueur_tour
    if position_victoire(plateau)=='x':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 0 a gagné.")
        return 0
    elif position_victoire(plateau)=='o':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 1 a gagné.")
        return 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nMatch nul.")
        return -1


def partie_blocus():
    """
    Défini la partie et renvoie le vainqueur
    """
    plateau = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # Choix du premier joueur
    while True :
        type_premier_joueur = input('\nPremier joueur ? [0/1/rd]\n\n')
        if type_premier_joueur == '0':
            joueur_tour = 0
            break
        elif type_premier_joueur == '1':
            joueur_tour = 1
            break
        elif type_premier_joueur == 'rd':
            joueur_tour = randint(0, 1)
            break
        else:
            continue
    while position_victoire(plateau)==' ' and nombre_case_libre(plateau)>0:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if nombre_case_libre(plateau)>2:
            i_bloque = randint(0, 2)
            j_bloque = randint(0, 2)
            while plateau[i_bloque][j_bloque]!=' ':
                i_bloque = randint(0, 2)
                j_bloque = randint(0, 2)
            plateau[i_bloque][j_bloque] = '#'
            
        grille(plateau)
        plateau = modif_plateau(plateau, joueur_tour)
        for i in range(3):
            for j in range(3):
                if plateau[i][j]=='#':
                    plateau[i][j]=' '
        
        joueur_tour = 1-joueur_tour
    if position_victoire(plateau)=='x':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 0 a gagné.")
        return 0
    elif position_victoire(plateau)=='o':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 1 a gagné.")
        return 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nMatch nul.")
        return -1
    
    
def partie_inversion():
    """
    Défini la partie et renvoie le vainqueur
    """
    plateau = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # Choix du premier joueur
    while True :
        type_premier_joueur = input('\nPremier joueur ? [0/1/rd]\n\n')
        if type_premier_joueur == '0':
            joueur_tour = 0
            break
        elif type_premier_joueur == '1':
            joueur_tour = 1
            break
        elif type_premier_joueur == 'rd':
            joueur_tour = randint(0, 1)
            break
        else:
            continue
    while position_victoire(plateau)==' ' and nombre_case_libre(plateau)>0:
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        plateau = modif_plateau(plateau, joueur_tour, True)
        joueur_tour = 1-joueur_tour
    if position_victoire(plateau)=='x' or position_victoire(plateau)=='o':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print(f"\nLe joueur {1-joueur_tour} a gagné.")
        return 0
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nMatch nul.")
        return -1
    

def partie_disparition():
    """
    Défini la partie et renvoie le vainqueur
    """
    plateau = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # Choix du premier joueur
    while True :
        type_premier_joueur = input('\nPremier joueur ? [0/1/rd]\n\n')
        if type_premier_joueur == '0':
            joueur_tour = 0
            break
        elif type_premier_joueur == '1':
            joueur_tour = 1
            break
        elif type_premier_joueur == 'rd':
            joueur_tour = randint(0, 1)
            break
        else:
            continue
    while position_victoire(plateau)==' ' and nombre_case_libre(plateau)>0:
        os.system('cls' if os.name == 'nt' else 'clear')
        if nombre_case_libre(plateau)<8:
            disp = bool(randint(0, 1))
            if disp:
                i_disp = randint(0, 2)
                j_disp = randint(0, 2)
                while plateau[i_disp][j_disp]==' ':
                    i_disp = randint(0, 2)
                    j_disp = randint(0, 2)
                plateau[i_disp][j_disp] = ' '
                tableau_corresp_col = ["A", "B", "C"]
                print(f"La case {tableau_corresp_col[i_disp]}{j_disp+1} a été supprimée.")
        grille(plateau)
        plateau = modif_plateau(plateau, joueur_tour)
        joueur_tour = 1-joueur_tour
    if position_victoire(plateau)=='x':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 0 a gagné.")
        return 0
    elif position_victoire(plateau)=='o':
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nLe joueur 1 a gagné.")
        return 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        grille(plateau)
        print("\nMatch nul.")
        return -1



def jeu():
    """
    Fonction du jeu entier
    """
    mode_jeu = 'a'
    rejouer = ''
    
    while mode_jeu!='q' and mode_jeu!='Q':
        os.system('cls' if os.name == 'nt' else 'clear')

        mode_jeu = input("\nEntrer le mode de jeu :\n  - Normal [n] : Mode de jeu normal en joueur contre joueur\n  - Aveugle [a] : La grille ne s'affiche qu'à la fin\n  - Blocus [b] : Une case aléatoire est bloquée à chaque tour de jeu\n  - Inversion [i] : A chaque tour, le symbole ajouté par le joueur est tiré au hasard\n  - Disparition [d] : A chaque tour, une case déjà jouée a 1 chance sur 2 de disparaître\n  - Quitter [q]\n\n")

        if mode_jeu=='n' or mode_jeu=='N':
            partie_normal()
            time.sleep(3)

                
        elif mode_jeu=='a' or mode_jeu=='A':
            partie_aveugle()
            time.sleep(3)
    
            
        elif mode_jeu=='b' or mode_jeu=='B':
            partie_blocus()
            time.sleep(3)

        elif mode_jeu=='i' or mode_jeu=='I':
            partie_inversion()
            time.sleep(3)
        
        elif mode_jeu=='d' or mode_jeu=='D':
            partie_disparition()
            time.sleep(3)
        
        elif mode_jeu=='q' or mode_jeu=='Q':
            print("\nMerci d'avoir joué.")
            
        else:
            print("\nCette option n'existe pas.\n\n")

            

jeu()