# GEMOT permnet de generer automatiquement des punitions, le programe choisit suivant un niveau de gravite
# Suite au niveau de gravite, tout sera auto, le logiciel choisir entre avetissement, mot et heure de colle
# ou un mélanfz autre pour punir l'éléve fautif
# le tout fait avec amour par Alexis en haute savoie en lc'an de grace 2022.

import random
punition = random.randint(1, 4)

while True:
    print("Genmot se lance, les eleves trenblent.")
    print("Pour continuer vous devez choisir un seuil de gravite")
    print("1.Faible Gravite")
    print("2.Moyenne Gravite")
    print("3.Haute Gravite")

    choice = int(input())

          # On commence par le soft, petite punition pour petite betises

          if choice = 1 and punition = 1
            print("Un simple advertissement devrait suffir")
                break
          elif choice = 1 and punition = 2
            print("Un mot dans le carnet ne sera pas de refus")
                break
         elif choice = 1 and punition = 3
            print("Un mot et du travail en plus devrait lui faire comprendre la lecon")
                break
          elif choice = 1 and punition = 4
            print("Un rappel a l'ordre devrait suffir")
                break

          # Ici on commence doucement a arriver sur du petit con

          elif choice = 2 and punition = 1
            print("Un advertissement verbal devrait faire l'affaire")
                break
          elif choice = 2 and punition = 2
            print("Un mot dans le carnet et du travail en plus")
                break
          elif choice = 2 and punition = 3
            print("La colle me semble appropriée")
                break
          elif choice = 2 and punition = 4
            print("Heure de colle + mot dans le carnet")
                break

          # Catégorie pour les gangster

          elif choice = 3 and punition = 1
            print("Le mot dans le carnet")
                break
          elif choice = 3 and punition = 2
            print("L'exclusion de cours et le mot dans le carnet")
                break
          elif choice = 3 and punition = 3
            print("Une colle, et une exclusion de cours, sur son mot dans le carnet")
                break
          elif choice = 3 and punition = 4
            print ("Bravo l'éléve a gagné un aller chez le cpe")
                break
