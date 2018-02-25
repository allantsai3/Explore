from const import *
from player import *
import tcod

font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(FONT_PATH, font_flags)

tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, INITIAL_GAME_FULLSCREEN_STATE)

#limiting FPS for non turn based
tcod.sys_set_fps(LIMIT_FPS)


#Main Loop of the game
while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0, player_x, player_y, 'x', tcod.BKGND_NONE)

    tcod.console_flush()
    tcod.console_put_char(0, player_x, player_y, ' ', tcod.BKGND_NONE) #erases the last position

    #key handling
    exit = handle_keys()
    if exit:
        break
