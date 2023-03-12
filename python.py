import random

# innitialisation des variables

token = 0 # choisi qui commenceras
player_1_city = 0 # représente le nombre de villes en la posséssion du jouer 1
player_2_city = 0 # représente le nombre de villes en la posséssion du jouer 2

# innitialisation des tableaux et dicctionnaires

list_card = [] # la liste des cartes (la pioche)
board_card = [] # les cartes qui seront déposées sur le plateau
player_1_hand = [] # les cartes dans la main du joueur 1
player_2_hand = [] # les cartes dans la main du joueur 2
player_1_take_card = [] # les cartes qui auront été récupérées par le joueur 1
player_2_take_card = [] # les cartes qui auront été récupérées par le joueur 2
player_1_actions = [] # liste les actions du joueur 1
player_2_actions = [] # liste les actions du joueur 2

# innitialisation des fonctions

    # choisi quel face du jeton commence
def random_token() :
    return random.randint(1,2)

    #mélanger les cartes
def shuffle_cards() :
    return

    # distribuer les cartes
def distribute_cards() :
    return

    # place les cartes sur le plateau lors du début du tour
def place_bord_card() :
    return

    # calcule les points
def point_calculation(list_card) :
    point = 0
    point += support_card_calculation(list_card)
    point += alliance_and_betrayal_card_calculation(list_card)
    return point

    # calcule les points par rapport au cartes supports
def support_card_calculation(list_card) :
    point = 0
    return point

    # calcule les points par rapport au cartes alliances et trahison
def alliance_and_betrayal_card_calculation(list_card) :
    point = 0
    return point

    # fonction qui détermine le vainqueur
def choose_the_winner(player_1_point, player_2_point) :
    if player_1_point > player_2_point :
        victory()
    else :
        defeat()

    # function si il y as victoire
def victory() :
    return

    # function si il y as défaite
def defeat() :
    return

    # affiche la main des deux joueurs
def display_cards(list_card_player_1, list_card_player_2) :
    return

    # quand le joueur joue une carte
def play_cards(list_card_player, which_card, player_1_or_2) :
    global player_1_actions
    global player_2_actions
    
    if player_1_or_2 == 1 :
        player_1_actions.append('place')
    else :
        player_2_actions.append('place')
    return

    #  fonction qui permet de prendre les cartes
def take_cards(player_1_or_2) :
    global player_1_take_card
    global player_2_take_card
    
    if player_1_or_2 == 1 :
        print('joueur 1 prend')
    else :
        print('joueur 2 prend')
    return 

# code
token = random_token()
while input("voulez vous jouer ? : ") != '' :
    shuffle_cards()
    for i in range(12) :
        distribute_cards()
        place_bord_card()
        display_cards()
        if token == 1 :
            print('tour joueur 1')
            token = 2
        else :
            print('tour joueur 2')
            token = 1
    choose_the_winner(point_calculation(player_1_take_card), point_calculation(player_2_take_card))