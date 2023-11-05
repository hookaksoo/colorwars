import sys
import pygame

# Alusta Pygame
pygame.init()

# Määritä ikkunan leveys ja korkeus
ikkunan_leveys = 400
ikkunan_korkeus = 400

# Luo peli-ikkuna
ikkuna = pygame.display.set_mode((ikkunan_leveys, ikkunan_korkeus))

# Määritä värit niiden nimillä
vari_punainen = (255, 0, 0)
vari_sininen = (0, 0, 255)
vari_keltainen = (255, 255, 0)
vari_vihrea = (0, 255, 0)

# Piirrä värisuorakulmiot ikkunaan
pygame.draw.rect(ikkuna, vari_punainen, (50, 50, 100, 100))
pygame.draw.rect(ikkuna, vari_sininen, (200, 50, 100, 100))
pygame.draw.rect(ikkuna, vari_keltainen, (50, 200, 100, 100))
pygame.draw.rect(ikkuna, vari_vihrea, (200, 200, 100, 100))

# Päivitä ikkuna
pygame.display.update()

# Pelisilmukka
kaynnissa = True
while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

# Sulje Pygame
pygame.quit()
