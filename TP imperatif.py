import re
from collections import Counter
from quote import quote


# Fonction pour extraire et nettoyer les citations
def extract_citations(author: str, limit: int = 30):
    quotes = quote(author, limit=limit)
    return [q['quote'] for q in quotes]


# Fonction pour dresser l'inventaire des titres de livres classés par fréquence d'apparition
def inventory_titles(quotes):
    titles = [quote['book']
    for quote in quotes
    if quote['book']]
    title_counts = Counter(titles)
    return title_counts.most_common()


# Fonction pour nettoyer les citations et enlever la ponctuation
def clean_citation(citation: str):
# Enlever la ponctuation en utilisant une expression régulière
    cleaned = re.sub(r'[^\w\s]', '', citation)
# Convertir en minuscules
    cleaned = cleaned.lower()
    return cleaned


# Fonction pour dresser l'inventaire des mots classés par fréquence d'apparition
def inventory_words(quotes):
    word_counts = Counter()
    for citation in quotes:
        cleaned_citation = clean_citation(citation)
        words = cleaned_citation.split()
        word_counts.update(words)

# Exclure les mots présents moins de 5 fois
    frequent_words = {word: count
    for word, count in word_counts.items()
        if count >= 5}
    return sorted(frequent_words.items(), key=lambda x: x[1], reverse=True)


# Extraction des citations d'Edgar Allan Poe
citations = extract_citations("Edgar Allan Poe", limit=30)

# 1. Inventaire des titres de livres
title_inventory = inventory_titles(citations)
print("Inventaire des titres de livres classés par fréquence d'apparition :")
for title, count in title_inventory:
    print(f"{title}: {count} fois")

# 2. Inventaire des mots
word_inventory = inventory_words(citations)
print("\nInventaire des mots classés par ordre décroissant de présence :")
for word, count in word_inventory:
    print(f"{word}: {count} fois")

