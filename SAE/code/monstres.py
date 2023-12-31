class Monstre(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hp = 30
        self.degat = 4
        self.type = ""
        self.image = "IMG/zombie.png"

    def __repr__(self) -> str:
        return f"Monstre({self.x}, {self.y}, {self.hp}, {self.degat})"
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
    def getHp(self):
        return self.hp
    
    def getVieMax(self):
        return 30
    
    def getDegat(self):
        return self.degat
    
    def getType(self):
        return self.type
    
    def getImage(self):
        return self.image
    
    def getHauteurImage(self):
        return 100
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
    
    def setHp(self, hp):
        self.hp = hp
        
    def setDegat(self, degat):
        self.degat = degat
        
    def setType(self, type):
        self.type = type
        
    def setImage(self, image):
        self.image = image
        
    def attaque(self, cible):
        cible.hp -= self.degat
        return cible.hp
        
    
# zombie, squelette, creeper, enderman, ender dragon