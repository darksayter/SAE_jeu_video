class Joueur(object):
    def __init__(self, nom, x : int , y : int):
        self.nom = nom
        self.x: int  = x
        self.y: int  = y
        self.hp = 50
        self.degat = 5
        self.armure = 0
        self.inventaire = []
        self.mouvement = False
        self.image = "IMG/steve.png"
        
    def __repr__(self) -> str:
        return f'joueur({self.nom}, {self.x}, {self.y}, {self.hp}, {self.degat}, {self.armure}, {self.inventaire})'
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
    def getNom(self):
        return self.nom
    
    def getHp(self):
        return self.hp
    
    def getDegat(self):
        return self.degat
    
    def getArmure(self):
        return self.armure
    
    def getInventaire(self):
        return self.inventaire
    
    def getMouvement(self):
        return self.mouvement
    
    def getImage(self):
        return self.image
        
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
    
    def setNom(self, nom):
        self.nom = nom
        
    def setHp(self, hp):
        self.hp = hp
        
    def setDegat(self, degat):
        self.degat = degat
        
    def setArmure(self, armure):
        self.armure = armure
    
    def setInventaire(self, inventaire):
        self.inventaire = inventaire
        
    def setMouvement(self, mouvement):
        self.mouvement = mouvement
        
    def setImage(self, image):
        self.image = image
        
    def attaque(self, cible):
        cible.hp -= self.degat
        return cible.hp
    
    def utiliser_une_pomme(self, cible):
        cible.hp += 10
        return cible.hp
        
    def utiliser_un_shield(self, cible):
        cible.armure += 10
        return cible.armure
        
    def utiliser_une_potion_de_force(self):
        self.degat += 10
        return self.degat
        
    def utiliser_une_potion_de_poison(self, cible):
        cible.hp -= 10
        return cible.hp
    