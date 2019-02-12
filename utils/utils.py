import os


def line_break():
    print('\n')


def clear():
    clear_screen = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_screen)
