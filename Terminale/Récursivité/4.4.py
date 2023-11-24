def bouge(x, y):
    # Vérification qu'il y a un pion disponible dans la tour x
    if hanoi[x]:
        # Vérification que le pion peut aller sur la tour y (tour y vide ou pion supérieur plus petit)
        if not hanoi[y] or hanoi[x][-1] < hanoi[y][-1]:
            # Déplacement du pion de la tour x vers la tour y
            pion = hanoi[x].pop()
            hanoi[y].append(pion)
            # Mise à jour de la hanoi_vision pour refléter l'état du jeu
            hanoi_vision[x] = hanoi_vision[x][:-1]  # Enlève le pion supérieur de la tour x
            hanoi_vision[y] += pion  # Ajoute le pion supérieur à la tour y
            print(f"Le pion {pion} a été déplacé de la tour {x} vers la tour {y}.")
        else:
            print("Erreur : le pion ne peut pas aller sur la tour spécifiée.")
    else:
        print("Erreur : aucune pion disponible dans la tour spécifiée.")


# Programme principal
hanoi = [[3, 2, 1], [], []]  # Représentation des tours de Hanoï
hanoi_vision = ["|321|", "|   |", "|   |"]  # Représentation visuelle de l'état du jeu

# Test de déplacement des pions de la tour de gauche vers la tour de droite
bouge(0, 2)  # Déplace le pion supérieur de la tour 0 vers la tour 2
bouge(0, 2)  # Déplace le pion supérieur de la tour 0 vers la tour 2
bouge(0, 2)  # Déplace le pion supérieur de la tour 0 vers la tour 2

def deplace2pions(depart, arrivee, intermediaire):
    # Déplacement du premier pion de la tour de départ vers la tour intermédiaire
    bouge(depart, intermediaire)
    
    # Déplacement du deuxième pion de la tour de départ vers la tour d'arrivée
    bouge(depart, arrivee)
    
    # Déplacement du premier pion de la tour intermédiaire vers la tour d'arrivée
    bouge(intermediaire, arrivee)


# Programme principal
hanoi = [[3, 2, 1], [], []]  # Représentation des tours de Hanoï
hanoi_vision = ["|321|", "|   |", "|   |"]  # Représentation visuelle de l'état du jeu

# Déplacement des 3 pions de la tour de gauche vers la tour de droite en utilisant la tour du milieu
deplace2pions(0, 2, 1)
deplace2pions(0, 2, 1)
deplace2pions(0, 2, 1)

def deplaceNpions(n, depart, arrivee, intermediaire):
    if n == 2:
        deplace2pions(depart, arrivee, intermediaire)
    else:
        deplaceNpions(n-1, depart, intermediaire, arrivee)
        bouge(depart, arrivee)
        deplaceNpions(n-1, intermediaire, arrivee, depart)


# Programme principal
hanoi = [[5, 4, 3, 2, 1], [], []]  # Représentation des tours de Hanoï
hanoi_vision = ["|54321|", "|     |", "|     |"]  # Représentation visuelle de l'état du jeu

# Déplacement des 5 pions de la tour de gauche vers la tour de droite en utilisant la tour du milieu
deplaceNpions(5, 0, 2, 1)

