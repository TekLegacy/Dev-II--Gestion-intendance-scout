from classe import Camp, Recette, Menu, Ingredient
import json

camp = Camp(nb_personnes_total = 10)

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
def afficher_recette():
    global string_recette
    string_recette = "Recettes disponible :\n \n"
    compteur_recette_numero = 1
    for i in menu.all_recette :
        string_recette += f"{compteur_recette_numero}. {i.nom_recette}\n"
        compteur_recette_numero += 1
    print(string_recette)

afficher_recette()
print("Ajout d'une recette")
menu.ajout_recette("Tomates moza", 2)
afficher_recette()
print("Suppression d'une recette")
menu.supprime_recette("Tomates moza")
afficher_recette()

def affiche_ingredient(recette_choisi):
    for i in recette_choisi.ingredient:
        print(i.nom)
    print("\n")

recette_choisi = menu.all_recette[2]
print("Ingredient avant modification :")
affiche_ingredient(recette_choisi)
recette_choisi.ajout_ingredient("fromage", 1.0, 1, True)
print("Ingredient après Ajout :")
affiche_ingredient(recette_choisi)
recette_choisi.supprimer_ingredient("fromage")
print("Ingredient après suppression :")
affiche_ingredient(recette_choisi)

