import pygame as pg
from settings import display




screen = pg.display.set_mode((display.WIDTH, display.HEIGHT))
pg.display.set_caption("My Pygame Window")

run = True
while run:
    for event in pg.event.get(): #entrega la lista de eventos que pueden ocurrir en el juego
        if event.type == pg.QUIT: # si el tipo de evento coincide con el evento de salir
            run = False # entonces salir del bucle


pg.quit()
    