class Recette:
    def __init__(self, nom_recette : str, nbr_ingredients : int) -> None:
        ''' 
        Constructeur de la classe Recette. 

        PRE:
            - nom_recette est un string non vide représentant le nom d'une recette
            - nbr_ingrédients est un integer plus grand que 0 représentant le nombre d'ingrédient différent dans la recette

        Post:
            - Un object Recette est crée avec les 2 attributs valide correspondant aux arguments nom_recette et nbr_ingrédients 
            ainsi qu'une liste "ingrédient" initialisé à vide. 
        '''
        self.__nom_recette = nom_recette
        self.__nbr_ingredients = nbr_ingredients

        self.__ingredient = []

    @property
    def nom_recette(self) -> str:
        return self.__nom_recette

    @property
    def nbr_ingredients(self) -> int:
        return self.__nbr_ingredients

    @property
    def ingredient(self) -> list:
        return self.__ingredient

    def ajout_ingredient(self, nom, prix, paquet, est_frais) -> str:
        """
        Crée un nouvelle objet ingrédient et l'ajoute à la liste ingrédients

        PRE: 
            - nom est un string non vide
            - prix est un float plus grand que 0
            - paquet est un integer plus grand que 0
            - est_frais est un booléen

        POST:
            - retourne un string validant l'ajout de l'ingrédient ou non
            - si la liste Ingrédient fait le taille de nbr_ingredients, 
            rajoute le nouvel ingrédient à la liste et augmente nbr_ingrédients de 1
            - si la taille de la liste ingrédient est plus petite que nbr_ingrédients, 
            rajoute le nouvel ingrédient à la liste
        """
        for i in self.__ingredient:
            if i.nom == nom:
                return f"L'ingrédient {nom} est déjà dans le recette"
        ing = Ingredient(nom, prix, paquet, est_frais)
        if len(self.__ingredient) < self.__nbr_ingredients:
            self.__ingredient.append(ing)
            return f"L'ingrédient {nom} à bien été ajouté à la recette"
        else:
            self.__ingredient.append(ing)
            self.__nbr_ingredients += 1
            return f"L'ingrédient {nom} à bien été ajouté à la recette"
        

    def supprimer_ingredient(self, ingre) -> str:
        """
        Supprime l'ingrédient avec le nom "ingre" de la liste ingrédient

        PRE:
            - ingre est un string non vide
            - la liste ingrédient ne peut pas être vide

        POST:
            - retourne un string confirmant ou non la suppression de l'ingrédient de la recette
            - supprime l'ingrédient de la liste
            - si l'ingrédient n'est pas dans la liste, ne fait rien
        """
        found = False
        for i in self.__ingredient:
            if i.nom == ingre:
                found = True
        if not found:
            return f"L'ingrédient {ingre} n'est pas dans la recette"

        temp_l = []
        for i in self.__ingredient:
            if i.nom != ingre:
                temp_l.append(i)
        self.__ingredient = temp_l
        self.__nbr_ingredients = len(temp_l)
        return f"L'ingrédient {ingre} à bien été supprimé de la recette"

    def __str__(self) -> str:
        return f"La recette {self.__nom_recette} contient {self.__nbr_ingredients} ingrédients."
