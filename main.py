#fichier contenant le script
from classe import Recette, Ingredient, Camp, Menu
import json

#fait par nathan
nbr_personnes = int(input("Combien de personnes vont au camp ? : "))
if nbr_personnes <= 0:
    raise ValueError("Aucune personne n'est présente au camp.")
camp= Camp(nb_personnes_total = nbr_personnes)

#fait par Hatim
# ajout tempo recette
menu = Menu()

fichier = open("recette.json", "r")
donnees = json.load(fichier)
recettes = donnees.get("recette", [])

compteur = 0
for i in recettes : 
    menu.ajout_recette(i, recettes[i][0])
    for j in recettes[i][1:]:
        menu.all_recette[compteur].ajout_ingredient(j["nom"], j["prix"], j["paquets"], j["est_frais"])
    compteur += 1    

compteur_recette_numero = 1
for i in menu.all_recette :
    print(compteur_recette_numero , i.nom_recette)
    compteur_recette_numero += 1

chiffre_choisi = int(input("Choisir le numéro d'une recette : ")) - 1
recette_choisi = menu.all_recette[chiffre_choisi]

cout = menu.calcul_cout(recette_choisi)

cout_tot = cout * camp.nb_personnes_total
print(cout_tot)

print(menu.calcul_quantite(recette_choisi, camp.nb_personnes_total))
 