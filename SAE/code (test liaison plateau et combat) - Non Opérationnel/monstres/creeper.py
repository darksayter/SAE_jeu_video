class creeper:
    def __init__(self,hp,degat):
        self.hp = hp
        self.degat = degat
        
    def attaque(self, cible):
        cible.hp -= self.degat
        return cible.hp
    
    def attaque_special(self, cible):
        cible.hp -= self.hp
        self.hp = 0
        return cible.hp, self.hp