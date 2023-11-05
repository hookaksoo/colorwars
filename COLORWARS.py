import sys
import pygame
import random

# Alusta Pygame
pygame.init()

# Määritä ikkunan leveys ja korkeus
ikkunan_leveys = 400
ikkunan_korkeus = 400

# Luo peli-ikkuna
ikkuna = pygame.display.set_mode((ikkunan_leveys, ikkunan_korkeus))

# Määritä ruudun koko ja ruudukon koko
ruudun_koko = 15
ruudukon_leveys = 18
ruudukon_korkeus = 18

# Määritä värit
varit = {
    1: (255, 0, 0),      # Punainen
    2: (0, 0, 255),      # Sininen
    3: (0, 255, 255),    # Sinivihreä (Cyan)
    4: (139, 69, 19),    # Ruskea
    5: (255, 255, 0),    # Keltainen
    6: (255, 182, 193),  # Vaaleanpunainen
    7: (255, 255, 255),  # Valkoinen
    8: (255, 165, 0)     # Oranssi
}

# Luo pelialue ja alusta värivalinnat
pelialue = []

for rivi in range(ruudukon_korkeus):
    for sarake in range(ruudukon_leveys):
        x = sarake * ruudun_koko
        y = rivi * ruudun_koko
        vari_numero = random.randint(1, 8)
        vari = varit[vari_numero]
        pygame.draw.rect(ikkuna, vari, (x, y, ruudun_koko, ruudun_koko))
        pelialue.append((x, y, vari_numero))

# Lisää pelaajat ja heidän väripalettinsa ohjaimiksi
pelaaja1_vari = random.randint(1, 8)
pelaaja2_vari = random.randint(1, 8)
pelaaja1_ohjain_x = 0
pelaaja2_ohjain_x = ikkunan_leveys - ruudun_koko * 8

# Piirrä pelaajien ohjaimet
for vari_numero in range(1, 9):
    vari = varit[vari_numero]
    pygame.draw.rect(ikkuna, vari, (pelaaja1_ohjain_x, ikkunan_korkeus - ruudun_koko, ruudun_koko, ruudun_koko))
    pygame.draw.rect(ikkuna, vari, (pelaaja2_ohjain_x, ikkunan_korkeus - ruudun_koko, ruudun_koko, ruudun_koko))
    pelaaja1_ohjain_x += ruudun_koko
    pelaaja2_ohjain_x += ruudun_koko

# Päivitä ikkuna
pygame.display.update()

# Pelisilmukka
kaynnissa = True
while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

    pygame.display.update()

# Sulje Pygame
pygame.quit()

