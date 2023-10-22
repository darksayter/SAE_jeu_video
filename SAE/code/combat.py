import pygame
import sys
from joueur import *
from monstres import *
from bouton import *

def combat():

    en_cours = True

    pygame.init()

    NOIR = (0, 0, 0)

    largeur_fenetre = 1120
    hauteur_fenetre = 800

    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Combat")

    fond_combat = pygame.image.load("IMG/fond_d_ecran.jpg")

    police_titre = pygame.font.Font(None, 60)

    mob1 = Monstre(1, 1)
    print(mob1)
    j1 = Joueur("j1", 1, 1)
    print(j1)

    def afficher_texte(texte, x, y, police, couleur=NOIR):
        texte_surface = police.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect(center=(x, y))
        fenetre.blit(texte_surface, texte_rect)

    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
                pygame.quit()
                sys.exit()

        fenetre.blit(fond_combat, (0, 0))
        fenetre.blit(pygame.image.load(mob1.getImage()), (largeur_fenetre//3, hauteur_fenetre//2))
        fenetre.blit(pygame.image.load(j1.getImage()), (largeur_fenetre//1.70, hauteur_fenetre//2))

        afficher_texte("Combat", largeur_fenetre//2, hauteur_fenetre//10, police_titre)
        
        bouton_attaquer = Bouton((largeur_fenetre//2.5, hauteur_fenetre//1.25), (200, 50), NOIR)
        bouton_attaquer.dessiner(fenetre)
        bouton_attaquer.afficher_texte_dans_bouton("Attaquer")

        pygame.display.flip()
    
    return en_cours

if __name__ == "__main__":
    combat()