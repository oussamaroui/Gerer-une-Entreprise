def ajouter_voiture():
    nomVoiture = input("Entrez le nom du voiture : ")
    couleurVoiture = input("Entrez la couleur du voiture : ")
    with open("voitures.txt", "a") as F:
        F.write(nomVoiture + ", sa couleur est : " + couleurVoiture + "\n")
    print("voiture ajouté avec succès !")


def afficher_voiture():
    with open("voitures.txt") as F:
        voitures = F.readlines()
    if voitures:
        print("Liste des voitures : ")
        for voiture in voitures:
            nom, couleur = voiture.strip().split(",")
            print(f"{nom} - {couleur}")
    else:
        print("Aucun voiture trouvé.")


def modifier_voiture():
    nomVoiture = input("Entrez le nom du voiture à modifier : ")
    new_nomVoiture = input("Entrez le nouveau nom du voiture : ")
    new_couleurVoiture = input("Entrez la nouvelle couleur du voiture : ")
    with open("voitures.txt") as F:
        voitures = F.readlines()
    with open("voitures.txt", "w") as F:
        for voiture in voitures:
            nom, couleur = voiture.strip().split(",")
            if nom == nomVoiture:
                F.write(new_nomVoiture + "," + new_couleurVoiture + "\n")
            else:
                F.write(voiture)
    print("voiture modifié avec succès !")


def rechercher_voiture():
    nomVoiture = input("Entrez le nom du voiture à rechercher : ")
    with open("voitures.txt") as F:
        voitures = F.readlines()
    trouve = False
    for voiture in voitures:
        nom, couleur = voiture.strip().split(",")
        if nom == nomVoiture:
            print(f"{nom} - {couleur}")
            trouve = True
    if not trouve:
        print("voiture non trouvé.")


def supprimer_voiture():
    nomVoiture = input("Entrez le nom du voiture à supprimer : ")
    with open("voitures.txt") as F:
        voitures = F.readlines()
    with open("voitures.txt", "w") as F:
        supprime = False
        for voiture in voitures:
            nom, couleur = voiture.split(",")
            if nom == nomVoiture:
                supprime = True
            else:
                F.write(voiture)
        if supprime:
            print("voiture supprimé avec succès !")
        else:
            print("voiture non trouvé.")


while True:
    print("Que souhaitez-vous faire ?")
    print("(1) Ajouter un voiture")
    print("(2) Afficher les voitures")
    print("(3) Modifier un voiture")
    print("(4) Rechercher un voiture")
    print("(5) Supprimer un voiture")
    print("(6) Quitter le programme")

    choice = input("Qu'aimez-vous ? :")
    if choice == "1":
        ajouter_voiture()
    elif choice == "2":
        afficher_voiture()
    elif choice == "3":
        modifier_voiture()
    elif choice == "4":
        rechercher_voiture()
    elif choice == "5":
        supprimer_voiture()
    elif choice == "6":
        print("Au Revoire :)")
        break
    else:
        print("Choix Invalide, Choisissez un Autre Numéro.")
