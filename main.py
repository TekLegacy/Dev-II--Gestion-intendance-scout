#fichier contenant le script
from classe import Recette, Ingredient, Camp, Menu

#fait par nathan
nbr_personnes = int(input("Combien de personnes vont au camp ? : "))
camp= Camp(nb_personnes_total = nbr_personnes)

#fait par Hatim
# ajout tempo recette
menu = Menu()
menu.ajout_recette(Recette("Salade",2))
menu.ajout_recette(Recette("Pizza",3))
menu.ajout_recette(Recette("Pate",1))
menu.ajout_recette(Recette("Boulette",1))
menu.ajout_recette(Recette("Burger",2))


# affichage recette avec numerotation
numerotation_recette = 1
for recette in menu.all_recette:
    print(f"{numerotation_recette}. {recette.nom_recette}")
    numerotation_recette += 1

#fait par Louis
for i in menu.all_recette:
    i.ajout_ingredient()

chiffre_choisi = int(input("Choisir le numéro d'une recette : ")) - 1
recette_choisi = menu.all_recette[chiffre_choisi]

cout = menu.calcul_cout(recette_choisi)

cout_tot = cout * camp.nb_personnes_total
print(cout_tot)

#fait par Antonin
def calcul_quantite(recette, nombre_personnes): 
    '''
    Calcul la quantite total d'ingredient pour une recette choisie. 
    
    PRE:
        -recette est une objet RECETTE correspond a la recette choisie. 
        -nombre_personne est un entier provenant de la classe CAMP correspond au nombre total de personne presente au camp.  
    POST:
        -retourne un dictionnaire contenant chaque nom d'ingredient present dans la recette et la quantite a acheter pour la recette choisie.
    
    '''
    quantites= {}
    for ingredient in recette.ingredient:
        quantite_totale = ingredient.paquets * nombre_personnes
        quantites[ingredient.nom] = quantite_totale
    return quantites

print(calcul_quantite(recette_choisi, camp.nb_personnes_total))
