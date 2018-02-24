from const import *
from tcod import libtcod
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

def player_movement():
    global player_y, player_x
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player_y = player_y - 1
