# Projet : Password Manager

# Step 1 : Menu
def menu():
    print("\n=== Password Manager ===")
    print("1. Ajouter un mot de passe")
    print("2. Voir les mots de passe enregistrés")
    print("3. Supprimer un mot de passe")
    print("4. Rechercher un mot de passe")
    print("5. Quitter")
    choix = input("Choisir une option (1-5): ")
    return choix

# Ajouter un mot de passe
def ajout_de_mot_de_passe():
    site_ou_apk = input("Entrer le nom de l'application ou l'URL du site : ")
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    with open("Password_Manager.txt", "a") as f:
        f.write(f"{site_ou_apk} | {username} | {password}\n")
    print("Mot de passe enregistré avec succès.\n")

# Voir les mots de passe enregistrés
def voir_mot_de_passe_enregistrer():
    try:
        with open("Password_Manager.txt", "r") as f:
            contenu = f.readlines()
            if contenu:
                print("\n=== Mots de Passe Enregistrés ===")
                for i, ligne in enumerate(contenu, 1):
                    print(f"{i}. {ligne.strip()}")
                print()
            else:
                print("Aucun mot de passe enregistré.\n")
    except FileNotFoundError:
        print("Aucun mot de passe enregistré dans la base de données.\n")

# Supprimer un mot de passe
def supprimer_mot_de_passe():
    try:
        with open("Password_Manager.txt", "r") as f:
            contenu = f.readlines()

        if not contenu:
            print("Aucun mot de passe à supprimer.\n")
            return

        print("\n=== Mots de Passe ===")
        for i, ligne in enumerate(contenu, 1):
            print(f"{i}. {ligne.strip()}")

        choix = int(input("Entrez le numéro du mot de passe à supprimer : "))
        if 1 <= choix <= len(contenu):
            contenu.pop(choix - 1)
            with open("Password_Manager.txt", "w") as f:
                f.writelines(contenu)
            print("Mot de passe supprimé avec succès.\n")
        else:
            print("Numéro invalide.\n")
    except FileNotFoundError:
        print("Aucun mot de passe à supprimer.\n")
    except ValueError:
        print("Veuillez entrer un numéro valide.\n")

# Rechercher un mot de passe
def rechercher_mot_de_passe():
    try:
        with open("Password_Manager.txt", "r") as f:
            contenu = f.readlines()

        if not contenu:
            print("Aucun mot de passe enregistré.\n")
            return

        recherche = input("Entrez le nom du site ou de l'application à rechercher : ").lower()
        resultats = [ligne.strip() for ligne in contenu if recherche in ligne.lower()]

        if resultats:
            print("\n=== Résultats de la recherche ===")
            for i, ligne in enumerate(resultats, 1):
                print(f"{i}. {ligne}")
            print()
        else:
            print("Aucun mot de passe trouvé pour cette recherche.\n")
    except FileNotFoundError:
        print("Aucun mot de passe enregistré.\n")

# Step 2 : Boucle principale
while True:
    choix = menu()

    if choix == "1":
        ajout_de_mot_de_passe()
    elif choix == "2":
        voir_mot_de_passe_enregistrer()
    elif choix == "3":
        supprimer_mot_de_passe()
    elif choix == "4":
        rechercher_mot_de_passe()
    elif choix == "5":
        print("Merci d'avoir utilisé Password Manager.")
        break
    else:
        print("Option invalide, retournez voir les options du menu.\n")
