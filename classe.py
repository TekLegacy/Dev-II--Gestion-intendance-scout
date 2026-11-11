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
        for i in range(self.nbr_ingredients):
            nom = str(input("le nom de l'ingédient ? : "))
            prix = float(input("son prix ? : "))
            paquet = int(input("quelle est sa taille ? : "))
            est_frais = bool(input("est-il frais ? (True ou False) : "))

            ing = Ingredient(nom, prix, paquet, est_frais)

            self.ingredient.append(ing)

    def supprimer_ingredient(self, ingre):
        temp_l = []
        for i in self.ingredient:
            if i.nom != ingre:
                temp_l.append(i)
        self.ingredient = temp_l
        self.nbr_ingredients = len(temp_l)

    def __str__(self):
        return f"La recette {self.nom_recette} comporte {self.nbr_ingredients} ingrédients."

        
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
        Cacule le côut total des ingrediants d'une recette

        Input: recette est un objet recette
        Output: cout est un nombre (float)

        PRE:
            - recette.ingredient est une liste d'Ingredient
            - le prix de chaque ingrédiant est un nombre positif

        POST:
            - returne la somme des prix de tous les ingrédiants
            - retourne 0 si la recette n'a pas d'ingrédiant (vu que de base mon variable cout commence par 0 )
            - la recette n'est pas modifiée (car on ne fait pas d'append ni de remove juste on lit l'info et on le prend pour le cacul du côut)

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
            - recette.ingredient est une liste d'Ingredient
            - l'attribut est_frais de chaque ingrédiant est un booléen

        POST:
            - retourne True si un des ingredient contient True à est_frais
            - retourne False si tout les ingredients contient False à est_frais
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