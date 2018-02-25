from const import *
import tcod

#Player information
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

def handle_keys():
    # key = tcod.console_wait_for_keypress(True)
    key = tcod.console_check_for_keypress()
    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter for fullscreen toggling
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    # exiting the game
    elif key.vk == tcod.KEY_ESCAPE:
        return True

    global player_y, player_x
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y = player_y - 1

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y = player_y + 1

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x = player_x - 1

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x = player_x + 1
