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