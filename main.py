import pygame as pg
import sys

import constants as const
from settings import display, assets
from character import main_character as main_char
from world import configuration as world_config 
from world.menu import menu
from world.lvl1 import generals as lvl1
# inicializa pygame
pg.init() 

#ventana del juego
window = pg.display.set_mode((display.WIDTH, display.HEIGHT))

#icono y titulo de la ventana
pg.display.set_icon(pg.image.load(const.ICON).convert())
pg.display.set_caption("Bushi-Do")

#fuentes
font = pg.font.Font("fonts\Oswald\Oswald-VariableFont_wght.ttf", 24)
title_font = pg.font.Font("fonts\Oswald\Oswald-VariableFont_wght.ttf", 48)
button_font = pg.font.Font("fonts\Oswald\Oswald-VariableFont_wght.ttf", 32)

#botones
start_button = pg.Rect(display.WIDTH//2 + 150, display.HEIGHT//2 +100, 200, 50)
exit_button = pg.Rect(display.WIDTH//2 + 150, display.HEIGHT//2 +200, 200, 50)

text_start_button = button_font.render("Start Game", True, const.BLACK)
text_exit_button = button_font.render("Exit Game", True, const.WHITE)


#pantalla de menu inicio
def draw_menu():
    window.fill(const.BLACK)
    window.blit(menu.background_menu, (0,0))
    title_text = title_font.render("Bushi-Do", True, const.WHITE)
    window.blit(title_text, (display.WIDTH//2 + 50 - title_text.get_width()//2 + 200 , 100))
    pg.draw.rect(window, const.GREEN, start_button, border_radius=10)
    pg.draw.rect(window, (158,16,25), exit_button, border_radius=10)
    window.blit(text_start_button, (start_button.x + (start_button.width - text_start_button.get_width())//2, start_button.y + (start_button.height - text_start_button.get_height())//2))
    window.blit(text_exit_button, (exit_button.x + (exit_button.width - text_exit_button.get_width())//2, exit_button.y + (exit_button.height - text_exit_button.get_height())//2))
    pg.display.update()

#carga de imagenes del personaje
chr_stand = pg.image.load(const.standing_character_image_path).convert_alpha()
chr_stand = pg.transform.scale(chr_stand, (80, 80))
chr_move = pg.image.load(const.moving_character_image_path).convert_alpha()
chr_move = pg.transform.scale(chr_move, (80, 80))



#bucle principal

def main():
    clock = pg.time.Clock()
    world =  world_config.WORLD_WIDTH, world_config.WORLD_HEIGHT
    screen = pg.display.set_mode(world)
    character = main_char
    run = True
    position_x, position_y = 100, 100
    movement = (0, 0)
    mostra_menu = True

    while run:
        #entrega la lista de eventos que pueden ocurrir en el juego
        for event in pg.event.get(): 
            # si el tipo de evento coincide con el evento de salir
            if event.type == pg.QUIT: 
                # entonces salir del bucle
                run = False
        #primero mostramos el menu de inicio  
        if mostra_menu:
            draw_menu()
            #click izquierdo del mouse
            if event.type == pg.MOUSEBUTTONDOWN:
                #click en start se va al else, lvl1
                if start_button.collidepoint(event.pos):
                    mostra_menu = False
                if exit_button.collidepoint(event.pos):
                    pg.quit()
                    sys.exit()
        else:

            # direccionamiento del personaje
            dx, dy = 0, 0
            moving = False
            # obtiene las teclas que se estan presionando
            keys = pg.key.get_pressed() 
            
            if keys[pg.K_LEFT]:
                dx -= 5
                moving = True
            if keys[pg.K_RIGHT]:
                dx += 5
                moving = True
            if keys[pg.K_UP]:
                dy -= 5
                moving = True  
            if keys[pg.K_DOWN]:
                dy += 5
                moving = True
            # aplica movimiento
            position_x, position_y = character.move_character(position_x, position_y, dx, dy, bounds=(world_config.WORLD_WIDTH, world_config.WORLD_HEIGHT), size=20)
            movement = (dx, dy)
            print(movement )

            # frames por segundo
            clock.tick(60)

            #crear el mundo 
            world_config.create_world(screen)   

            #lvl1 background
            screen.blit(lvl1.backgroun_lvl1, (0,0))

            #dibuja el personaje
            if moving:
                screen.blit(chr_move,(position_x, position_y,))

            else:
                screen.blit(chr_stand,(position_x, position_y,))


            

            
            #actualiza la pantalla
        pg.display.flip() 

main()
pg.quit()
    