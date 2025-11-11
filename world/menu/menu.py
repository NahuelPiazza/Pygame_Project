import pygame as pg
import world.configuration as world_config
import constants as const

background_menu = pg.image.load(const.background_menu_image_path)
background_menu = pg.transform.scale(background_menu, (world_config.WORLD_WIDTH, world_config.WORLD_HEIGHT))