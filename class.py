#fichier contenant les classes
class Ingredient : 
    def __init__ (self,nom : str, prix : float, paquets : int, est_frais : bool):
        self.nom = nom
        self.prix = prix
        self.paquets = paquets
        self.est_Frais = est_frais
        