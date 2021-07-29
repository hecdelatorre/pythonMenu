# pip install simple-term-menu

from simple_term_menu import TerminalMenu
import time

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
    print(opc)
    time.sleep(3)
    repeat = (opc < 4)
