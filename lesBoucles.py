#Exo 1
# Liste à parcourir
liste = ["bernard", "gérard", "gontran", "jacqueline", "intrus", "nadia", "jack"]

# Parcourir la liste à la recherche de l'intrus
for element in liste:
    if element == "intrus":
        print("intrus trouvé!")
        break
#Exo2
# Sans utiliser la fonction sum(), retourner la somme de la liste suivante à l'aide d'une boucle

liste_somme = [12.3, 34, 1, 0.4, 23, -17, 76, -300.2]

# Initialiser une variable pour la somme
total = 0

# Ajouter chaque élément de la liste à la somme
for nombre in liste_somme:
    total += nombre

# Printer le résultat
print(total)

#Exo3
# A l'aide d'une boucle et d'une range, calculer le factoriel de 10 (3628800)
# Le factoriel d'un entier n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n
# Printer le résultat

# Initialiser la variable factoriel
factoriel = 1

# Calculer le factoriel de 10 en multipliant les nombres de 1 à 10
for i in range(1, 11):
    factoriel *= i

# Printer le résultat
print(factoriel)
#Exo4
# A l'aide d'une boucle while, demander à l'utilisateur de "Taper oui, ou non.", et tant que ce dernier n'a pas tapé "non", continuer de lui demander "Taper oui, ou non."
# Si l'utilisateur ne tape ni "oui", ni "non", continuer la boucle en lui mettant un message d'erreur car l'input est invalide

while True:
    reponse = input("Taper oui, ou non : ").strip().lower()
    if reponse == "non":
        break
    elif reponse == "oui":
        continue
    else:
        print("Réponse invalide, veuillez taper 'oui' ou 'non'.")

#Exo5
# A partir de la liste suivante printer le résultat suivant à l'aide d'une boucle :
# "L'élément à l'index 0 est a"
# "L'élément à l'index 1 est 3"
# "L'élément à l'index 2 est True"
# ...

ma_liste = ['a', 3, True, "coucou", 'r', 3.14, [1, 2, 3]]

# Parcourir la liste avec index et printer le résultat
for index, element in enumerate(ma_liste):
    print(f"L'élément à l'index {index} est {element}")

#Exo6
# A l'aide d'une compréhension de liste générer une nouvelle liste suivant les règles suivantes :
# Si le chiffre est un multiple de 5, le multiplier par 2
# Sinon, retourner sa division entière par 3
# Printer la nouvelle liste obtenue

liste_de_base = [23, 1, 27, 28, 3, 4, 763, 12, 90]

# Utiliser une compréhension de liste pour générer la nouvelle liste
nouvelle_liste = [x * 2 if x % 5 == 0 else x // 3 for x in liste_de_base]

# Printer la nouvelle liste
print(nouvelle_liste)

#Exo7

# A l'aide d'une compréhension de liste et de all() printer une fois True ou False si toutes les chaînes de caractères contenues dans la liste sont des palindromes.

palindrome = ["kayak", "coloc", "malayalam", "pop", "erre"]

# Vérifier si toutes les chaînes sont des palindromes
toutes_palindromes = all(s == s[::-1] for s in palindrome)

# Printer le résultat
print(toutes_palindromes)


#Exo8
# A l'aide de boucles imbriquées, créer une nouvelle liste "flat", qui sera une liste aplatie de "liste", ayant les éléments classés dans l'ordre décroissant : [7, 6, 5, 4, 3, 2, 1]

liste = [1, 3, 7, [4, 6, [5, 2]]]

# Fonction pour aplatir la liste
def aplatir(l):
    result = []
    for element in l:
        if isinstance(element, list):
            result.extend(aplatir(element))
        else:
            result.append(element)
    return result

# Aplatir la liste et trier en ordre décroissant
flat = sorted(aplatir(liste), reverse=True)

# Printer le résultat
print(flat)

