import pygame
import sys

def menu_princ():
    
    en_cours = True
    
    # Initialisation de Pygame
    pygame.init()

    # Couleurs
    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)

    # Paramètres de la fenêtre
    largeur_fenetre = 1120
    hauteur_fenetre = 800

    # Création de la fenêtre
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Jeu de Plateau")

    # Charger l'image d'arrière-plan de l'écran d'accueil
    fond_accueil = pygame.image.load("IMG/fond_d_ecran.jpg")

    # Charger la police pour le texte
    police = pygame.font.Font(None, 36)

    def afficher_texte(texte, x, y):
        texte_surface = police.render(texte, True, NOIR)
        texte_rect = texte_surface.get_rect(center=(x, y))
        fenetre.blit(texte_surface, texte_rect)

    # Boucle principale du jeu
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Le jeu commence !")
                    en_cours = False

        # Affichage de l'arrière-plan de l'écran d'accueil
        fenetre.blit(fond_accueil, (0, 0))

        # Affichage du texte
        afficher_texte("Bienvenue au Jeu de Plateau", largeur_fenetre // 2, hauteur_fenetre // 2 - 50)
        afficher_texte("Appuyez sur Espace pour commencer", largeur_fenetre // 2, hauteur_fenetre // 2 + 50)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter le taux de rafraîchissement de la boucle
        pygame.time.Clock().tick(30)
        
    return en_cours

if __name__ == '__main__':
    menu_princ()