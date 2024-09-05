#Exo1
import pathlib
import random
from pathlib import Path

# Générer 5 entiers aléatoires entre 0 et 100
nombres_aleatoires = [random.randint(0, 100) for _ in range(5)]

# Créer le chemin complet du fichier dans le dossier 'Documents'
chemin_fichier = Path("C:/Users/lenovo/Documents/nombres_aleatoires.txt")

# Écrire les nombres aléatoires dans le fichier
with chemin_fichier.open(mode='w') as fichier:
    fichier.write(f"Voici mes 5 nombres aléatoires: {', '.join(map(str, nombres_aleatoires[:-1]))} et {nombres_aleatoires[-1]}")

# Lire et afficher le contenu du fichier
with chemin_fichier.open(mode='r') as fichier:
    contenu = fichier.read()
    print(contenu)

# Supprimer le fichier
chemin_fichier.unlink()




#Exo2
from datetime import datetime
date_naissance = "1998-04-23"
date_naissance_dt = datetime.strptime(date_naissance, "%Y-%m-%d")
date_actuelle = datetime.now()
age = date_actuelle.year - date_naissance_dt.year
if (date_actuelle.month, date_actuelle.day) < (date_naissance_dt.month, date_naissance_dt.day):
    age -= 1
print(f"L'âge de la personne est de {age} ans.")


#Exo3
import zipfile
import os
from pathlib import Path


# Creer un dossier de chaque type
mon_path =r"direction"
root = pathlib.Path( mon_path)
mon_musique = root.joinpath("musique")
mon_videos = pathlib.Path("Videos")
mon_images = pathlib.Path( "Images")
mon_documents = pathlib.Path("documents")
mon_divers = pathlib.Path("Divers")

# Chemin vers le dossier "Annexes" et l'archive "source.zip"
zip_file= zipfile.ZipFile(mon_path + r"\source.zip")
dossier_annexes = Path("Annexes")
archive_zip = dossier_annexes / "source.zip"

# Chemin vers le dossier d'extraction
dossier_extraction = dossier_annexes / "extracted_files"

# Extraire les fichiers de l'archive zip
with zipfile.ZipFile(archive_zip, 'r') as zip_ref:
    zip_ref.extractall(dossier_extraction)

# Créer les dossiers de destination
categories = {
    "Musique": [".mp3", ".wav", ".flac"],
    "Videos": [".avi", ".mp4", ".gif"],
    "Images": [".bmp", ".png", ".jpg"],
    "Documents": [".txt", ".pptx", ".csv", ".xls", ".odp", ".pages"],
    "Divers": []
}

for category in categories:
    os.makedirs(dossier_extraction / category, exist_ok=True)

# Trier les fichiers extraits dans les bons dossiers
for fichier in dossier_extraction.iterdir():
    if fichier.is_file():
        extension = fichier.suffix.lower()
        deplace = False
        for category, extensions in categories.items():
            if extension in extensions:
                fichier.rename(dossier_extraction / category / fichier.name)
                deplace = True
                break
        if not deplace:
            fichier.rename(dossier_extraction / "Divers" / fichier.name)
