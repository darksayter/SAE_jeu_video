import pygame
import random

class Bouton:
    
    def __init__(self, position, taille, couleur):
        self.position = position
        self.taille = taille
        self.couleur = couleur
        self.clic_detecte = False

    def dessiner(self, surface):
        pygame.draw.rect(surface, self.couleur, (*self.position, *self.taille))

    def est_clique(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            position_souris = pygame.mouse.get_pos()
            if (
                self.position[0] <= position_souris[0] <= self.position[0] + self.taille[0]
                and self.position[1] <= position_souris[1] <= self.position[1] + self.taille[1]
                and not self.clic_detecte
            ):
                self.clic_detecte = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clic_detecte = False
        return False
    
    def afficher_texte_dans_bouton(bouton, texte, police, couleur_texte, surface):
        font = pygame.font.Font(None, police)
        texte_surface = font.render(texte, True, couleur_texte)
        texte_rect = texte_surface.get_rect(center=(bouton.position[0] + bouton.taille[0] // 2, bouton.position[1] + bouton.taille[1] // 2))
        surface.blit(texte_surface, texte_rect)

    def reset_clic(self):
        self.clic_detecte = False

    def lancer_de(self):
        resultat_de = random.randint(1, 3)
        return resultat_de