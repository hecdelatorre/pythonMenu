from menu import menu, shortcuts, multi_select, pausa

def main():
    title = "Menu"
    items = ["1 Shortcuts", 
             "2 MultiSelect", 
             "3 Option", 
             "Exit"]

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            print('Shortcuts')
            shortcuts()
            pausa(0)
        elif (opc == 2):
            print('MultiSelect')
            multi_select()
            pausa(0)
        elif (opc == 3):
            print('Option 3')
            pausa(0)
    
        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
