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
fondo = pg.image.load(const.FONDO)
fondo = pg.transform.scale(fondo, (world_config.WORLD_WIDTH, world_config.WORLD_HEIGHT))


#texto
fuente = pg.font.Font("fonts/Oswald/static/Oswald-Bold.ttf", 50) #definimos la fuente y el tamaño
text = font.render("BIENVENIDO A BUSHIDO ", True, (255, 255  , 255)) #le damos color

text_x = 300 #modifcas posicion horizontal del texto
text_y = 50 #modifcas altura del texto
#imagenes
personaje_img = pg.image.load("media/samuraikk.png").convert_alpha()
personaje_img = pg.transform.scale(personaje_img, (80, 80))

personaje_walk = pg.image.load("media/samukaii.png").convert_alpha()
personaje_walk = pg.transform.scale(personaje_walk, (80, 80))


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
        moving = False
        keys = pg.key.get_pressed() #obtiene las teclas que se estan presionando
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
        world_config.create_world(window)   
        
        screen.blit(fondo, (0,0)) #dibuja el fondo en la pantalla, importante ponerlo antes de crear personaje
        #dibuja el personaje
        #character.draw_character(window, ("red"),position_x, position_y,  size= 20)
        if moving:
            screen.blit(personaje_walk,(position_x, position_y,))

        else:
            screen.blit(personaje_img,(position_x, position_y,))
        #try:
        #    rect_personaje = character.dibujar_personaje(window, personaje_img,position_x, position_y,  size= 60)#creamos el personaje
        #except FileNotFoundError:
        #    imagen_sprite = pg.surface((50, 50))
        #    imagen_sprite.fill((255, 0, 0))
         #dibuja el texto en la pantalla
        screen.blit(text, (text_x, text_y)) #dibuja el texto en la pantalla
        #obtener y mostrar la posicion del mouse
     
        
        # window.blit(text, (450, 300)) #dibuja el texto en la pantalla
        
        pg.display.flip() #actualiza la pantalla
        
main()
pg.quit()
