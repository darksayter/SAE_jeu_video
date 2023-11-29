import random as rd
import pygame

def lancer_de():
    return rd.randint(1, 6)

def affichage_de():
    if lancer_de == 1 :
        img = pygame.image.load("./IMG/de/1.png")
    if lancer_de == 2 :
        img = pygame.image.load("./IMG/de/2.png")
    if lancer_de == 3 :
        img = pygame.image.load("./IMG/de/3.png")
    if lancer_de == 4 :
        img = pygame.image.load("./IMG/de/4.png")
    if lancer_de == 5 :
        img = pygame.image.load("./IMG/de/5.png")
    if lancer_de == 6 :
        img = pygame.image.load("./IMG/de/6.png")
    return img