from menu import menu, pausa

def main():
    title = "Menu"
    items = ["1 Opc", 
             "2 Opc", 
             "3 Opc", 
             "Exit"]

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            print('Op 1')
            pausa()
        elif (opc == 2):
            print('Op 2')
            pausa()
        elif (opc == 3):
            print('Op 3')
            pausa()
    
        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
