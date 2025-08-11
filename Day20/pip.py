#Exercice
#1 (read url)
import requests
from collections import Counter
import re
def common_word (url, top_n =10):
    url_read = requests.get(url)
    url_text = url_read.text
    word = re.findall(r'\b\w+\b', url_text)
    word_count = Counter(word)
    return word_count.most_common(top_n)
url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
print(common_word(url, 10))


#2
import requests
import statistics
from collections import Counter

def cat_breed_stats():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)
    breeds = response.json()

    weights = []
    lifespans = []
    countries = []

    for breed in breeds:

        weight_range = breed["weight"]["metric"].split(" - ")
        avg_weight = (float(weight_range[0]) + float(weight_range[1])) / 2
        weights.append(avg_weight)

        life_range = breed["life_span"].split(" - ")
        avg_life = (float(life_range[0]) + float(life_range[1])) / 2
        lifespans.append(avg_life)

        countries.append(breed.get("origin", "Unknown"))
    print("Poids (kg) → min:", min(weights), "max:", max(weights),
          "moyenne:", statistics.mean(weights), "médiane:", statistics.median(weights),
          "écart type:", statistics.stdev(weights))
    
    print("Durée de vie (ans) → min:", min(lifespans), "max:", max(lifespans),
          "moyenne:", statistics.mean(lifespans), "médiane:", statistics.median(lifespans),
          "écart type:", statistics.stdev(lifespans))
    print("Pays d'origine les plus fréquents :")

    for country, count in Counter(countries).most_common(10):
        print(country, ":", count)

cat_breed_stats()


#3
import requests
from collections import Counter

def country_data():
    url = "https://restcountries.com/v2/all"
    response = requests.get(url)
    countries = response.json()

    # 10 pays les plus grands
    largest_countries = sorted(countries, key=lambda x: x.get("area", 0), reverse=True)[:10]
    print("\n🌍 10 pays les plus grands :")
    for c in largest_countries:
        print(c["name"], "-", c.get("area", 0), "km²")

    # Compter les langues
    languages = []
    for c in countries:
        langs = c.get("languages", [])
        for l in langs:
            languages.append(l["name"])

    # 10 langues les plus parlées
    lang_count = Counter(languages)
    print("\n🗣️ 10 langues les plus parlées :")
    for lang, count in lang_count.most_common(10):
        print(lang, "-", count, "pays")

    # Nombre total de langues uniques
    print("\nNombre total de langues :", len(set(languages)))

country_data()


#4
import requests
from bs4 import BeautifulSoup

def scrape_uci_datasets():
    url = "https://archive.ics.uci.edu/ml/datasets.php"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erreur de téléchargement :", response.status_code)
        return

    soup = BeautifulSoup(response.content, "html.parser")

    datasets = []
    for link in soup.find_all("p", {"class": "normal"}):
        a_tag = link.find("a")
        if a_tag and a_tag.get("href"):
            dataset_name = a_tag.text.strip()
            dataset_link = "https://archive.ics.uci.edu/ml/" + a_tag.get("href")
            datasets.append((dataset_name, dataset_link))

    # Afficher les 10 premiers datasets
    for name, link in datasets[:10]:
        print(f"{name} → {link}")

scrape_uci_datasets()
