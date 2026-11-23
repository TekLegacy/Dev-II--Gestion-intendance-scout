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
        self.__nb_jours = nb_jours
        self.__nb_personnes_total = nb_personnes_total
        self.__budget_jour_personne = budget_jour_personne
        self.__nb_pers_tranche = nb_pers_tranche
        self.__budget = self.__nb_jours * self.__nb_personnes_total * self.__budget_jour_personne


    def calcule_portion(self):

        '''
        Calcule la portion de nourriture nécessaire pour le camp en fonction du nombre de personnes dans chaque tranche d'âge.

        PRE:
            - self.__nb_pers_tranche est une liste de trois entiers représentant le nombre de personnes dans chaque tranche d'âge.

        POST:
            - Retourne un float représentant la portion totale de nourriture nécessaire pour le camp.

        '''
        portion = self.__nb_pers_tranche[0] * 0.8 + self.__nb_pers_tranche[1] * 1 + self.__nb_pers_tranche[2] * 1.1
        return portion
    
    @property
    def budget(self) -> float:
        return self.__budget 

    @property
    def nb_personnes_total(self) -> int:
        return self.__nb_personnes_total
    
    @property
    def nb_jours(self) -> int:
        return self.__nb_jours

    @property
    def budget_jour_personne(self) -> float:
        return self.__budget_jour_personne
    
    @property
    def nb_pers_tranche(self) -> list:
        return self.__nb_pers_tranche
    

    @budget.setter
    def deduire_cout(self, cout) -> None:
        '''
        Déduit le coût d'une recette du budget total du camp.

        PRE:
            - cout est un float représentant le coût d'une recette.
            - le budget doit être aussi plus grand que cout

        POST:
            - Met à jour l'attribut self.__budget en soustrayant le coût de la recette.
            - Le budget ne peut pas devenir négatif. Si le coût est supérieur au budget, une exception est levée.
        '''
        if self.budget >= cout:
            self.budget -= cout
        else:
            raise ValueError("Budget insuffisant pour déduire ce coût.") 
