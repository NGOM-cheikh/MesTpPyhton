Exo1
# A l'aide d'une boucle, parcourir la liste suivante à la recherche de l'intrus
# Une fois l'intrus trouvé, printer "intrus trouvé!" et sortir de la boucle

liste = ["bernard", "gérard", "gontran", "jacqueline", "intrus", "nadia", "jack"]

for nom in liste:
    if nom == "intrus":
        print("intrus trouvé!")
        break

Exo2
# Sans utiliser la fonction sum(), retourner la somme de la liste suivante à l'aide d'une boucle

liste_somme = [12.3, 34, 1, 0.4, 23, -17, 76, -300.2]
somme = 0

for nombre in liste_somme:
    somme += nombre

print(somme)

Exo3
# A l'aide d'une boucle et d'une range, calculer le factoriel de 10 (3628800)
# Le factoriel d'un entier n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n
# Printer le résultat

factoriel = 1

for i in range(1, 11):
    factoriel *= i

print(factoriel)

Exo4
# A l'aide d'une boucle while, demander à l'utilisateur de "Taper oui, ou non.",
# et tant que ce dernier n'a pas tapé "non", continuer de lui demander "Taper oui, ou non."
# Si l'utilisateur ne tape ni "oui", ni "non", continuer la boucle en lui mettant un message d'erreur car l'input est invalide

while True:
    reponse = input("Taper oui, ou non: ").lower()
    if reponse == "non":
        break
    elif reponse == "oui":
        continue
    else:
        print("Erreur : Réponse invalide.")

Exo5
# A partir de la liste suivante printer le résultat suivant à l'aide d'une boucle :
# "L'élément à l'index 0 est a"
# "L'élément à l'index 1 est 3"
# "L'élément à l'index 2 est True"
# ...

ma_liste = ['a', 3, True, "coucou", 'r', 3.14, [1, 2, 3]]

for index, element in enumerate(ma_liste):
    print(f"L'élément à l'index {index} est {element}")

Exo6
# A l'aide d'une compréhension de liste générer une nouvelle liste suivant les règles suivantes :
# Si le chiffre est un multiple de 5, le multiplier par 2
# Sinon, retourner sa division entière par 3
# Printer la nouvelle liste obtenue

liste_de_base = [23, 1, 27, 28, 3, 4, 763, 12, 90]

nouvelle_liste = [x * 2 if x % 5 == 0 else x // 3 for x in liste_de_base]
print(nouvelle_liste)

Exo7
# A l'aide d'une compréhension de liste et de all() printer une fois True ou False si toutes les chaînes de caractères contenues dans la liste sont des palindromes.

palindrome = ["kayak", "coloc", "malayalam", "pop", "erre"]

est_palindrome = all([mot == mot[::-1] for mot in palindrome])
print(est_palindrome)

Exo8
# A l'aide de boucles imbriquées, créer une nouvelle liste "flat", qui sera une liste applatie de "liste",
# ayant les éléments classés dans l'ordre décroissant : [7, 6, 5, 4, 3, 2, 1]

liste = [1, 3, 7, [4, 6, [5, 2]]]

flat = []

# Fonction pour aplatir la liste
def aplatir(liste):
    for element in liste:
        if isinstance(element, list):
            aplatir(element)
        else:
            flat.append(element)

aplatir(liste)
flat.sort(reverse=True)
print(flat)
