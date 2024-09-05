# Exo1
# Printer le nombre 5 à partir de la liste suivante
liste = [1, 2, [3, 4, [5, 6, 7]]]
print(liste[2][2][0])  # Affiche 5

# A l'aide d'une slice, extrayez 3 et 4
print(liste[2][0:2])  # Affiche [3, 4]

# Exo2
# A partir du texte suivant, créer une liste contenant chacune des phrases
# Créer une slice regroupant les phrases du texte en inversant leur ordre d'apparition
# Joindre la slice avec un antislash pour séparateur et printer le résultat

texte = ("Les Cucurbitaceae (Cucurbitacées) sont une famille de plantes dicotylédones de l'ordre des Cucurbitales, "
         "originaires pour la plupart des régions tropicales et subtropicales, qui comprend environ 800 espèces réparties en 180 genres. "
         "Ce sont généralement des plantes herbacées, annuelles ou vivaces, à port rampant ou grimpant, aux tiges munies de vrilles, et plus rarement des arbustes. "
         "Ces plantes sont sensibles au gel. "
         "Les fleurs sont unisexuées, portées parfois par les mêmes plantes (monoïques), parfois par des plantes différentes (dioïques). "
         "Les fruits sont le plus souvent des baies modifiées appelées péponides, plus rarement des fruits secs (capsules, samares). "
         "De nombreuses espèces sont cultivées pour leur fruits comestibles (courges, courgettes, concombres, cornichons, doubeurres, melons, pastèques, chayotes, etc.) "
         "et parfois pour leurs graines (courge à huile, pistache africaine). "
         "Leur domestication est très ancienne et remonte à plusieurs milliers d'années, tant dans le Nouveau Monde (Cucurbita, Sechium) que dans l'Ancien (Citrullus, Cucumis, Lagenaria, Luffa, Albanus Quénetus).")

# Création de la liste des phrases
phrases = texte.split('. ')

# Création de la slice inversée
phrases_inversees = phrases[::-1]

# Joindre la slice avec un antislash pour séparateur et printer le résultat
resultat =" \\" .join(phrases_inversees)
print(resultat)

# Exo3
# Insérer 2 en dernier élément de la liste
# Insérer 31 en premier élément de la liste
# Insérer 100 au milieu de la liste (doit fonctionner quelque soit la longueur de la liste)
# Printer la liste obtenue

li = [23, 12, 7, 38, 90, 9, 1, 0]

# Insertion de 2 en dernier élément
li.append(2)

# Insertion de 31 en premier élément
li.insert(0, 31)

# Insertion de 100 au milieu de la liste
milieu = len(li) // 2
li.insert(milieu, 100)

# Printer la liste obtenue
print(li)

# Créer un objet filter, qui ne retient de la liste que les éléments inférieurs ou égaux à 30
filtered_list = filter(lambda x: x <= 30, li)

# Printer l'objet sous forme d'une liste
print(list(filtered_list))
