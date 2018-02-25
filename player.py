from const import *
import tcod

#Player information

def handle_keys(coord):
    # key = tcod.console_wait_for_keypress(True)
    key = tcod.console_check_for_keypress()
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter for fullscreen toggling
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    # exiting the game
    elif key.vk == tcod.KEY_ESCAPE:
        return True

    if tcod.console_is_key_pressed(tcod.KEY_UP):
        coord['y'] = coord['y'] - 1

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        coord['y'] = coord['y'] + 1

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        coord['x'] = coord['x'] - 1

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        coord['x'] = coord['x'] + 1
