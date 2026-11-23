#fichier contenant le script
from classe import Recette, Ingredient, Camp, Menu
import json
import  tkinter as tk

def nb_personnes() -> None:
    
    nbr_personnes = int(champ_personnes.get().strip())

    if nbr_personnes <= 0:
        raise ValueError("Aucune personne n'est présente au camp.")

    global camp
    camp = Camp(nb_personnes_total = nbr_personnes)

    affichage_recette()




def affichage_recette() -> None:
    global menu
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

    string_recette = "Recettes disponible :\n \n"
    compteur_recette_numero = 1
    for i in menu.all_recette :
        string_recette += f"{compteur_recette_numero}. {i.nom_recette}\n"
        compteur_recette_numero += 1

    resultat.config(text=string_recette)

    zone_depart.pack_forget()
    fin_affichage()


def recommencer() -> None:
    zone_bas.forget()
    zone_milieux_haute.forget()
    champ_personnes.delete(0, tk.END)
    choix_recette.delete(0, tk.END)
    resultat.config(text="")
    resultat_cout.config(text="")
    resultat_quantite.config(text="")
    zone_recette.pack_forget()

    zone_depart.pack(side="top", padx=20, pady=25)


def recette_choisi() -> None:

    chiffre_choisi = int(choix_recette.get().strip()) - 1
    if chiffre_choisi < 0 or chiffre_choisi >= len(menu.all_recette):
        raise ValueError(f"La recette {chiffre_choisi + 1} n'existe pas")
    recette_choisi = menu.all_recette[chiffre_choisi]

    cout = menu.calcul_cout(recette_choisi)

    cout_tot = cout * camp.nb_personnes_total
    quantite = menu.calcul_quantite(recette_choisi, camp.nb_personnes_total)

    affichage_quantite = "Quantité nécessaire :\n"

    for i in quantite:
        affichage_quantite += f"{i} : {quantite[i]} \n"
    
    resultat_cout.config(text=f"Coût total : {cout_tot}")
    resultat_quantite.config(text=f"{affichage_quantite}")
 


if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Intedance Scout")


    zone_depart = tk.Frame(fenetre)
    zone_depart.pack(padx=20, pady=25)

    phrase_personnes = tk.Label(zone_depart, text="Combien de personnes sont présentes au camp ? \n")
    phrase_personnes.pack(side="top", padx=20)

    champ_personnes = tk.Entry(zone_depart, width=25)
    champ_personnes.pack(side="left", padx=25)

    bouton_personne = tk.Button(zone_depart, text="Valider", command=nb_personnes)
    bouton_personne.pack(side="left", padx=10)



    zone_recette = tk.Frame(fenetre)
    zone_recette.pack(padx=20, pady=25)

    resultat = tk.Label(zone_recette, text="")
    resultat.pack(padx=10, pady=10)

    def fin_affichage() -> None:
        global choix_recette, resultat_cout, resultat_quantite, zone_bas, zone_milieux_haute

        zone_milieux_haute = tk.Frame(fenetre)
        zone_milieux_haute.pack(padx=20, pady=25)

        phrase_recette = tk.Label(zone_milieux_haute, text="Numéro de la recette souhaitée : \n")
        phrase_recette.pack(side="top", padx=20)

        choix_recette = tk.Entry(zone_milieux_haute, width=20)
        choix_recette.pack(side="left", padx=25)

        bouton_recette = tk.Button(zone_milieux_haute, text="Valider", command=recette_choisi)
        bouton_recette.pack(side="left", padx=25)

        zone_bas = tk.Frame(fenetre)
        zone_bas.pack(padx=20, pady=25)

        resultat_cout = tk.Label(zone_bas, text="")
        resultat_cout.pack(padx=10, pady=10)

        resultat_quantite = tk.Label(zone_bas, text="")
        resultat_quantite.pack(padx=10, pady=10)

        bouton_recommencer = tk.Button(zone_bas, text="Changez le nombre de personnes", command=recommencer)
        bouton_recommencer.pack(side="top", pady=10)
        
        bouton_quitter = tk.Button(zone_bas, text="Quitter", command=fenetre.destroy)
        bouton_quitter.pack(side="top", pady=10)
  
    fenetre.mainloop()



