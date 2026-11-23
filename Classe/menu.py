class Menu:
    def __init__(self) -> None:
        '''
        Constructeur de la classe Menu.
        
        PRE: AUCUN 

        POST: 
            - Creer un objet Menu avec la liste all_recette initilisé a vide.
         
        '''
        self.__all_recette = []

    @property
    def all_recette(self) -> list:
        return self.__all_recette

    def calcul_cout(self,recette) -> float:
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
        if len(recette.ingredient) == 0:
            return cout
        else : 
            for i in recette.ingredient:
                cout += i.prix * i.paquets
            return cout

    def contient_frais(self, recette) -> bool:
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

    def ajout_recette(self, nom_recette, nbr_ingredient) -> str:
        """
        (Antonin)
        Ajout d'une recette au menu. 

        PRE:
            - nom_recette est une chaîne de caractères
            - nbr_ingredient est un entier positif

        POST: 
            - si une recette avec le même nom existe déjà dans le menu, retourne 'erreur'.  (EXCEPTION ValueError)
            - si aucune recette avec ce nom n'existe pas dans le menu, crée une nouvelle recette et la retourne
        """
        for i in self.__all_recette : 
            if i.nom_recette == nom_recette:
                raise ValueError("La recette existe déjà dans le menu.")
        new_recette = Recette(nom_recette, nbr_ingredient)
        self.__all_recette.append(new_recette)
        return 'La recette a bien été ajouté au menu'
 
    def supprime_recette(self, old_recette) -> str:
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
        for i in self.__all_recette:
            if i.nom_recette != old_recette:
                temporaire.append(i)
        if len(temporaire) < len(self.__all_recette):
            self.__all_recette = temporaire
            return "La recette a bien ete supprime de la liste"
        raise ValueError("La recette n'existe pas dans le menu")

    def calcul_quantite(self, recette, nombre_personnes) -> dict: 
        '''
        Calcul la quantite total d'ingredient pour une recette choisie. 
        
        PRE:
            -recette est une objet RECETTE correspond a la recette choisie. 
            -nombre_personne est un entier provenant de la classe CAMP correspond au nombre total de personne presente au camp.  
        POST:
            -retourne un dictionnaire contenant chaque nom d'ingredient present dans la recette et la quantite a acheter pour la recette choisie en fonction du nombre de personnes presentes.
            -si nombre de personne est 0, retourne un message d'erreur disant que personne n'est present au camp.
        '''
        quantites= {}
        for ingredient in recette.ingredient: 
            quantite_totale = ingredient.paquets * nombre_personnes
            quantites[ingredient.nom] = quantite_totale
        return quantites

    def __str__(self) -> str: # en cours
        return f"Le menu contient {len(self.__all_recette)} recettes"
