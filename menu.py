# pip install simple-term-menu

from simple_term_menu import TerminalMenu
import time

def pausa(t = 1):
    time.sleep(t)

def menu(title, items):
    cursor = "❯ "
    cursor_style = ("fg_cyan", "bold")
    menu_style = ("fg_gray", "fg_cyan")

    main_menu = TerminalMenu(
        menu_entries = items,
        title = title,
        menu_cursor = cursor,
        menu_cursor_style = cursor_style,
        menu_highlight_style = menu_style,
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
         "4 Opc", 
         "5 Opc", 
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

    repeat = (opc < len(items))
