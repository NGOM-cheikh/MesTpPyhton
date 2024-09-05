#Exo1 calcul.py

def addition(a: float, b: float) -> float:
    """
    Retourne la somme de deux nombres.

    :param a: Le premier nombre
    :param b: Le second nombre
    :return: La somme des deux nombres
    """
    return a + b


def soustraction(a: float, b: float) -> float:
    """
    Retourne la différence entre deux nombres.

    :param a: Le premier nombre
    :param b: Le second nombre
    :return: La différence entre les deux nombres
    """
    return a - b


def multiplication(a: float, b: float) -> float:
    """
    Retourne le produit de deux nombres.

    :param a: Le premier nombre
    :param b: Le second nombre
    :return: Le produit des deux nombres
    """
    return a * b


def division(a: float, b: float) -> float:
    """
    Retourne le quotient de la division de deux nombres.

    :param a: Le premier nombre
    :param b: Le second nombre
    :return: Le quotient de la division
    :raises ZeroDivisionError: Si le second nombre est zéro
    """
    if b == 0:
        raise ZeroDivisionError("Division par zéro non autorisée.")
    return a / b

# Exo2
# main.py

import calcul

def main() -> None:
    """
    Fonction principale pour effectuer des calculs de base en utilisant le module calcul.
    """
    nombre1: float = 10.0
    nombre2: float = 5.0

    # Utilisation des fonctions du module calcul
    print(f"Addition : {nombre1} + {nombre2} = {calcul.addition(nombre1, nombre2)}")
    print(f"Soustraction : {nombre1} - {nombre2} = {calcul.soustraction(nombre1, nombre2)}")
    print(f"Multiplication : {nombre1} * {nombre2} = {calcul.multiplication(nombre1, nombre2)}")
    print(f"Division : {nombre1} / {nombre2} = {calcul.division(nombre1, nombre2)}")

if __name__ == "__main__":
    main()
