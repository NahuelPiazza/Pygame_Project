import pygame as pg
import world.configuration as world_config
import media
import constants as const


backgroun_lvl1 = pg.image.load(const.BACKGROUND_LVL1)
backgroun_lvl1 = pg.transform.scale(backgroun_lvl1, (world_config.WORLD_WIDTH, world_config.WORLD_HEIGHT))