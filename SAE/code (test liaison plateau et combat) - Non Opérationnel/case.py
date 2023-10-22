from __future__ import annotations

class Case:
    
    allCases : list [Case] = []
    
    @staticmethod
    def getAllCases() ->list[Case]:
        return Case.allCases
    
    def __init__(self, id, x, y):
        self.id:int = id
        self.x:int = x
        self.y:int = y
        self.type:str = ""
        self.joueur:str = ""
        self.couleur = (0,0,0)
        Case.allCases.append(self)
        
    def setSpecificCase(self : Case,id : int):
        for case in Case.allCases:
            if case.getId() == id:
                case.setType(self.getType())

    def getXSpecificCase(self : Case,id : int):
        for case in Case.allCases:
            if case.getId() == id:
                return case.getX()
        return None
    
    def getYSpecificCase(self : Case,id : int):
        for case in Case.allCases:
            if case.getId() == id:
                return case.getY()
        return None
        
    def __repr__(self) -> str:
        return f'Case({self.id}, {self.x}, {self.y})'
        
    def getId(self):
        return self.id
        
    def getX(self):
        return int(self.x)
    
    def getY(self):
        return int(self.y)
    
    def getType(self):
        return self.type
    
    def getCouleur(self):
        return self.couleur
    
    def setId(self, id):
        self.id = id
        
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
    def setType(self, type):
        self.type = type
        
    def setCouleur(self, couleur):
        self.couleur = couleur