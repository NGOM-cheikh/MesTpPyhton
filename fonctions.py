# Exo1
import math

# Créer une fonction square_root prenant un nombre en paramètre, et retournant la racine carrée de ce nombre.
def square_root(nombre):
    return math.sqrt(nombre)

# Printer l'appel de la fonction avec un nombre donné
print(square_root(25))  # Affiche 5.0

# Exo2
# Créer une fonction extendator ne prenant aucun paramètre, et qui ne retourne rien.
# Faire en sorte qu'elle modifie la liste suivante définie dans l'espace global en l'étendant de la liste suivante [4, 5, 6]

liste_depart = [1, 2, 3]

def extendator():
    global liste_depart
    liste_depart.extend([4, 5, 6])

# Appel de la fonction
extendator()
print(liste_depart)  # Affiche [1, 2, 3, 4, 5, 6]

# Exo3
# Créer une fonction add prenant en paramètres deux nombres et qui retourne l'addition de ses deux nombres.
def add(a, b):
    return a + b

# Créer une fonction carre qui prend un nombre en paramètre et retourne ce dernier élevé au carré.
def carre(nombre):
    return nombre ** 2

# A l'aide de ces deux fonctions, retourner la somme des carrés de 2 et 3 (2² + 3²).
resultat = add(carre(2), carre(3))

# Printer le résultat.
print(resultat)  # Affiche 13

# Exo4
# Le labyrinthe
# Partant de maze[0][0] (8) dans le labyrinthe, créer une fonction récursive capable de trouver la sortie (9).
# Les 0 présents dans le labyrinthe sont les murs infranchissables.
# Les 1 sont des chemins possibles. Parcours en diagonale interdit.

maze = [[8, 1, 1, 1, 1, 0],  # 0
        [1, 0, 1, 0, 1, 0],  # 1
        [1, 0, 1, 1, 1, 1],  # 2
        [1, 0, 0, 0, 1, 0],  # 3
        [1, 1, 1, 0, 1, 0],  # 4
        [0, 1, 0, 0, 1, 9]]  # 5


def trouver_sortie(maze, x, y, visited):
    # Si la position est hors des limites du labyrinthe, ou si elle est un mur, retourner False.
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 0 or (x, y) in visited:
        return False

    # Si la position actuelle est la sortie, retourner True.
    if maze[x][y] == 9:
        return True

    # Marquer la position actuelle comme visitée.
    visited.add((x, y))

    # Vérifier les directions : haut, bas, gauche, droite.
    if (trouver_sortie(maze, x + 1, y, visited) or  # Bas
            trouver_sortie(maze, x - 1, y, visited) or  # Haut
            trouver_sortie(maze, x, y + 1, visited) or  # Droite
            trouver_sortie(maze, x, y - 1, visited)):  # Gauche
        return True

    # Si aucune direction ne mène à la sortie, retourner False.
    return False


# Appel de la fonction pour trouver la sortie du labyrinthe.
visited = set()
if trouver_sortie(maze, 0, 0, visited):
    print("Sortie trouvée!")
else:
    print("Aucune sortie possible.")

