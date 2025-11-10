import pygame as pg
import sys

import constants as const
from settings import display, assets
from character import main_character as main_char
import world.configuration as world_config

# inicializa pygame
pg.init() 

#ventana del juego
window = pg.display.set_mode((display.WIDTH, display.HEIGHT))

#icono y titulo de la ventana
pg.display.set_icon(pg.image.load(const.ICON))
pg.display.set_caption("Bushi-Do")

#fuente
font = pg.font.Font("fonts\Oswald\Oswald-VariableFont_wght.ttf", 24)




#bucle principal

def main():
    clock = pg.time.Clock()
    world =  world_config.WORLD_WIDTH, world_config.WORLD_HEIGHT
    screen = pg.display.set_mode(world)
    character = main_char
    run = True
    position_x, position_y = 100, 100
    movement = (0, 0)

    while run:
        for event in pg.event.get(): #entrega la lista de eventos que pueden ocurrir en el juego
            if event.type == pg.QUIT: # si el tipo de evento coincide con el evento de salir
                run = False # entonces salir del bucle

        # direccionamiento del personaje
        dx, dy = 0, 0
        keys = pg.key.get_pressed() #obtiene las teclas que se estan presionando
        if keys[pg.K_LEFT]:
            dx -= 5
        if keys[pg.K_RIGHT]:
            dx += 5
        if keys[pg.K_UP]:
            dy -= 5
        if keys[pg.K_DOWN]:
            dy += 5

        # aplica movimiento
        position_x, position_y = character.move_character(position_x, position_y, dx, dy, bounds=(world_config.WORLD_WIDTH, world_config.WORLD_HEIGHT), size=20)
        movement = (dx, dy)
        print(movement )

        # frames por segundo
        clock.tick(60)

        #crear el mundo 
        world_config.create_world(window)   

        #dibuja el personaje
        character.draw_character(window, ("red"),position_x, position_y,  size= 20)

        #obtener y mostrar la posicion del mouse

        
        # window.blit(text, (450, 300)) #dibuja el texto en la pantalla
        
        pg.display.flip() #actualiza la pantalla
main()
pg.quit()
    