
ListeDesLettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #Liste des lettres

# ---------- Programme en python ----------

incrementation = 2  # variable qui présente le pas d'incrémentation

def melange_cartes(ancien_ensemble, incrementation):  # fonction pour mélanger et ramasser les cartes jusqu'à ce qu'il reste une seule carte dans l'ancien ensemble
    nouveau_ensemble = []  # initialisation du nouveau ensemble
    ensemble_temporaire = ancien_ensemble.copy()  # copie de l'ancien ensemble pour traiter ces données sans le modifier
    i = 0  # initialisation du pointeur
    while len(ensemble_temporaire) != 0:  # répétition du traitement jusqu'à ce qu'il ne reste aucune carte
        carte_actuelle = ensemble_temporaire[i]  # Spécification de la carte sur laquelle se trouve actuellement le pointeur pour faciliter les traitements ultérieurs
        ensemble_temporaire.remove(carte_actuelle)  # Supprimer la carte actuelle de la collection temporaire (pour ne pas avoir à revenir à la même carte plus tard)
        nouveau_ensemble.append(carte_actuelle)  # ajout de la carte actuelle dans le nouveau ensemble
        i += incrementation - 1  # incrémentation du compteur pour déplacer le pointeur
        if len(ensemble_temporaire) != 0:  # vérification du nombre des éléments de l'ensemble actuel pour éviter modulo 0
            i = i % len(ensemble_temporaire)  # recalibrage du compteur pour qu'il reste dans la range 0-(len(ensemble_temporaire)) en calculant le modulo
    return nouveau_ensemble  # Ramène le nouveau groupe qui a été mixé

def main():
    N = input("Nombre de mélanges par l'utilisateur : ")  # saisie du nombre N de mélanges par l'utilisateur
    if N.isdigit():  # vérification que N est un nombre entier
        ensembleDeCartes = ListeDesLettres.copy()  # copie de la liste de base pour garder l'originale intacte
        for i in range(int(N)):  # répétition du mélange N fois
            ensembleDeCartes = melange_cartes(ensembleDeCartes, incrementation)  # le mélange de l'ensemble
            print("Ensemble " + str(i+1) + " : = " + str(ensembleDeCartes))
        print("Pour " + str(N) + " ensembles : " + str(ensembleDeCartes))
        return ensembleDeCartes  # retourne l'ensemble de cartes après N mélanges
    else:  # Dans le cas où l'utilisateur saisi un autre chose qu'un nombre entier
        print("Veuillez saisir un entier.")
        return

main()
