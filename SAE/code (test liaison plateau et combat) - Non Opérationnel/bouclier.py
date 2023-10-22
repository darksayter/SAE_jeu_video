class shield(object):
    def __init__(self, nom, armure):
        self.nom = nom
        self.armure = armure
        
    def getNom(self):
        return self.nom
    
    def getArmure(self):
        return self.armure
    
    def setNom(self,nom):
        self.nom = nom
        
    def setArmure(self,armure):
        self.armure = armure
        
    def utiliser_un_shield(self, cible):
        cible.armure += 10
        return cible.armure