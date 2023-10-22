class zombie:
    def __init__(self,hp,degat):
        self.hp = hp
        self.degat = degat
        
    def attaque(self, cible):
        cible.hp -= self.degat
        return cible.hp
    
    def attaque_special(self, cible):
        cible.hp -= self.degat*1,5
        return cible.hp