# Projet: Jeu du jour mystère

import random

# Ce programme permet à l'utilisateur de deviner une date choisie au hasard par le programme

# Listes des jours du mois en question:
janvier = list(range(1, 32))
fevrier = list(range(1, 29))
mars = list(range(1, 32))
avril = list(range(1, 31))
mai = list(range(1, 32))
juin = list(range(1, 31))
juillet = list(range(1, 32))
aout = list(range(1, 32))
septembre = list(range(1, 31))
octobre = list(range(1, 32))
novembre = list(range(1, 31))
decembre = list(range(1, 32))
mois = [("Janvier", janvier), ("Février", fevrier), ("Mars", mars), ("Avril", avril), ("Mai", mai), ("Juin", juin), ("Juillet", juillet), ("Août", aout), ("Septembre", septembre), ("Octobre", octobre), ("Novembre", novembre), ("Décembre", decembre)]  # Liste contenant les mois et leur liste de jours associée
liste_mois_joueur = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]  # Liste qui répertorie tous les choix de mois que peut faire l'utilisateur

# Choix au hasard de la date:
mois_choisi = random.choice(mois)   # Utilisation de la fonction random qui permet au programme de prendre un mois au hasard dans la liste "mois"
mois_a_deviner = mois_choisi[0]  # Récupère le nom du mois choisi 

jours_du_mois_choisi = mois_choisi[1]  # Récupère la liste des jours du mois choisi
jour_a_deviner = random.choice(jours_du_mois_choisi) 

# Affichages des règles et modes de jeu
print("Bienvenue sur le jeu Devine La Date!")
print("Votre but est de trouver la date que j'ai choisie au hasard.")
print("Il existe deux modes de difficulté: le mode facile avec des indices et le mode difficile sans indice.")
niveau_choisi = input("Si vous voulez jouer au mode facile tapez 1 et si vous voulez jouer au mode difficile tapez 2: ")
while niveau_choisi not in ["1", "2"]:  # Vérifie que le mode de jeu choisi est 1 ou 2
    print("Mode de jeu introuvable")
    niveau_choisi = input("Veuillez taper 1 (facile) ou 2 (difficile): ")

# Début du mode facile
# Deviner le mois:
if niveau_choisi == "1":
    print("D'accord c'est parti pour le mode facile!")
    print("Commençons par le mois.")
    nombre_mois_a_deviner = mois.index(mois_choisi)  # Place du mois dans la liste 
    trouve = False
    while trouve == False:  # Tant que le mois n'est pas trouvé, le programme va la demander
         mois_joueur = input("Quel mois j'ai choisi?: ")
         mois_joueur = mois_joueur.capitalize()  # Met la première lettre en majuscule, pour correspondre à la liste des choix possible, dans le cas où la première lettre serait rentré en minuscule
         while mois_joueur not in liste_mois_joueur:  # Vérifie si le mois qui est rentré est bien dans la liste des choix possible
             mois_joueur = input("Erreur. Veuillez rentrer un mois valable: ")
             mois_joueur = mois_joueur.capitalize()
         nombre_mois_joueur = liste_mois_joueur.index(mois_joueur)
         if nombre_mois_joueur < nombre_mois_a_deviner:  # Permet de donner un indice sur le mois qu'il faut deviner sous le modèle du juste prix
             print("C'est pas ça! Le mois que j'ai choisi vient après celui que vous avez entré.")
         elif nombre_mois_joueur > nombre_mois_a_deviner:
             print("C'est pas ça! Le mois que j'ai choisi vient avant celui que vous avez entré.")
         else:
             print("Bravo vous avez trouvé le mois!")
             trouve = True  # Ce qui permet de sortir de la boucle
    
    # Deviner le jour:
    print("Maintenant, passons au jour.")
    trouve = False
    while trouve == False:  # Tant que le jour n'est pas trouvé, le programme va la demander
        while True:  # Boucle infinie qui vérifie si ce qui est entré est bien un nombre entier
            try:
                jour_joueur = int(input("Quel jour j'ai choisi?: "))
                break  # Passe à la suite
            except:  # Renvoie en arrière
                print("Erreur. Veuillez rentrer un jour valable.")
        if jour_joueur < jour_a_deviner:  # Permet de donner un indice sur le jour qu'il faut deviner sous le modèle du juste prix
            print("C'est pas ça! Le jour que j'ai choisi est plus grand que celui que vous avez entré.")
        elif jour_joueur > jour_a_deviner:
            print("C'est pas ça! Le jour que j'ai choisi est plus petit que celui que vous avez entré.")
        else:
            print("Bravo vous avez trouvé le jour!")
            trouve = True  # Ce qui permet de sortir de la boucle
    print("J'avais donc choisi le", jour_a_deviner, mois_a_deviner,)  # Résultat final

# Début du mode difficile
# Deviner le mois:
else:
    print("D'accord, c'est parti pour le mode difficile!")
    print("Commençons par le mois")
    trouve = False
    while trouve == False:  # Tant que le mois n'est pas trouvé, le programme va la demander
         mois_joueur = input("Quel mois j'ai choisi?: ")
         mois_joueur = mois_joueur.capitalize()
         while mois_joueur not in liste_mois_joueur:  # Vérifie si le mois qui est rentré est bien dans la liste des choix possible
             mois_joueur = input("Erreur. Veuillez rentrer un mois valable: ")
             mois_joueur = mois_joueur.capitalize()
         if mois_joueur != mois_a_deviner:  # Vérifie si le mois qui est rentré correspond au mois qu'il faut deviner
             print("C'est pas ça!")
         else:
             print("Bravo vous avez trouvé le mois!")
             trouve = True  # Ce qui permet de sortir de la boucle
    
    # Deviner le jour:
    print("Maintenant, passons au jour.")
    trouve = False
    while trouve == False:  # Tant que le jour n'est pas trouvé, le programme va la demander
        while True:  # Boucle infini qui vérifie si ce qui est entré est bien un nombre entier
            try:
                jour_joueur = int(input("Quel jour j'ai choisi?: "))
                break  # Passe à la suite
            except:  # Renvoie en arrière
                print("Erreur. Veuillez rentrer un jour valable.") 
        if jour_joueur != jour_a_deviner:  # Vérifie si le jour qui est rentré correspond au jour qu'il faut deviner
            print("C'est pas ça!")
        else:
            print("Bravo vous avez trouvé le jour!")
            trouve = True  # Ce qui permet de sortir de la boucle
    print("J'avais donc choisi le", jour_a_deviner, mois_a_deviner,)  # Résultat final