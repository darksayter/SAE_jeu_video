class potion_force(object):
    def __init__(self, nom, degat):
        self.nom = nom
        self.degat = degat
        
    def getNom(self):
        return self.nom
    
    def getDegat(self):
        return self.degat
    
    def setNom(self,nom):
        self.nom = nom
        
    def setDegat(self,degat):
        self.degat = degat
        
    def utiliser(self, cible):
        cible.degat += self.degat
        return cible.degat