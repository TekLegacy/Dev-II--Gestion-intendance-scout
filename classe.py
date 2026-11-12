#fichier contenant les classes

class Camp:
    def __init__(self, nb_jours : int = 12 , nb_personnes_total : int = 0 , budget_jour_personne : float = 6.5, nb_pers_tranche : list = [0, 0, 0]):
        '''
        Constructeur de la classe Camp.

        PRE:
            - nb_jours est un entier représentant le nombre de jours du camp
            - nb_personnes_total est un entier représentant le nombre total de personnes au camp
            - budget_jour_personne est un float représentant le budget par jour et par personne
            - nb_pers_tranche est une liste de trois entiers représentant le nombre de personnes dans chaque tranche d'âge

        POST:
            - Un objet Camp est créé avec les attributs nb_jours, nb_personnes_total, budget_jour_personne, nb_pers_tranche et budget
        ''' 
        self.nb_jours = nb_jours
        self.nb_personnes_total = nb_personnes_total
        self.budget_jour_personne = budget_jour_personne
        self.nb_pers_tranche = nb_pers_tranche
        self.budget = self.nb_jours * self.nb_personnes_total * self.budget_jour_personne
    
    def calcule_portion(self):

        '''
        Calcule la portion de nourriture nécessaire pour le camp en fonction du nombre de personnes dans chaque tranche d'âge.

        PRE:
            - self.nb_pers_tranche est une liste de trois entiers représentant le nombre de personnes dans chaque tranche d'âge.

        POST:
            - Retourne un float représentant la portion totale de nourriture nécessaire pour le camp.

        '''
        portion = self.nb_pers_tranche[0] * 0.8 + self.nb_pers_tranche[1] * 1 + self.nb_pers_tranche[2] * 1.1
        return portion

    def deduire_cout(self, cout):
        '''
        Déduit le coût d'une recette du budget total du camp.

        PRE:
            - cout est un float représentant le coût d'une recette.
            - le budget doit être aussi plus grand que cout

        POST:
            - Met à jour l'attribut self.budget en soustrayant le coût de la recette.
        '''
        if self.budget >= cout:
            self.budget -= cout
        else:
            print("Budget insuffisant pour déduire ce coût.") 




class Recette:
    def __init__(self, nom_recette : str, nbr_ingredients : int):
        ''' 
        Constructeur de la classe Recette. 

        PRE:
            - nom_recette est un string non vide représentant le nom d'une recette
            - nbr_ingrédients est un integer plus grand que 0 représentant le nombre d'ingrédient différent dans la recette

        Post:
            - Un object Recette est crée avec les 2 attributs valide correspondant aux arguments nom_recette et nbr_ingrédients 
            ainsi qu'une liste "ingrédient" initialisé à vide. 
        '''
        self.nom_recette = nom_recette
        self.nbr_ingredients = nbr_ingredients

        self.ingredient = []

    def ajout_ingredient(self, nom, prix, paquet, est_frais):
        """
        Crée un nouvelle objet ingrédient et l'ajoute à la liste ingrédients

        PRE: 
            - nom est un string non vide
            - prix est un float plus grand que 0
            - paquet est un integer plus grand que 0
            - est_frais est un booléen

        POST:
            - ne retourne rien
            - si la liste Ingrédient fait le taille de nbr_ingredients, 
            rajoute le nouvel ingrédient à la liste et augmente nbr_ingrédients de 1
            - si la taille de la liste ingrédient est plus petite que nbr_ingrédients, 
            rajoute le nouvel ingrédient à la liste
        """
        ing = Ingredient(nom, prix, paquet, est_frais)
        if len(self.ingredient) < self.nbr_ingredients:
            self.ingredient.append(ing)
        else:
            self.ingredient.append(ing)
            self.nbr_ingredients += 1
        

    def supprimer_ingredient(self, ingre):
        """
        Supprime l'ingrédient avec le nom "ingre" de la liste ingrédient

        PRE:
            - ingre est un string non vide
            - la liste ingrédient ne peut pas être vide

        POST:
            - ne retourne rien
            - supprime l'ingrédient de la liste
            - si l'ingrédient n'est pas dans la liste, ne fait rien
        """
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
        ''' 
        Constructeur de la classe Ingredient. 

        PRE:
            - nom est une chaîne de caractères représentant le nom de l'ingrédient 
                Attention: le nom ne peut pas etre une chaine vide
            - prix est un nombre flottant représentant le prix de l'ingrédient 
                Attention: le prix doit etre plus grand ou egal a 0     
            - paquets est un entier représentant le nombre de paquets de l'ingrédient 
                Attention: le nombre de paquets doit etre plus grand ou egal a 1 
            - est_frais est un booléen indiquant si l'ingrédient est frais ou non

        Post:
            - Un object Ingredient est crée avec les quattre attributs valide correspond aux argument nom, prix, paquets et est_frais. 
        '''

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

    def calcul_cout(self,recette):
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

    def __str__(self): # en cours
        return f"Le menu contient {len(self.all_recette)} recettes"
