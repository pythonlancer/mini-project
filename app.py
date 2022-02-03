# Import all important packages: products, couriers and orders
import os
import products
import couriers


# This functions defines our Cafe Main Menu
def main_menu():
    main_menu = '''-------------------Main App Menu----------------
    0: Exit
    1: Products
    2: Couriers
    3: Orders
    ---------------------------------------------'''
    print(main_menu)

def start_app(user):
    while True:
        main_menu()
        app_open = int(input(f"{name.capitalize()}, Welcome to Tea Cafe App, what would you like to do: "))

        if app_open == 0: # quit the application here
            print("App successfully terminated. Thank you for using Tea Cafe App")
            break

        elif app_open == 1: # running the products department
            while True:
                products.cafe_menu()
                user_input = int(input(f'Yes {user}, what would you like to do: '))
                if user_input == 0:
                    print("You have been redirected to the main menu")
                    break
                elif user_input == 1:
                    #os.system('clear')                    
                    products.view_menu()
                elif user_input == 2:
                    product = input('Enter the new product name: ')   
                    price = input(f'Enter the price for {product} : ') 
                    products.add_product(product,price)
                elif user_input == 3:
                    old_product = input('Enter the Tea name you want to update: ')   
                    new_product = input(f'Enter the new Tea to replace {old_product}: ')   
                    new_price = input(f'Enter the price for {new_product} : ')               
                    new_product = f'{new_product}, {new_price}'
                    products.update_product(old_product,new_product)
                elif user_input == 4:
                    delete_product = input('Enter the tea name to delete from menu: ')   
                    products.delete_product(delete_product)

        elif app_open == 2: # running the courier department
            while True:
                couriers.courier_menu()
                user_input = int(input(f'Yes {user}, what would you like to do: '))
                if user_input == 0:
                    print("You have been redirected to the main menu")
                    break
                elif user_input == 1:
                    #os.system('cls')
                    couriers.view_menu()
                elif user_input == 2:
                    courier = input('Enter the new courier name: ')   
                    mode = input(f'Enter the delivery mode for {courier} : ') 
                    couriers.add_courier(courier,mode)
                elif user_input == 3:
                    old_courier = input('Enter the courier name you want to update: ')   
                    new_courier = input(f'Enter the new courier to replace {old_courier}: ')   
                    new_mode = input(f'Enter the delivery mode for {new_courier}: ')               
                    new_courier = f'{new_courier}, {new_mode}'
                    couriers.update_courier(old_courier,new_courier)
                elif user_input == 4:
                    delete_courier = input('Enter the courier name to delete from Courier List: ')   
                    couriers.delete_courier(delete_courier)
                elif user_input == 5:
                    #os.system('cls')
                    couriers.delivery_menu()


name = input('Please provide your name to login: ')
        
start_app(name)

