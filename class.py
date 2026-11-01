#fichier contenant les classes
#test

class Recette:
    def __init__(self, nom_recette : str, nbr_ingredients : int):
        self.nom_recette = nom_recette
        self.nbr_ingredients = nbr_ingredients

        self.ingredient = []

    def ajout_ingredient(self):
        for i in range(self.nbr_ingredients):
            nom = input("le nom de l'ingédient ? : ")
            prix = input("son prix ? : ")
            paquet = input("quelle est son prix ? : ")
            est_frais = input("est-il frais ? (True ou False) : ")

            ing = Ingredients(nom, prix, paquet, est_frais)

            self.ingredient.append(ing)

    def supprimer_ingredient(self, ingre):
        temp_l = []
        for i in self.ingredient:
            if i.nom != ingre:
                temp_l.append(i)
        self.ingredient = temp_l
        self.nbr_ingredients = len(temp_l)

        