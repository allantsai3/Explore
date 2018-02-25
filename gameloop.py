from const import *
from player import *
import tcod

font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(FONT_PATH, font_flags)

tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, INITIAL_GAME_FULLSCREEN_STATE)

#limiting FPS for non turn based
tcod.sys_set_fps(LIMIT_FPS)

#Player information
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_coord = {'x': player_x, 'y': player_y}

#Main Loop of the game
while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0, player_coord['x'], player_coord['y'], 'x', tcod.BKGND_NONE)

    tcod.console_flush()
    tcod.console_put_char(0, player_coord['x'], player_coord['y'], ' ', tcod.BKGND_NONE) #erases the last position

    #key handling
    exit = handle_keys(player_coord)
    if exit:
        break
