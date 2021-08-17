# pip install simple-term-menu

from simple_term_menu import TerminalMenu
import time

def pausa(t = 1): 
    if(t == 0): input(' Press ENTER to continue ')
    else: time.sleep(t)

def menu(title, items):
    cursor = "❯ "
    cursor_style = ("fg_cyan", "bold")
    menu_style = ("fg_gray", "fg_cyan")

    main_menu = TerminalMenu(
        menu_entries = items,
        title = f'  {title}',
        menu_cursor = cursor,
        menu_cursor_style = cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )
    
    num = main_menu.show()
    num = num + 1 if num is not None else exit()
    return num

def shortcuts():
    fruits = ["[a] apple", "[b] banana", "[o] orange"]
    terminal_menu = TerminalMenu(fruits, 
                                 title = "Fruits",
                                 menu_cursor = "❯ ",
                                 shortcut_key_highlight_style = ("fg_red",),
                                 shortcut_brackets_highlight_style = ("fg_red",),
                                )

    menu_entry_index = terminal_menu.show()
    print(menu_entry_index)

def multi_select():
    terminal_menu = TerminalMenu(
        ["dog", "cat", "mouse", "squirrel"],
        multi_select=True,
        show_multi_select_hint=False,
    )
    menu_entry_indices = terminal_menu.show()
    print(menu_entry_indices)
    print(terminal_menu.chosen_menu_entries)
