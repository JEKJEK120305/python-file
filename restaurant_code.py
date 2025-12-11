print("Jek's yummy restaurant\n\n\nMenu list:\n\tA. Chicken\n\tB. Pork\n\tC. Beef\n\tD. Vegetable\n\tE. Drinks\n\n\tAll with rice(50.0 pesos) except drinks.\n")

def restaurant():
    menu = ""
    order = "y"

    while order == 'y':
        order = input("Do you want to order? y/n: ").lower()
        if order == 'y':
            menu = input('\nEnter menu of your choice: ').upper()
            if menu == 'A':
                print("Choose type of Chicken:\nA. Chicken Inasal    ---₱120.0\nB. Chicken Lechon    ---₱250.0")
                chicken = input("Enter chicken of your choice: ").upper()
                if chicken == 'A':
                    print("Chicken Inasal is 120 pesos.")
                    price = 120
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print(f'Your total order is: {tamount}')
                elif chicken == 'B':
                    print("Chicken Lechon is 250 pesos.")
                    price = 250
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print(f'Your total order is: {tamount}')
                else:
                    print("INVALID ka boss layas!")

            elif menu == 'B':
                print("Choose type of Pork:\nA. Pork Steak        ---₱174.0\nB. Bicol Express     ---₱203.0")
                pork = input("Enter pork of your choice: ").upper()
                if pork == 'A':
                    print("Pork Steak is 174 pesos.")
                    price = 174
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print('Your total order is: {}'.format(tamount))
                elif pork == 'B':
                    print("Bicol Express is 203 pesos.")
                    price = 203
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print('Your total order is: {}'.format(tamount))
                else:
                    print("INVALID ka boss layas!")

            elif menu == 'C':
                print("Choose type of Beef:\nA. Mechado    ---₱97.0\nB. Pares      ---₱80.0")
                beef = input("Enter beef of your choice: ").upper()
                if beef == 'A':
                    print("Mechado is 97 pesos.")
                    price = 97
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print(f'Your total order is: {tamount}')
                elif beef == 'B':
                    print("Pares is 80 pesos.")
                    price = 80
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print(f'Your total order is: {tamount}')
                else:
                    print("INVALID ka boss layas!")

            elif menu == 'D':
                print("Choose type of Vegetable:\nA. Ginataang Langka       ---₱100.0\nB. Ginisang Munggo        ---₱125.0")
                vegetable = input("Enter vegetable of your choice: ").upper()
                if vegetable == 'A':
                    print("Ginataang Langka is 100 pesos.")
                    price = 100
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print('Your total order is: {}'.format(tamount))
                elif vegetable == 'B':
                    print("Ginisang Munggo is 125 pesos.")
                    price = 125
                    rice = 50
                    quantity = int(input("\nEnter number of order: "))
                    tamount = (price + rice) * quantity
                    print('Your total order is: {}'.format(tamount))
                else:
                    print("INVALID ka boss layas!")

            elif menu == 'E':
                print("Choose type of Drink:\nA. Coca Cola          ---₱43.0\nB. Mountain Dew       ---₱58.0")
                drink = input("Enter drink of your choice: ").upper()
                if drink == 'A':
                    print("Coca Cola is 43 pesos.")
                    price = 43
                    quantity = int(input("\nEnter number of order: "))
                    tamount = price*quantity
                    print(f'Your total order is: {tamount}')
                elif drink == 'B':
                    print("Mountain Dew is 58 pesos.")
                    price = 58
                    quantity = int(input("\nEnter number of order: "))
                    tamount = price*quantity
                    print(f'Your total order is: {tamount}')
                else:
                    print("INVALID ka boss layas!")
            else:
                print("Invalid ka boss may pambayad ka ba?")

            if menu == 'E':
                continue
            elif menu == 'A' or menu == 'B' or menu == 'C' or menu == 'D':
                extra_rice = input("Do you want extra rice? y/n: ").lower()
                if extra_rice == 'y':
                    e_rice = 50
                    erice_quantity = int(input("Enter number of extra rice: "))
                    t_erice = e_rice*erice_quantity
                    print(f"Total extra rice you've ordered {t_erice}")
                    tamount = (tamount + t_erice)
                elif extra_rice == 'n':
                    continue
                else:
                    print("INVALID!")
            else:
                print("No result!")
        
            
                
        

restaurant()