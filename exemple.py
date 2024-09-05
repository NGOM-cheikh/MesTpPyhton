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

    @classmethod
    def esperance_vie(cls):
        return 10  # Renvoie une espérance de vie moyenne en années

    def __str__(self):
        # Retourne une chaîne de caractères avec le nom et l'âge de l'animal
        return f"{self.nom} ({self.age} ans)"
