#Étape 1 - Création de la classe
#Étape 2 - Le constructeur
#Étape 3 - Méthode

#Étape 5 - Méthode statique
#Étape 6 - Méthode de classe
#Étape 7 - Méthode magique
class Animal:
    population = 0  # Propriété statique, initialisée à zéro

    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
        Animal.population += 1  # Incrémente la population à chaque création d'animal

    def crier(self):
        pass  # La méthode reste vide pour l'instant

    @staticmethod
    def nombre_animaux():
        return Animal.population  # Renvoie la population actuelle

    def __str__(self):
        # Retourne une chaîne de caractères avec le nom et l'âge de l'animal
        return f"{self.nom} ({self.age} ans)"

#Exo8: Heritage
class Chien(Animal):
    pass

#Exo9 :Encapsulation
class Animal:
    population = 0  # Propriété statique, initialisée à zéro

    def __init__(self, nom: str, age: int):
        self._nom = nom  # Attribut privé
        self._age = age  # Attribut privé
        Animal.population += 1  # Incrémente la population à chaque création d'animal

    def crier(self):
        pass  # Méthode abstraite, à redéfinir dans les sous-classes

    @staticmethod
    def nombre_animaux():
        return Animal.population  # Renvoie la population actuelle

    @classmethod
    def esperance_vie(cls):
        return 10  # Renvoie une espérance de vie moyenne en années

    def __str__(self):
        return f"{self._nom} ({self._age} ans)"

#Exo10: Surcharge
class Chien(Animal):
    def crier(self):
        return "Woof!"  # Surcharge de la méthode crier pour les chiens
#exo11 : Abstraction
class Animal:
    population = 0  # Propriété statique, initialisée à zéro

    def __init__(self, nom: str, age: int):
        self._nom = nom  # Attribut privé
        self._age = age  # Attribut privé
        Animal.population += 1  # Incrémente la population à chaque création d'animal

    def crier(self):
        raise NotImplementedError("La méthode 'crier' doit être redéfinie dans les sous-classes.")

    @staticmethod
    def nombre_animaux():
        return Animal.population  # Renvoie la population actuelle

    @classmethod
    def esperance_vie(cls):
        return 10  # Renvoie une espérance de vie moyenne en années

    def __str__(self):
        return f"{self._nom} ({self._age} ans)"


class Chien(Animal):
    def crier(self):
        return "Woof!"  # Surcharge de la méthode crier pour les chiens
