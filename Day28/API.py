#Exercices

import requests

answer = requests.get("google.com")
print(answer.status_code)


# mon petit resume sur la comprhension du cours

with open("resumer.txt", "w", encoding="utf-8") as fichier:
    fichier.write("un API (Application Programming Interface) est une interface qui permet a deux programmes de communiquer entre eux\n")
    fichier.write("je peut le considerer comme un serveur qui interfere entre le client et la base de donne\n")
    fichier.write("HTTP (Hyper Text Transfert Protocol) est le langage de communication entre un navigateur et un serveur\n")
    fichier.write("Tu tape une adresse , elle envoie une requet HTTP au serveur , qui a son tour renvoie une reponse http \n")
    fichier.write("quand le statut code de la reponse est 200 cela veut dire que tout est bon mais si c'est 404 alors not found \n" \
    "pour plus de precision sue les status code, on peut se rendre sur le site https://httpstatusdogs.com/")