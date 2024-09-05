#Exo3
# Liste des couleurs (format RGB ou RGBA)
colors = [
    (12, 72, 89),       # RGB
    (23, 77, 200, 1),   # RGBA
    (0, 0, 0),          # RGB de couleur noire
    (123, 123, 67, 1),  # RGBA
    (255, 255, 255, 0), # RGBA
    (255, 255, 255, 1), # RGBA de couleur blanche
    (0, 0, 0, 0)        # RGBA
]

# Boucle pour traiter chaque couleur
for color in colors:
    match color:
        case (r, g, b):  # Cas RGB
            if r == 0 and g == 0 and b == 0:
                print("RGB de couleur noire")
            elif r == 255 and g == 255 and b == 255:
                print("RGB de couleur blanche")
            else:
                print("RGB")
        case (r, g, b, a):  # Cas RGBA
            if r == 0 and g == 0 and b == 0 and a > 0:
                print("RGBA de couleur noire")
            elif r == 255 and g == 255 and b == 255 and a > 0:
                print("RGBA de couleur blanche")
            else:
                print("RGBA")
