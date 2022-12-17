#          _____                    _____                    _____                   _______               _____          
#         /\    \                  /\    \                  /\    \                 /::\    \             /\    \         
#        /::\    \                /::\    \                /::\____\               /::::\    \           /::\    \        
#       /::::\    \              /::::\    \              /::::|   |              /::::::\    \          \:::\    \       
#      /::::::\    \            /::::::\    \            /:::::|   |             /::::::::\    \          \:::\    \      
#     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |            /:::/~~\:::\    \          \:::\    \     
#    /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |           /:::/    \:::\    \          \:::\    \    
#   /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |          /:::/    / \:::\    \         /::::\    \   
#  /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______   /:::/____/   \:::\____\       /::::::\    \  
# /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \ |:::|    |     |:::|    |     /:::/\:::\    \ 
#/:::/____/  ___\:::|    |/:::/__\:::\   \:::\____\/:::/    |:::::::::\____\|:::|____|     |:::|    |    /:::/  \:::\____\
#\:::\    \ /\  /:::|____|\:::\   \:::\   \::/    /\::/    / ~~~~~/:::/    / \:::\    \   /:::/    /    /:::/    \::/    /
# \:::\    /::\ \::/    /  \:::\   \:::\   \/____/  \/____/      /:::/    /   \:::\    \ /:::/    /    /:::/    / \/____/ 
#  \:::\   \:::\ \/____/    \:::\   \:::\    \                  /:::/    /     \:::\    /:::/    /    /:::/    /          
#   \:::\   \:::\____\       \:::\   \:::\____\                /:::/    /       \:::\__/:::/    /    /:::/    /           
#    \:::\  /:::/    /        \:::\   \::/    /               /:::/    /         \::::::::/    /     \::/    /            
#     \:::\/:::/    /          \:::\   \/____/               /:::/    /           \::::::/    /       \/____/             
#      \::::::/    /            \:::\    \                  /:::/    /             \::::/    /                            
#       \::::/    /              \:::\____\                /:::/    /               \::/____/                             
#        \::/____/                \::/    /                \::/    /                 ~~                                   
#                                  \/____/                  \/____/                                                       
                                                                                                                      
                                                                                                                      
# GEMOT permnet de generer automatiquement des punitions, le programe choisit suivant un niveau de gravite
# Suite au niveau de gravite, tout sera auto, le logiciel choisir entre avetissement, mot et heure de colle
# ou un mélanfz autre pour punir l'éléve fautif
# le tout fait avec amour par Alexis en haute savoie en l'an de grace 2022.

#On lance l'import qui nous permets d'avoir accés a la fonction "random"
#On y ajoute le random punition (choisit la punition)
#Et le random devoirs, pour piocher automatiquement un devoir a faire

import random
punition = random.randint(1,4)
devoirs = random.randint(1,4)
colle = random.randint(1,4)


while True:
    print(
    "G E M O T"
    )
    print("")
    print("Made  by Alexis")
    print("")
    print("Pour continuer vous devez choisir un seuil de gravite")
    print("1.Faible Gravite")
    print("2.Moyenne Gravite")
    print("3.Haute Gravite")
    print("Votre choix ?")
    
    choice = int(input())

          # On commence par le soft, petite punition pour petite betises

    if choice == 1 and punition == 1:
        print("Petite bétise, un advertissement devrait suffir")
        break
    elif choice == 1 and punition == 2:
        print("Petite bétise, un mot devrait suffir")
        break
        
    elif choice == 1 and punition == 3:
        print("Petite bétise, une heure de colle devrait suffir")
            # sur de rien a partir d'ici a prochain com, mais ici on devrait pouvoir générer des heures de colles aléatoires
            if colle ==1:
            print("Il devra faire une heure de colle")
            break
            elif colle == 2:
            print("Il devra faire 2 heures de colles")
            break
            elif colle == 3:
            print("Il devra faire 3 heures de colles")
            break
            elif colle == 4:
            print("Il devra faire 4 heures de colles")
            break
            # Fin du truc bordélique
    elif choice == 1 and punition == 4:
        print("Petite bétise, un mélange mot/heure de colle devrait suffir")
        break

          # On continue avec le medium, punition pour betises moyennes
    elif choice == 2 and punition == 1:
        print("Bétise moyenne, un mot devrait suffir")
        break
    elif choice == 2 and punition == 2:
        print("Bétise moyenne, heure de colle devrait suffir")
            # sur de rien a partir d'ici a prochain com, mais ici on devrait pouvoir générer des heures de colles aléatoires
            if colle ==1:
            print("Il devra faire une heure de colle")
            break
            elif colle == 2:
            print("Il devra faire 2 heures de colles")
            break
            elif colle == 3:
            print("Il devra faire 3 heures de colles")
            break
            elif colle == 4:
            print("Il devra faire 4 heures de colles")
            break
            # Fin du truc bordélique
    elif choice == 2 and punition == 3:
        print("Bétise moyenne, un mélange mot/heure de colle devrait suffir")
            # sur de rien a partir d'ici a prochain com, mais ici on devrait pouvoir générer des heures de colles aléatoires
            if colle ==1:
            print("Il devra faire une heure de colle")
            break
            elif colle == 2:
            print("Il devra faire 2 heures de colles")
            break
            elif colle == 3:
            print("Il devra faire 3 heures de colles")
            break
            elif colle == 4:
            print("Il devra faire 4 heures de colles")
            break
            # Fin du truc bordélique
    elif choice == 2 and punition == 4:
        print("Une exclusion de cours, et une heure de colle devrait lui faire comprendre")
            # sur de rien a partir d'ici a prochain com, mais ici on devrait pouvoir générer des heures de colles aléatoires
            if colle ==1:
            print("Il devra faire une heure de colle")
            break
            elif colle == 2:
            print("Il devra faire 2 heures de colles")
            break
            elif colle == 3:
            print("Il devra faire 3 heures de colles")
            break
            elif colle == 4:
            print("Il devra faire 4 heures de colles")
            break
            # Fin du truc bordélique

          # On continue avec le hard, punition pour betises graves
    
    elif choice == 3 and punition == 1:
        print("Bétise grave, une heure de colle devrait suffir")
            # sur de rien a partir d'ici a prochain com, mais ici on devrait pouvoir générer des heures de colles aléatoires
            if colle ==1:
            print("Il devra faire une heure de colle")
            break
            elif colle == 2:
            print("Il devra faire 2 heures de colles")
            break
            elif colle == 3:
            print("Il devra faire 3 heures de colles")
            break
            elif colle == 4:
            print("Il devra faire 4 heures de colles")
            break
            # Fin du truc bordélique
    elif choice == 3 and punition == 2:
        print("Bétise grave, un mélange mot/heure de colle devrait suffir")
            # sur de rien a partir d'ici a prochain com, mais ici on devrait pouvoir générer des heures de colles aléatoires
            if colle ==1:
            print("Il devra faire une heure de colle")
            break
            elif colle == 2:
            print("Il devra faire 2 heures de colles")
            break
            elif colle == 3:
            print("Il devra faire 3 heures de colles")
            break
            elif colle == 4:
            print("Il devra faire 4 heures de colles")
            break
            # Fin du truc bordélique
    elif choice == 3 and punition == 3:
        print("Une exclusion de cours, et une plusieurs heures de colle devrait lui faire comprendre")
            # sur de rien a partir d'ici a prochain com, mais ici on devrait pouvoir générer des heures de colles aléatoires
            if colle ==1:
            print("Il devra faire une heure de colle")
            break
            elif colle == 2:
            print("Il devra faire 2 heures de colles")
            break
            elif colle == 3:
            print("Il devra faire 3 heures de colles")
            break
            elif colle == 4:
            print("Il devra faire 4 heures de colles")
            break
            # Fin du truc bordélique
    elif choice == 3 and punition == 4:
        print("un aller retour chez le cpe devrait lui faire comprendre")
        break

            # Secret option, pour les betises les plus graves
    
    elif choice == 5:
        print("Un Aller retour chez le principal")
        break
    elif choice == 666 :
        print("This student must die")
        break
    
            # Final pour les fautes de frappe

    else:
        print("Veuillez choisir un nombre entre 1 et 3")
        continue
        
    # Futur option pour les punitions
    # Recupération de la liste des punitions
    # attribution d'un nombre a chaque punition
    # choix du nombre de punition
    # choix de la punition


    #Sa pourrait ressembler a cela:
    
    #Heure de colle
        #Heure de colle généré aléatoirement
            #Devoir 1
            #Devoir 2
        #Heure de colle genéré aléatoirement
            #Devoir 1
            #Devoir 2
