import os


def clear():
    clear_screen = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_screen)
