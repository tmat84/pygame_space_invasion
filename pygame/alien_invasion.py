import sys

import pygame

from settings import Settings

def run_game():
    #Inicjalizacja gry i utworzenie obiketu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Inwazja obcych")

    #Rozpoczęcie pętli głównej gry.
    while True:

        #Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Odświeżanie ekranu w trakcie każdej iteracji pętli
        screen.fill(ai_settings.bg_color)

        # Wyświtlenie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()

run_game()
