from menu import menu, shortcuts, pausa

def main():
    title = "Menu"
    items = ["1 Shortcuts", 
             "2 Option", 
             "3 Option", 
             "Exit"]

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            print('Shortcuts 1')
            shortcuts()
            pausa(0)
        elif (opc == 2):
            print('Option 2')
            pausa(0)
        elif (opc == 3):
            print('Option 3')
            pausa(0)
    
        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
