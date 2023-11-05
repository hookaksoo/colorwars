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

# Pelaajien vuorot
vuorot = [1, 2]
vuoron_indeksi = 0
tekstin_fontti = pygame.font.Font(None, 36)
tekstin_vari = (0, 0, 0)

# Alareunan palkin asetukset
palkki_vari = (192, 192, 192)
palkki_korkeus = 50
palkki_y = ikkunan_korkeus - palkki_korkeus
viesti = "Klikkaa hiirellä vaihtaaksesi väriä."

# Päivitä ikkuna
pygame.display.update()

# Pelisilmukka
kaynnissa = True
while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False
        elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x, y = tapahtuma.pos
            valittu_vari = None
            valitun_varin_numero = None

            # Tarkista pelaajien ohjaimet ja muuta pelaajan väriä
            if 0 <= y <= ikkunan_korkeus - ruudun_koko:
                for vari_numero in varit:
                    if pelaaja1_ohjain_x <= x <= pelaaja1_ohjain_x + ruudun_koko:
                        valittu_vari = varit[vari_numero]
                        valitun_varin_numero = vari_numero
                        break
                    elif pelaaja2_ohjain_x <= x <= pelaaja2_ohjain_x + ruudun_koko:
                        valittu_vari = varit[vari_numero]
                        valitun_varin_numero = vari_numero
                        break

            if valittu_vari:
                pygame.draw.rect(ikkuna, valittu_vari, (x, y, ruudun_koko, ruudun_koko))
                pygame.display.update()
                pelialue.append((x, y, valitun_varin_numero))

                # Tarkista viereiset ruudut ja mahdolliset alueet
                viereiset_ruudut = [(x - ruudun_koko, y), (x + ruudun_koko, y), (x, y - ruudun_koko), (x, y + ruudun_koko)]
                for viereinen_x, viereinen_y in viereiset_ruudut:
                    if (0 <= viereinen_x < ikkunan_leveys) and (0 <= viereinen_y < ikkunan_korkeus - ruudun_koko):
                        viereinen_vari_numero = None
                        for ruutu_x, ruutu_y, vari_numero in pelialue:
                            if ruutu_x == viereinen_x and ruutu_y == viereinen_y:
                                viereinen_vari_numero = vari_numero
                                break
                        if viereinen_vari_numero == valitun_varin_numero:
                            pygame.draw.rect(ikkuna, valittu_vari, (viereinen_x, viereinen_y, ruudun_koko, ruudun_koko))
                            pygame.display.update()
                            pelialue.append((viereinen_x, viereinen_y, valitun_varin_numero))

                vuoron_indeksi = (vuoron_indeksi + 1) % len(vuorot)

    # Piirrä alareunan palkki ja viesti
    pygame.draw.rect(ikkuna, palkki_vari, (0, palkki_y, ikkunan_leveys, palkki_korkeus))
    teksti_pinta = tekstin_fontti.render(viesti, True, tekstin_vari)
    ikkuna.blit(teksti_pinta, (10, palkki_y + palkki_korkeus // 2 - 18))
    
    pygame.display.update()

# Sulje Pygame
pygame.quit()
