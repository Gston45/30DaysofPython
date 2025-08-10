#Exercices: Level 1
#1 (Function which count number of lines and numbers of words)
def compter_lignes_mots(fichier):
    lignes = 0
    mots = 0
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                lignes += 1
                mots += len(ligne.split())  # split() coupe la ligne en mots
        return lignes, mots
    except FileNotFoundError:
        print(f"Fichier introuvable : {fichier}")
        return 0, 0
    


#2 (Function that finds the ten most spoken languages)
import json
from collections import Counter

def most_spoken_languages(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    languages_count = Counter()
    for country in countries:
        for lang in country.get('languages', []):
            languages_count[lang] += 1
    return languages_count.most_common(top_n)

#3 ()
import json

def most_populated_countries(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    sorted_countries = sorted(countries, key=lambda x: x.get('population', 0), reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:top_n]]


#Exercices: Level 2
#4 ()
import re

def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return emails

#5 ()
from collections import Counter
import re

def find_most_common_words(file_path, top_n):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    word_count = Counter(words)
    return word_count.most_common(top_n)