import pygame
import sys
from joueur import *
from bouton import *

def menu_pers():
    
    en_cours = True
    
    # Initialisation de Pygame
    pygame.init()

    # Couleurs
    NOIR = (0, 0, 0)
    GRIS = (200, 200, 200)

    # Paramètres de la fenêtre
    largeur_fenetre = 1120
    hauteur_fenetre = 800

    # Création de la fenêtre
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Sélection du Personnage")

    # Charger l'image d'arrière-plan de l'écran d'accueil
    fond_accueil = pygame.image.load("IMG/fond_d_ecran.jpg")


    # Charger la police pour le texte
    police_titre = pygame.font.Font(None, 60)
    police_normal = pygame.font.Font(None, 36)

    # Liste des noms de personnages
    index_personnage = 0
    nb_pers = [1, 2, 3, 4]  # Add this line to initialize nb_pers
    noms_personnages = [f"Personnage {nb_up}" for nb_up in nb_pers]
    
    # Liste des boutons
    bouton_suivant = Bouton((largeur_fenetre//35,hauteur_fenetre//30),(largeur_fenetre//7,hauteur_fenetre//8),GRIS)

    # Champs de saisie de texte pour le nom du personnage
    input_rect = pygame.Rect(largeur_fenetre // 2 - 150, hauteur_fenetre // 2 - 25, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = False
    text_surface = police_normal.render(text, True, color)

    def afficher_texte(texte, x, y, police, couleur=NOIR):
        texte_surface = police.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect(center=(x, y))
        fenetre.blit(texte_surface, texte_rect)
        
    

    # Boucle principale de la sélection du personnage
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    index_personnage = (index_personnage - 1) % len(noms_personnages)
                elif event.key == pygame.K_RIGHT:
                    index_personnage = (index_personnage + 1) % len(noms_personnages)
                elif event.key == pygame.K_UP:
                    nb_pers.append(nb_pers[-1]+1)
                    print(nb_pers)
                elif event.key == pygame.K_DOWN:
                    if len(nb_pers) > 1:
                        nb_pers.pop()
                    print(nb_pers)
                elif active:
                    if event.key == pygame.K_RETURN:
                        print(f"Nom du personnage {index_personnage + 1}: {text}")
                        if nb_pers[index_personnage] == 1:
                            j1 = Joueur(text, 1, 1)
                            text = ''
                            print(j1)
                        if nb_pers[index_personnage] == 2:
                            j2 = Joueur(text, 1, 1)
                            text = ''
                            print(j2)
                        if nb_pers[index_personnage] == 3:
                            j3 = Joueur(text, 1, 1)
                            text = ''
                            print(j3)
                        if nb_pers[index_personnage] == 4:
                            j4 = Joueur(text, 1, 1)
                            text = ''
                            print(j4)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        text_surface = police_normal.render(text, True, color)
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                    
            if bouton_suivant.est_clique(event):
                en_cours = False
                bouton_suivant.reset_clic()


        # Update the noms_personnages list based on nb_pers
        noms_personnages = [f"Personnage {nb}" for nb in nb_pers]

        # Affichage de l'arrière-plan de l'écran d'accueil
        fenetre.blit(fond_accueil, (0, 0))

        # Affichage du nom du personnage sélectionné
        # if index_personnage+1 == nb_pers[index_personnage]:
        #     afficher_texte(noms_personnages[index_personnage-1], largeur_fenetre // 2, hauteur_fenetre // 2 - 50, police_normal)
        # else:
        afficher_texte(noms_personnages[index_personnage], largeur_fenetre // 2, hauteur_fenetre // 2 - 50, police_normal)
        # print(index_personnage+1)
        # print("test")
        # print(nb_pers[index_personnage])

        # Affichage du champ de saisie de texte pour le nom du personnage
        afficher_texte(f"Nom du personnage: {text}", largeur_fenetre // 2, hauteur_fenetre // 2 + 50, police_normal)
        afficher_texte(f"Nombre de joueur actuel : {nb_pers[-1]}", largeur_fenetre // 2, hauteur_fenetre // 2 + 100, police_normal)
        afficher_texte("Aide : pour changer de joueur, il suffit d'appuyer sur vos flèches latérales", largeur_fenetre // 2, hauteur_fenetre // 2 + 150, police_normal)
        afficher_texte("Pour augmenter ou baisser le nombre de joueur,", largeur_fenetre // 2, hauteur_fenetre // 2 + 200, police_normal)
        afficher_texte("il suffit d'appuyer sur vos flèches Haut et Bas", largeur_fenetre // 2, hauteur_fenetre // 2 + 250, police_normal)
        width = max(200, text_surface.get_width())
        input_rect.w = width + 100
        fenetre.blit(text_surface, (input_rect.x + 65, input_rect.y + 13))
        pygame.draw.rect(fenetre, color, input_rect, 2)
        bouton_suivant.dessiner(fenetre)
        bouton_suivant.afficher_texte_dans_bouton("Suivant", 40, NOIR, fenetre)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter le taux de rafraîchissement de la boucle
        pygame.time.Clock().tick(30)
            
    return en_cours

if __name__ == '__main__':
    menu_pers()