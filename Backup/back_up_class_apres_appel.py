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
        '''
        Constructeur de la classe Menu.

        PRE: AUCUN

        POST:
            - Creer un objet Menu avec la liste all_recette initilisé a vide.

        '''
        self.all_recette = []

    def calcul_cout(self, recette):
        """
        Calcule le coût total des ingrédients d'une recette

        Input: recette est un objet Recette
        Output: cout est un nombre (float)

        PRE:
            - recette.ingredient est une liste d'Ingrédient
            - le prix de chaque ingrédient est un nombre positif

        POST:
            - retourne la somme des prix de tous les ingrédients
            - retourne 0 si la recette n'a pas d'ingrédient
            - la liste ingredient n'est pas modifiée

        """
        cout = 0
        for i in recette.ingredient:
            cout += i.prix
        return cout

    def contient_frais(self, recette):
        """
        Indique si la recette contient au minimum un ingrédient frais

        Input: recette est un objet Recette
        Output: Booléen

        PRE:
            - recette.ingredient est une liste d'Ingrédient
            - l'attribut est_frais de chaque ingrédient est un booléen

        POST:
            - retourne True si un des ingrédients est frais
            - retourne False si aucun ingredient n'est frais
            - retourne False si la recette n'a aucun ingrédient
            - la recette n'est pas modifiée

        """
        for i in recette.ingredient:
            if i.est_frais == True:
                return True

        return False

    def ajout_recette(self, new_recette):
        """
        Ajout d'une recette au menu.

        PRE:
            -new_recettte est un objet Recette qui correspond a la recette que l'on veut ajouter.

        POST:
            -si new_recette existe deja aux menu on retourne 'erreur'.  (EXCEPTION ValueError)
            -si new_recette n'existe pas au menu on l'ajoute et on retourne 'La recette a bien été ajouté au menu'
        """
        self.all_recette.append(new_recette)
        return 'La recette a bien été ajouté au menu'

    def supprime_recette(self, old_recette):
        """
        Suppression d'une recette du menu

        Input: old_recette est un objet Recette
        Output: Un message de confirmation est affiche si la suppression a réussi

        PRE:
            - self.all_recette est une liste de recettes

        POST:
            - retourne un message de confirmation "old recette a bien été supprimé de la liste" si la suppression a réussi

            - si old_recette ne se trouve pas dans self.all_recette alors la méthode retourne ValuError "La recette n'existe pas dans le menu"

        """

        temporaire = []
        for i in self.all_recette:
            if i != old_recette:
                temporaire.append(i)
        if len(temporaire) < len(self.all_recette):
            self.all_recette = temporaire
            return "La recette a bien ete supprime de la liste"
        return 'erreur'

    def __str__(self):  # en cours
        return f"Le menu contient {len(self.all_recette)} recettes"