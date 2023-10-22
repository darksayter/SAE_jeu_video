import pygame
import sys
from etat_combat import CombatState  # Assurez-vous d'utiliser le bon chemin vers CombatState
from joueur import Joueur
from monstres import Monstre
from bouton import Bouton

def Combat(combat_state):
    en_cours = True
    bouton_attaque_clique = False

    pygame.init()

    NOIR = (0, 0, 0)
    BLANC = (255, 255, 255)

    largeur_fenetre = 1120
    hauteur_fenetre = 800

    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Combat")

    fond_combat = pygame.image.load("IMG/fond_d_ecran.jpg")

    police_titre = pygame.font.Font(None, 60)

    mob1 = Monstre(1, 1)
    j1 = Joueur("j1", 1, 1)

    def dessiner_barre_de_vie(surface, x, y, largeur, hauteur, vie_actuelle, vie_max):
        bordure_rect = pygame.Rect(x, y, largeur, hauteur)
        pygame.draw.rect(surface, NOIR, bordure_rect, 2)

        largeur_vie = (vie_actuelle / vie_max) * (largeur - 4)

        barre_vie_rect = pygame.Rect(x + 2, y + 2, largeur_vie, hauteur - 4)
        pygame.draw.rect(surface, (0, 255, 0), barre_vie_rect)

        police = pygame.font.Font(None, 36)
        texte_vie = f"{vie_actuelle}/{vie_max}"
        texte_surface = police.render(texte_vie, True, NOIR)
        texte_rect = texte_surface.get_rect(center=(x + largeur / 2, y - 20))
        surface.blit(texte_surface, texte_rect)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_attaquer.est_clique(event):
                    bouton_attaque_clique = True

        fenetre.blit(fond_combat, (0, 0))
        fenetre.blit(pygame.image.load(mob1.getImage()), (largeur_fenetre//3, hauteur_fenetre//2))
        fenetre.blit(pygame.image.load(j1.getImage()), (largeur_fenetre//1.70, hauteur_fenetre//2))

        afficher_texte("Combat", largeur_fenetre//2, hauteur_fenetre//10, police_titre)

        dessiner_barre_de_vie(fenetre, largeur_fenetre // 1.70, hauteur_fenetre // 2 + j1.getHauteurImage() + 10, 200, 20, j1.getHp(), j1.getVieMax())
        dessiner_barre_de_vie(fenetre, largeur_fenetre // 3, hauteur_fenetre // 2 + mob1.getHauteurImage() + 10, 200, 20, mob1.getHp(), mob1.getVieMax())

        bouton_attaquer = Bouton((largeur_fenetre//2.5, hauteur_fenetre//1.25), (200, 50), NOIR)
        bouton_attaquer.dessiner(fenetre)
        bouton_attaquer.afficher_texte_dans_bouton("Attaquer", 40, BLANC, fenetre)

        if bouton_attaque_clique:
            j1.attaque(mob1)
            mob1.attaque(j1)
            if j1.getHp() == 0 or mob1.getHp() == 0:
                en_cours = False
                pygame.quit()
                sys.exit()
            bouton_attaque_clique = False

        pygame.display.flip()

    return en_cours

if __name__ == "__main__":
    combat_state = CombatState()
    Combat(combat_state)
