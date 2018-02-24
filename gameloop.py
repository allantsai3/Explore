from const import *
import tcod as libtcod

font_flags = libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD
libtcod.console_set_custom_font(FONT_PATH, font_flags)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FULLSCREEN)

#limiting FPS for non turn based
libtcod.sys_set_fps(LIMIT_FPS)


#Main Loop of the game
while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)

    libtcod.console_flush()

