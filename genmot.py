# GEMOT permnet de generer automatiquement des punitions, le programe choisit suivant un niveau de gravite
# Suite au niveau de gravite, tout sera auto, le logiciel choisir entre avetissement, mot et heure de colle
# ou un mélanfz autre pour punir l'éléve fautif
# le tout fait avec amour par Alexis en haute savoie en lc'an de grace 2022.

import random
punition = random.randint(1,4)

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
        break
    elif choice == 1 and punition == 4:
        print("Petite bétise, un mélange mot/heure de colle devrait suffir")
        break

          # On continue avec le medium, punition pour betises moyennes
    
    elif choice == 2 and punition == 1:
        print("Bétise moyenne, un mot devrait suffir")
        break
    elif choice == 2 and punition == 2:
        print("Bétise moyenne, une heure de colle devrait suffir")
        break
    elif choice == 2 and punition == 3:
        print("Bétise moyenne, un mélange mot/heure de colle devrait suffir")
        break
    elif choice == 2 and punition == 4:
        print("Une exclusion de cours, et une heure de colle devrait lui faire comprendre")
        break

          # On continue avec le hard, punition pour betises graves
    
    elif choice == 3 and punition == 1:
        print("Bétise grave, une heure de colle devrait suffir")
        break
    elif choice == 3 and punition == 2:
        print("Bétise grave, un mélange mot/heure de colle devrait suffir")
        break
    elif choice == 3 and punition == 3:
        print("Une exclusion de cours, et une plusieurs heures de colle devrait lui faire comprendre")
        break
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