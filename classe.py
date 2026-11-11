#fichier contenant les classes

class Camp:
    def __init__(self, nb_jours = 0, nb_personnes_total = 0, budget_jour_personne = 0, nb_pers_tranche = [0, 0, 0]):
        self.nb_jours = nb_jours
        self.nb_personnes_total = nb_personnes_total
        self.budget_jour_personne = budget_jour_personne
        self.nb_pers_tranche = nb_pers_tranche
        self.budget = self.nb_jours * self.nb_personnes_total * self.budget_jour_personne
    
    def calcule_portion(self):
        portion = self.nb_pers_tranche[0] * 0.8 + self.nb_pers_tranche[1] * 1 + self.nb_pers_tranche[2] * 1.1
        return portion

    def deduire_cout(self, cout):
        self.budget -= cout


class Recette:
    def __init__(self, nom_recette : str, nbr_ingredients : int):
        self.nom_recette = nom_recette
        self.nbr_ingredients = nbr_ingredients

        self.ingredient = []

    def ajout_ingredient(self):
        if len(self.ingredient) == 0:
            for i in range(self.nbr_ingredients):
                nom = str(input("le nom de l'ingédient ? : "))
                prix = float(input("son prix ? : "))
                paquet = int(input("quelle est sa taille ? : "))
                est_frais = bool(input("est-il frais ? (True ou False) : "))

                ing = Ingredient(nom, prix, paquet, est_frais)
                self.ingredient.append(ing)
        else:
            nom = str(input("le nom de l'ingédient ? : "))
            prix = float(input("son prix ? : "))
            paquet = int(input("quelle est sa taille ? : "))
            est_frais = bool(input("est-il frais ? (True ou False) : "))
            ing = Ingredient(nom, prix, paquet, est_frais)
            self.ingredient.append(ing)
            self.nbr_ingredients += 1


    def supprimer_ingredient(self, ingre):
        temp_l = []
        for i in self.ingredient:
            if i.nom != ingre:
                temp_l.append(i)
        self.ingredient = temp_l
        self.nbr_ingredients = len(temp_l)

    def __str__(self):
        return f"La recette {self.nom_recette} contient {self.nbr_ingredients} ingrédients."

        
class Ingredient : 
    def __init__(self,nom : str, prix : float, paquets : int, est_frais : bool):
        self.nom = nom
        self.prix = prix
        self.paquets = paquets
        self.est_frais = est_frais

    def __str__(self):
        return f"L'ingrédient : {self.nom} coûte {self.prix}, s'achète par paquet de {self.paquets}, est frais : {self.est_frais}"   


class Menu:
    def __init__(self):
        self.all_recette = []

    def cacul_cout(self,recette):
        """
        Calcule le coût total des ingrédients d'une recette

        Input: recette est un objet recette
        Output: cout est un nombre (float)

        PRE:
            - recette.ingredient est une liste d'Ingrédient
            - le prix de chaque ingrédient est un nombre positif

        POST:
            - retourne la somme des prix de tous les ingrédients
            - retourne 0 si la recette n'a pas d'ingrédient
                (vu que de base mon variable cout commence par 0 )
            - la recette n'est pas modifiée
                (car on ne fait pas d'append ni de remove juste on lit l'info et on le prend pour le calcul du coût)

        """
        cout = 0
        for i in recette.ingredient:
            cout += i.prix
        return cout

    def contient_frais(self, recette):
        """
        Il indique si la recette contient au minimum un ingrédient frais

        Input: recette est un objet recette
        Output: Booléen

        PRE:
            - recette.ingredient est une liste d'Ingrédient
            - l'attribut est_frais de chaque ingrédient est un booléen

        POST:
            - retourne True si un des ingrédients contient True à est_frais
            - retourne False si tous les ingrédients contient False à est_frais
            - retourne False si la recette n'a aucun ingrédient
            - la recette n'est pas modifiée (car on ne fait pas de modification juste de la lecture)

        """
        for i in recette.ingredient:
            if i.est_frais == True:
                return True
            else:
                return False

    def ajout_recette(self, new_recette):
        self.all_recette.append(new_recette)
        return 'La recette a bien été ajouter au menu'

    def supprime_recette(self, old_recette):
        """
        Suppression d'une recette du menu

        Input: old_recette est un objet recette
        Output: Un message de confirmation est affiche si la suppression a réussi

        PRE:
            - old_recette est un objet Recette
            - self.all_recette est une liste de recettes
            - old_recette doit être unique lors de l'ajout de la recette

        POST:
            - si dans old_recette est dans self.all_recette alors on déplace tous les recettes
                sauf la old_recette et on écrase l'ancien self.all_recette avec la nouvelle en mettant un message de confirmation

            - si dans old_recette ne se trouve pas dans self.all_recette alors la méthode retourne "erreur"

        """

        temporaire = []
        for i in self.all_recette:
            if i != old_recette:
                temporaire.append(i)
        if len(temporaire) < len(self.all_recette):
            self.all_recette = temporaire
            return "La recette a bien ete supprime de la liste"
        return 'erreur'

    def __str__(self): # en cours
        return f"Le menu contient {len(self.all_recette)} recettes"