
1# Demander à un utilisateur de taper un mot
mot = input("Veuillez entrer un mot : ")

# Vérifier si le mot contient la lettre 'e' ou la lettre 'a'
contient_e = 'e' in mot
contient_a = 'a' in mot

# Afficher "Beep" si le mot contient 'e' ou 'a', ou "Boop" si le mot contient 'e' ou 'a' mais pas les deux en même temps
if contient_e or contient_a:
    if contient_e and contient_a:
        print("Beep")
    else:
        print("Boop")




2# Liste des couleurs (format RGB ou RGBA)
couleurs = [
    (255, 0, 0),       # RGB (Red)
    (0, 255, 0, 128),  # RGBA (Green, with 50% transparency)
    (0, 0, 0),         # RGB (Black)
    (0, 0, 255, 255),  # RGBA (Blue, fully opaque)
    (0, 0, 255, 0),    # RGBA (Blue, fully transparent)
    (255, 255, 255, 128),  # RGBA (White, with 50% transparency)
    (255, 255, 255, 255)   # RGBA (White, fully opaque)
]

# Boucle pour traiter chaque couleur
for couleur in couleurs:
    match couleur:
        case (r, g, b):
            if r == 0 and g == 0 and b == 0:
                print("RGB de couleur noire")
            elif r == 255 and g == 255 and b == 255:
                print("RGB de couleur blanche")
            else:
                print("RGB")
        case (r, g, b, a):
            if r == 0 and g == 0 and b == 0 and a > 0:
                print("RGBA de couleur noire")
            elif r == 255 and g == 255 and b == 255 and a > 0:
                print("RGBA de couleur blanche")
            else:
                print("RGBA")
