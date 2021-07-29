# pip install simple-term-menu

from simple_term_menu import TerminalMenu
import time

def pausa(t=3):
    time.sleep(t)

def menu(title, items):
    main_menu_cursor = "❯ "
    main_menu_cursor_style = ("fg_cyan", "bold")
    main_menu_style = ("fg_gray", "fg_cyan")

    main_menu = TerminalMenu(
        menu_entries = items,
        title = title,
        menu_cursor = main_menu_cursor,
        menu_cursor_style = main_menu_cursor_style,
        menu_highlight_style = main_menu_style,
        cycle_cursor = True,
        clear_screen = True
    )
    
    num = main_menu.show()
    num += 1
    return num

title = "  Menu"
items = ["1 Opc", 
         "2 Opc", 
         "3 Opc", 
         "Exit"]

repeat = True
while repeat:
    opc = menu(title, items)

    if(opc == 1):
        print('Op 1')
        pausa()
    elif (opc == 2):
        print('Op 2')
        pausa()
    elif (opc == 3):
        print('Op 3')
        pausa()

    repeat = (opc < 4)
