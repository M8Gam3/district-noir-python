# Bibliothèques utilisées
import random
import re
import os

#-------------------- Fonctions ----------------
"""Concaténer une chaine à un code couleur.
Cette fonction sert à retourner une chaine en lui appliquant une couleur en fonction d'un code 
Codes Couleur utile pour l'exercice
Blue : 32 | Orange : 208 | Pink : 206 | Yellow : 220 | Green : 28 | Red : 196
Parameters
----------
pstr : string
    Chaine à colorer
pcolor : int
    code couleur (cf. chiffre ci-dessus)
Returns
-------
string
    la chaine en entrée concaténé avec la couleur, de type : 
        Code couleur : "\x1b[38;5;33m" + {valeur} + Code permettant de remttre la couleur intiale "\x1b[0;0m"
"""
def set_color(pstr, pcolor):
    
    num1 = str(pcolor)
    if pcolor % 16 == 0:
        return(f"\033[38;5;{num1}m{pstr}\033[0;0m")
    else:
        return(f"\033[38;5;{num1}m{pstr}\033[0;0m")
# print(set_color('5', 206))

"""Retire tous les codes couleur.
Permetter de retirer tous les codes couleur des valeurs d'une liste passé en paramètre
Parameters
----------
lst_cards_with_color : list
    liste des cartes du jeux avec les codes couleur
Returns
-------
list
    retourne la liste des cartes du jeux sans les codes couleur
"""
def get_lst_cards_value(lst_cards_with_color):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    lst_cards_value = []
    for card in lst_cards_with_color:
        value = ansi_escape.sub('', card).strip()
        if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            value = int(value)
        lst_cards_value.append(value)
    return lst_cards_value
# test = [set_color('5', 32), set_color('8', 208), set_color('7', 206)]
# print(get_lst_cards_value(test))

"""Initialisation de la partie.
Cette fonction aura pour but de générer le paquets de cartes en fonction de sa composition dans le jeu :
- Cartes "SOUTIEN" : carte 5 * 5, carte 6 * 6, carte 7 * 7, carte 8 * 8 (ces cartes pourront être générés à l'aide d'une double boucle)
- Cartes "ALLIANCE" : carte 2 * 4, carte 3 * 2, carte 4 * 1 (cf. tuple alliances)
- Cartes "TRAHISON" : carte -1 * 3, carte -2 * 4, carte -3 * 2 (cf. tuple treasons)
Parameters
----------
Aucun
Returns
-------
lst_cards : list
    Retourne la liste des cartes qui constitue le paquet. Le code couleur sera appliqué sur les cartes (cf. dict code_color_cards)
beginner: int
    Retourne le numéro du joueur qui commence à la manche 1. Le chiffre sera soit 1 soit 2 et sera choisi aléatoirement
"""
def init_game():
    # tuple contenant la liste des cartes alliances du paquet
    alliance = (2, 2, 2, 2, 3, 3, 4)
    
    # tuple contenant la liste des cartes trahison du paquet
    trahison = (-1, -1, -1, -2, -2, -2, -2, -3, -3)
    
    # dictionnaire permettant de connaitre le code couleur de la carte en fonction de sa valeur
    color_soutien = {
        5 : 32,
        6 : 206,
        7 : 208,
        8 : 220,
    }
    
    lst_cards = []

    # Ajout des cartes 5, 6, 7 et 8
    for i in range(5, 9) :
        for x in range(i) :
            lst_cards.append(set_color(i, color_soutien[i]))
    
    # Ajout des cartes "ville"
    lst_cards.append("Docs")
    lst_cards.append("Commissariat")
    lst_cards.append("Mairie")
    
    # Ajout de cartes "alliance"
    for i in alliance :
        lst_cards.append(set_color(i, 28))

    # Ajout de cartes "trahison"
    for i in trahison :
        lst_cards.append(set_color(i, 196))

    # Mélangez les 45 cartes
    random.shuffle(lst_cards)

    # Retirer 3 cartes
    lst_cards = lst_cards[3:]
    
    # Une fois la génération du paquet de cartes terminé, on le retourne
    return lst_cards
# , random.randint(1,2)
# print(get_lst_cards_value(init_game()))
# print(len(init_game()))
"""Distribue les cartes pour chaque joueur et en mets 2 sur la table à la manche 1.
Cette fonction aura pour but de distribuer 5 cartes à chaque joueur
Au round 1, 2 cartes 
Parameters
----------
round : int
    numéro de la manche en cours
Returns
-------
lst_game, lst_player_1, lst_player_2
    Retourne 3 listes :
        - lst_game : liste contenant 2 cartes pour la 1ère manche et vide pour les autres manches
        - lst_player_1 : contenant les 5 cartes du joueur 1
        - lst_player_2 : contenant les 5 cartes du joueur 2
"""
def to_deal(lst_game, round):
    global lst_cards
    lst_player_1 = []; lst_player_2 = []

    # Distribuez 5 cartes à chaque joueur
    for i in range(5) :
        lst_player_1.append(lst_cards[0])
        lst_player_2.append(lst_cards[1])
        lst_cards = lst_cards[1:]

    # On distribue 2 cartes sur la table uniquement pour la première manche
    if round == 1 :
        for i in range(2) :
            lst_game.append(lst_cards[0])
            lst_cards = lst_cards[0:]
        # Distribuez 2 cartes face visible
        
        #i'm here !
    
    return lst_game, lst_player_1, lst_player_2
lst_cards = init_game()
print(f"{to_deal([], 1)[0]}\n{to_deal([], 1)[1]}\n{to_deal([], 1)[2]}")

"""Affiche le jeu.
Cette procédure affiche les cartes de la table ainsi que les cartes ramassées par les joueurs
Parameters
----------
round : int
    numéro du round en cours
lst_game : list
    Liste des cartes sur la table
lst_collecting_cards_1 : list
    Liste des cartes ramassées par le joueur 1
lst_collecting_cards_2 : list
    Liste des cartes ramassées par le joueur 2
num_player : int
    Numéro du joueur qui doit jouer
lst_player: list
    Liste des cartes du joueur qui doit jouer
Returns
-------
Aucun
"""
def display_game(round, lst_game, lst_collecting_cards_1, lst_collecting_cards_2, num_player = 0, lst_player = []):
    # Efface la console
    os.system('cls')
    
    # Séparateur pour une meilleur visibilité
    print(f'--------- Manche {round} ----------')

    # Afficher les cartes sur la table

    # Afficher les cartes ramassées par le joueur 1

    # Afficher les cartes ramassées par le joueur 2

    # Séparateur pour une meilleur visibilité
    print('\n------------------------------')

    # Afficher la main du joueur qui doit jouer
    

"""Lance un tour de jeu.
Cette fonction aura pour but de lancer le tour d'un joueur, elle devra :
- Si le joueur décide de poser une carte : mettre à jour les cartes de sa main
- Si le joueur décide de ramasser : mettre à jour ses cartes ramassées et mettre à jour le booléen take
- Dans les 2 cas : mettre à jour les cartes de la table
Parameters
----------
lst_game : list
    Liste des cartes sur la table
num_player : int
    Numéro du joueur qui est en train de jouer
lst_player: list
    Liste des cartes du joueur qui est en train de jouer
lst_collecting_cards : list
    Liste des cartes ramassées du joueur qui est en train de jouer
player_take : Boolean
    booléen permettant de savoir si le joueur qui est en train de jouer à déjà ramassé durant la manche ou non
Returns
-------
lst_game, lst_player, lst_collecting_cards, take
    Retourne 4 listes :
        - lst_game : liste des cartes de la table mise à jour
        - lst_player : liste des cartes du joueur qui est en train de jouer mise à jour
        - lst_collecting_cards : liste des cartes ramassées du joueur qui est en train de jouer mise à jour
        - take : booléen permettant de savoir si le joueur qui est en train de jouer à déjà ramassé durant la manche ou non mis à jour
"""
def to_play(lst_game, num_player, lst_player, lst_collecting_cards, player_take):
    
    # On converti la liste des cartes de la main du joueur en liste extrayant que la valeur des cartes
    
    # Tant que la saisie diffère d'une carte de la main ou qu'elle est différente de 0, on refait saisir le joueur
    while True:
        # Demander au joueur de saisie la valeur d'une carte de sa main ou de saisir la chaine "take" s'il souhaite prendre et qu'il n'a pas encore pris durant cette manche
        
        # Si le joueur décide de joueur une carte de sa main

            # on retire la carte de sa main et on l'ajouter aux cartes de la table
            
            break
        # Sinon si le joueur décide de prendre les cartes de la table s'il n'a pas déjà pris durant cette manche et qu'il y a au moins 1 carte sur la table
        
            # Si le jeu contient moins de 5 cartes, le joueur ramasse toutes les cartes de la table

                # On ajoute les cartes prise à ses carte ramassées et on les retire de la table de jeu
                
            # On vérifie si le joueur possède 3 carte cité
            
            
            # Ne pas oublié de passer le drapeau permettant de savoir s'il a pris durant cette manche à True
            
            break

    return lst_game, lst_player, lst_collecting_cards, player_take

"""Vérifie si le joueur ne possède pas 3 cartes cités.
Cette fonction aura pour but vérifier si le joueur qui vient de ramasser des cartes ne possède pas 3 cartes cités,
si c'est le cas, il faudra mettre fin à la partie tout de suite et le déclarer vainqueur
Parameters
----------
num_player : int
    Numéro du joueur qui est en train de jouer
lst_collecting_cards : list
    Liste des cartes ramassées du joueur pour laquelle on souhaite vérifier qu'il n'y a pas 3 cartes cités
Returns
-------
Aucun
"""
def check_three_cities(num_player, lst_collecting_cards):
    nb_cities = 0
    # On boucle sur les cartes ramassées du joueur
    
        # Si la carte a pour valeur (inutile de retirer le code couleur car les cartes cités n'en possède pas) le nom d'une des 3 cités
        
            # si c'est le cas on incrémente un compteur

    # Si 3 cartes cités sont comptés on appelle la fonction end_game
    

"""Regroupe et Compte les cartes ramassées par un joueur.
Cette fonction aura pour but de regrouper les cartes de même valeur et de les compter. Ce qui simplifira le comptage des points.
Elle exclura également les cartes cités car elle ne sont pas nécessaire au comptage des points
Parameters
----------
lst_collecting_cards : list
    Liste des cartes ramassées du joueur pour laquelle on souhaite vérifier qu'il n'y a pas 3 cartes cités
Returns
-------
lst_group_cards : dictionnaire
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes
"""    
def get_group_cards(lst_collecting_cards):
    lst_group_cards = {}
    # Avant de compter les cartes, on retire le code couleur des cartes
    
    # On boucle sur toutes les cartes
    
        # Si les cartes sont différentes des cartes cités on les ajoute au dictionnaire
        
            # Si la valeur de la carte a déjà été inséré dans le dictionnaire, on incrémente sa quantité
            
            # Sinon on l'ajoute dans le dictionnaire
            
    return lst_group_cards

"""Calcule les points
Cette fonction aura pour but de calculer les points à partir du dictionnaire regroupant les cartes. Le comptage se fera selon les règles suivantes :
    - cartes SOUTIEN identiques : la majorité marque le nombre de points égal au chiffre du SOUTIEN, en cas d'égalité aucun joueur ne remporte les points
    - 4 cartes SOUTIEN différentes : 5 points par série de 5-6-7-8
    - cartes ALLIANCE et TRAHISON : ajouter et retirer les points figurant sur les cartes
En cas d'égalité : le joueur ayant le plus de cartes SOUTIEN 8 remporte la partie, si égalité même chose pour les cartes SOUTIEN 7 etc...
Parameters
----------
group_cards_1 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 1
group_cards_2 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 2
Returns
-------
score_player_1 : int
    Score du joueur 1
score_player_2 : int
    Score du joueur 2
"""
def get_scoring(group_cards_1, group_cards_2):
    score_player_1 = 0
    score_player_2 = 0

    # SOUTIEN (cartes de 5 à 8) : La majorité marque un nombre de points égal au chiffre représenté sur la carte SOUTIEN 
    # En cas d'égalité aucun joueur ne remporte les points
    

    # SOUTIEN (cartes de 5 à 8) : 4 SOUTIENS différents repporte 5 points
    # Calcul pour le Joueur 1
    
    # Calcul pour le Joueur 2

    # ALLIANCE et TRAHISON : Additionner et soustraire leur valeur

        # ALLIANCE Joueur 1
        
        # ALLIANCE Joueur 2
        
    
        # TRAHISON Joueur 1
    
        # TRAHISON Joueur 2

    return score_player_1, score_player_2

"""Retourne le vainqueur
Compare le score du joueur 1 et du joueur 2 et retourne le vainqueur.
En cas d'égalité, compte quel joueur possède le plus de cartes SOUTIEN 8 et le retorune en vainqueur, si égalité même chose pour les cartes SOUTIEN 7 etc...
Parameters
----------
score_player_1 : int
    Score du joueur 1
score_player_2 : int
    Score du joueur 2
group_cards_1 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 1
group_cards_2 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 2
Returns
-------
[1-2]: int
    Retourn 1 si le joueur 1 remporte la partie et 2 si le joueur 2 remporte la partie
"""
def get_winner(score_player_1, score_player_2, group_cards_1, group_cards_2):
    return
    # Le score du joueur 1 est supérieur au score du joueur 2 => le joueur 1 gagne

    # Le score du joueur 1 est inférieur au score du joueur 2 => le joueur 2 gagne

    # Sinon égalité

        # En cas d'égalité, le joueur ayant le plus de soutien de valeur 8 l'emporte, puis en cas de nouvelle égalité le joueur ayant le plus de soutien de valeur 7 l'emporte etc.
        

"""Affiche le vainqueur
Concatène "Vainqueur : Joueur"  et le numéro du joueur vainqueur pour l'afficher et quitte le jeu
Parameters
----------
num_player : int
    numéro du joueur vainqueur
Returns
-------
Aucun"""

def end_game(num_player):
    print(f"-----------Vainqueur : Joueur {num_player}------------")
    exit()

#-------------------- Initialisation de mon dictionnaire players ----------------
players = {"lst_player_1" : [], "lst_player_2" : [], "lst_collecting_cards_1" : [], "lst_collecting_cards_2" : [], "take_player_1": False, "take_player_2": False}

#-------------------- Script principal ----------------
# Initilisation d'une partie
lst_cards = init_game()

# Boucler pour lancer 4 manches

    # Distribution des cartes pour chaque manche

    # Boucler tant que les joueurs possèdent encore des cartes en main et qu'ils n'ont pas tous les 2 pris de cartes sur la table
        
        # Ordre des tours de jeu en fonction du joueur qui coommence la manche
        

        # Boucler pour les 2 joueurs

            # Afficher le jeu
            
            # Faire jouer un joueur
            

    # Remettre la drapeau take des players False


#-------------------- Fin de partie ----------------
# regrouper les cartes des joueurs pour simplifier le calcul des points

# Calcul des points pour les 2 joueurs

# en fonction du nombre de points des joueurs on renvoie le vainqueur ou on départage en cas d'égalité