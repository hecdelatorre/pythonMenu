# pip install simple-term-menu

from simple_term_menu import TerminalMenu
import time

def pausa(t = 1): 
    if(t == 0): input('--Press ENTER to continue--')
    else: time.sleep(t)

def menu(title, items):

    main_menu = TerminalMenu (
        menu_entries = items,
        title = f'  {title}',
        menu_cursor = "❯ ",
        menu_cursor_style = ("fg_cyan", "bold"),
        menu_highlight_style = ("fg_gray", "fg_cyan"),
        cycle_cursor = True,
        clear_screen = True
    )
    
    num = main_menu.show()
    num = num + 1 if num is not None else exit()
    return num

def shortcuts():
    fruits = ["[a] apple", "[b] banana", "[o] orange"]
    menu = TerminalMenu (
        fruits, 
        title = "  Fruits",
        menu_cursor = "❯ ",
        menu_cursor_style = ("fg_cyan", "bold"),
        menu_highlight_style = ("fg_gray", "fg_cyan"),
        shortcut_key_highlight_style = ("fg_green",),
        shortcut_brackets_highlight_style = ("fg_green",)
    )

    index = menu.show()
    print(index)

def multi_select():
    animals = ["dog", "cat", "mouse", "squirrel"]
    terminal_menu = TerminalMenu(
        animals,
        multi_select=True,
        show_multi_select_hint=False,
        title = "  Animals",
        menu_cursor = "❯ ",
        menu_cursor_style = ("fg_cyan", "bold"),
        menu_highlight_style = ("fg_gray", "fg_cyan")
    )
    menu_entry_indices = terminal_menu.show()
    print(menu_entry_indices)
    print(terminal_menu.chosen_menu_entries)
