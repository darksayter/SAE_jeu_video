class pomme(object):
    def __init__(self, nom, hp):
        self.nom = nom
        self.hp = hp
        
    def getNom(self):
        return self.nom
    
    def getHp(self):
        return self.nom
    
    def setNom(self,nom):
        self.nom = nom
        
    def setHp(self,hp):
        self.hp = hp
        
    def utiliser(self, cible):
        cible.hp += self.hp
        return cible.hp