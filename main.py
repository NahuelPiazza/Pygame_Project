import pygame as pg

from settings import display, media, assets


pg.init()
pg.display.set_icon(pg.image.load(media.ICON))
window = pg.display.set_mode((display.WIDTH, display.HEIGHT))
pg.display.set_caption("Bushi-Do")
font = pg.font.Font("fonts\Oswald\Oswald-VariableFont_wght.ttf", 24)

run = True

while run:
    for event in pg.event.get(): #entrega la lista de eventos que pueden ocurrir en el juego
        if event.type == pg.QUIT: # si el tipo de evento coincide con el evento de salir
            run = False # entonces salir del bucle
    window.fill("white") #rellena la pantalla de color rojo
    mouse_x, mouse_y = pg.mouse.get_pos() #obtiene la posicion del mouse
    text = font.render(f"posicion en x: {mouse_x} posicion en y: {mouse_y} ", True, ("black")) #renderiza el texto
    window.blit(text, (450, 300)) #dibuja el texto en la pantalla
    
    pg.display.flip() #actualiza la pantalla

pg.quit()
    