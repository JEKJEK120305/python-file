print("Jek's yummy restaurant\n\n\nMenu list:\n\tA. Chicken\n\tB. Pork\n\tC. Beef\n\tD. Vegetable\n\tE. Drinks\n\n\tAll with rice(50.0 pesos) except drinks.\n")

def restaurant():
    menu = ""
    order = "y"

    while order == 'y':
        order = input("Do you want to order? y/n: ").lower()
        if order == 'y':
            menu = input('\nEnter menu of your choice: ').upper()
            if menu == 'A':
                print("Choose type of chicken:\nA. Chicken Inasal    ---₱120.0\nB. Chicken Lechon    ---₱250.0")
                chicken = input("Enter chicken of your choice: ").upper()
                if chicken == 'A':
                    print("Chicken Inasal is 120 pesos.")
                    price = 120
                    quantity = int(input("\nEnter number of order: "))
                    tamount = price * quantity
                    print(f'Your total order is: {tamount}')
                elif chicken == 'B':
                    print("Chicken Lechon is 250 pesos.")
                    price = 250
                    quantity = int(input("\nEnter number of order: "))
                    tamount = price * quantity
                    print(f'Your total order is: {tamount}')
                else:
                    print("INVALID ka boss layas!")
restaurant()                       