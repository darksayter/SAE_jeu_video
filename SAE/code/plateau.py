import random
import pygame
import sys
from de import *
from case import Case
from bouton import Bouton
from joueur import Joueur
from monstres import Monstre


def plateau():
    
    # Initialisation de Pygame
    pygame.init()

    # Définition des couleurs
    NOIR = (0, 0, 0)
    ORANGE = (255, 165, 0)
    GRIS = (200, 200, 200)

    # Taille de la fenêtre et des cases
    taille_case = 80
    largueur = 14
    hauteur = 10
    largueur_fenetre = taille_case * largueur
    hauteur_fenetre = taille_case * hauteur


    # Création de la fenêtre
    fenetre = pygame.display.set_mode((largueur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Plateau de jeu")

    # Charger l'image d'arrière-plan de l'écran d'accueil
    fond_accueil = pygame.image.load("IMG/fond_d_ecran.jpg")

    # Initialisation de toutes les cases du plateau
    case1 : Case = Case(1, 5, 8)
    case2 : Case = Case(2, 4, 8)
    case3 : Case = Case(3, 3, 8)
    case4 : Case = Case(4, 3, 7)
    case5 : Case = Case(5, 2, 7)
    case6 : Case = Case(6, 1, 7)
    case7 : Case = Case(7, 1, 6)
    case8 : Case = Case(8, 1, 5)
    case9 : Case = Case(9, 2, 5)
    case10 : Case = Case(10, 2, 4)
    case11 : Case = Case(11, 2, 3)
    case12 : Case = Case(12, 1, 3)
    case13 : Case = Case(13, 1, 2)
    case14 : Case = Case(14, 1, 1)
    case15 : Case = Case(15, 2, 1)
    case16 : Case = Case(16, 3, 1)
    case17 : Case = Case(17, 3, 2)
    case18 : Case = Case(18, 4, 2)
    case19 : Case = Case(19, 5, 2)
    case20 : Case = Case(20, 5, 1)
    case21 : Case = Case(21, 6, 1)
    case22 : Case = Case(22, 7, 1)
    case23 : Case = Case(23, 8, 1)
    case24 : Case = Case(24, 8, 2)
    case25 : Case = Case(25, 8, 3)
    case26 : Case = Case(26, 8, 4)
    case27 : Case = Case(27, 8, 5)
    case28 : Case = Case(28, 7, 5)
    case29 : Case = Case(29, 7, 6)
    case30 : Case = Case(30, 7, 7)
    case31 : Case = Case(31, 6, 7)
    case32 : Case = Case(32, 6, 8)

    # Initialisation du plateau
    plateau =   [[None,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   , None],
                [None,  case14  ,  case13  ,  case12  ,   None   ,  case8   ,  case7   ,  case6   ,   None   ,   None   ,    4     ,    5     ,   None   , None],
                [None,  case15  ,   None   ,  case11  ,  case10  ,  case9   ,   None   ,  case5   ,   None   ,   None   ,   None   ,   None   ,   None   , None],
                [None,  case16  ,  case17  ,   None   ,   None   ,   None   ,   None   ,  case4   ,  case3   ,   None   ,   None   ,   None   ,   None   , None],
                [None,   None   ,  case18  ,   None   ,   None   ,   None   ,   None   ,   None   ,  case2   ,   None   ,   None   ,   None   ,   None   , None],
                [None,  case20  ,  case19  ,   None   ,   None   ,   None   ,   None   ,   None   ,  case1   ,    3     ,   None   ,   None   ,   None   , None],
                [None,  case21  ,   None   ,   None   ,   None   ,   None   ,   None   ,  case31  ,  case32  ,   None   ,   None   ,   None   ,   None   , None],
                [None,  case22  ,   None   ,   None   ,   None   ,  case28  ,  case29  ,  case30  ,   None   ,   None   ,   None   ,   None   ,   None   , None],
                [None,  case23  ,  case24  ,  case25  ,  case26  ,  case27  ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   , None],
                [None,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   ,   None   , None]]

    # Initialisation de la liste des boutons
    liste_boutons = []
    
    # Initialisation de la listes de monstres
    mobs = []

    # Initialisation des perso pour tests
    j1 : Joueur = Joueur("joueur_1", case1.getX(), case1.getY())
    j2 : Joueur = Joueur("joueur_2", case1.getX(), case1.getY())
    
    # Initialisation des mobs pour tests
    mob1 : Monstre = Monstre(case2.getX(),case2.getY())
    mob2 : Monstre = Monstre(case3.getX(),case3.getY())
    mob3 : Monstre = Monstre(case4.getX(),case4.getY())
    
    # def genereMobs(plateau, mobs, nombre_de_mobs):
    #     # Réinitialise la liste des monstres
    #     mobs.clear()

    #     # Créez une liste de cases disponibles pour générer des monstres (à l'exception de la case1)
    #     cases_disponibles = []
    #     for i in range(largueur):
    #         for j in range(hauteur):
    #             if plateau[j][i] is not None and plateau[j][i] != case1:
    #                 cases_disponibles.append(plateau[j][i])

    #     # Générer le nombre de monstres souhaité
    #     for _ in range(nombre_de_mobs):
    #         # Vérifiez si des cases sont disponibles
    #         if cases_disponibles:
    #             # Choisissez une case aléatoire parmi les cases disponibles
    #             case_aleatoire = random.choice(cases_disponibles)

    #             # Créez un monstre et placez-le sur la case aléatoire
    #             monstre = Monstre(case_aleatoire, case_aleatoire)

    #             # Ajoutez le monstre à la liste des monstres
    #             mobs.append(monstre)

    #     return mobs
            

    case1.setType("Joueur")

    def getCase(x,y) -> Case:
        return plateau[x][y]

    def getJoueur(x,y) -> Joueur:
        case_temp = getCase(x,y)
        if case_temp.getX() == j1.getX():
            if case_temp.getY() == j1.getY():
                return j1
        if case_temp.getX() == j2.getX():
            if case_temp.getY() == j2.getY():
                return j2
        

    def creationPlateau(plateau):
        for i in range(largueur):
            for j in range(hauteur):
                if plateau[j][i] is not None:
                    if isinstance(plateau[j][i],Case):
                        case_temp = getCase(j,i)
                        if case_temp == case1:
                            pygame.draw.rect(fenetre, ORANGE, (i * taille_case, j * taille_case, taille_case, taille_case))
                            if case_temp.getType() == "Joueur":
                                fenetre.blit(pygame.image.load(j1.getImage()), (i * taille_case, j * taille_case))
                                fenetre.blit(pygame.image.load(j2.getImage()), (i * taille_case, j * taille_case))
                        elif case_temp.getType() == "Joueur":
                            temp_joueur = getJoueur(j,i)
                            pygame.draw.rect(fenetre, NOIR, (i * taille_case, j * taille_case, taille_case, taille_case))
                            fenetre.blit(pygame.image.load(temp_joueur.getImage()), (i * taille_case, j * taille_case))
                        else:
                            pygame.draw.rect(fenetre, NOIR, (i * taille_case, j * taille_case, taille_case, taille_case))
                    if plateau[j][i] == 3:
                        fenetre.blit(pygame.image.load("IMG/fleche_sens.png"), (i * taille_case, j * taille_case))
                    if plateau[j][i] == 4:
                        boutonDe = Bouton((i * taille_case, j * taille_case), (taille_case, taille_case), (255, 0, 0))
                        liste_boutons.append(boutonDe)
                    if plateau[j][i] == 5:
                        fenetre.blit(pygame.image.load("IMG/de/de_vide.png"), (i * taille_case, j * taille_case))
                        if boutonDe.est_clique(event):
                            if resultat_de == 1:
                                fenetre.blit(pygame.image.load("IMG/de/de_1.png"), (i * taille_case, j * taille_case))
                            if resultat_de == 2:
                                fenetre.blit(pygame.image.load("IMG/de/de_2.png"), (i * taille_case, j * taille_case))
                            if resultat_de == 3:
                                fenetre.blit(pygame.image.load("IMG/de/de_3.png"), (i * taille_case, j * taille_case))                            


    def deplacement(case : Case,joueur: Joueur):
        if resultat_de == 1 :
            if case.getId()+1 > 32:
                temp = case.getId()+1
                temp = temp - 32
                joueur.setX(case.getXSpecificCase(temp))
                joueur.setY(case.getYSpecificCase(temp))
                case.setSpecificCase(temp)
                case.setType("")
            else:
                joueur.setX(case.getXSpecificCase(case.getId()+1))
                joueur.setY(case.getYSpecificCase(case.getId()+1))
                case.setSpecificCase(case.getId()+1)
                case.setType("")
                

        elif resultat_de == 2 :
            if case.getId()+2 > 32:
                temp = case.getId()+2
                temp = temp - 32
                joueur.setX(case.getXSpecificCase(temp))
                joueur.setY(case.getYSpecificCase(temp))
                case.setSpecificCase(temp)
                case.setType("")
            else:
                joueur.setX(case.getXSpecificCase(case.getId()+2))
                joueur.setY(case.getYSpecificCase(case.getId()+2))
                case.setSpecificCase(case.getId()+2)
                case.setType("")
            
        elif resultat_de == 3 :
            if case.getId()+3 > 32:
                temp = case.getId()+3
                temp = temp - 32
                joueur.setX(case.getXSpecificCase(temp))
                joueur.setY(case.getYSpecificCase(temp))
                case.setSpecificCase(temp)
                case.setType("")
            else:
                joueur.setX(case.getXSpecificCase(case.getId()+3))
                joueur.setY(case.getYSpecificCase(case.getId()+3))
                case.setSpecificCase(case.getId()+3)
                case.setType("")

    # Boucle pour afficher la fenêtre
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        for bouton in liste_boutons:
            bouton.dessiner(fenetre)

            if bouton.est_clique(event):
                if j1.getMouvement() == False:
                    resultat_de = bouton.lancer_de()
                    print("resultat_de :", resultat_de)
                    deplacement(getCase(j1.getX(), j1.getY()), j1)
                    creationPlateau(plateau)
                    j1.setMouvement(True)
                    print("test1")
                    bouton.reset_clic()
                elif j2.getMouvement() == False:
                    resultat_de = bouton.lancer_de()
                    print("resultat_de :", resultat_de)
                    deplacement(getCase(j2.getX(), j2.getY()), j2)
                    creationPlateau(plateau)
                    j2.setMouvement(True)
                    print("test2")
                    bouton.reset_clic()
            j1.setMouvement(False)
            j2.setMouvement(False)
            bouton.reset_clic()
            
            pygame.display.flip()
            
        # if not mobs:
            # Si la liste des monstres est vide, générez 5 monstres
            # mobs = genereMobs(plateau, mobs, 5)
        
        # Initialisation du fond de la fenetre en gris clair
        fenetre.fill(GRIS)
        
        # Affichage de l'arrière-plan de l'écran d'accueil
        fenetre.blit(fond_accueil, (0, 0))

        # Affichage du plateau
        creationPlateau(plateau)
        
        # for monstre in mobs:
        #     x = monstre.getX()
        #     y = monstre.getY()
        #     image = monstre.getImage()
        #     fenetre.blit(pygame.image.load(image), (x * taille_case, y * taille_case))





            
        pygame.time.delay(20)
            
        # def clicBouton(plateau):
        #     while True:
        #         for event in pygame.event.get():
        #             if event.type == pygame.QUIT:
        #                 pygame.quit()
        #                 sys.exit()
        #             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #                 position_souris = pygame.mouse.get_pos()
        #                 for bouton in liste_boutons:
        #                     if bouton.est_clique(position_souris):
        #                         print(f"Clic gauche sur le bouton à la position {position_souris}")
        
        # Appeler la fonction pour détecter les clics des boutons
        # clicBouton(plateau)
        
if __name__ == '__main__':
    plateau()