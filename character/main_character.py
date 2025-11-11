import pygame as pg
import constants as const

def draw_character(screen, color, position_x, position_y, size):
    
    return pg.draw.rect(screen, color, (position_x, position_y, size, size))

def character_transform(surface, size, scale_factor):
    return pg.transform.scale(surface, size, scale_factor)


def move_character(x, y, dx ,dy, bounds=None, size=20):
    x += dx
    y += dy 
    if bounds:
        w, h = bounds
        x = max(0, min(x, w - size))
        y = max(0, min(y, h - size))
    return x, y
    
