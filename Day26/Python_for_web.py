#Exercice
'''
text_analyzer/
│── app.py
│── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
│── venv/   (ton environnement virtuel)
'''

from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

def analyser_texte(texte):
    texte = texte.lower()
    mots = texte.split()
    nb_mots = len(mots)
    nb_caracteres = len(texte)
    compteur = Counter(mots)
    mots_frequents = compteur.most_common(5)
    return {
        "mots": nb_mots,
        "caracteres": nb_caracteres,
        "mots_frequents": mots_frequents
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texte = request.form["texte"]
        resultats = analyser_texte(texte)
        return render_template("result.html", texte=texte, resultats=resultats)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


