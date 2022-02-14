# Import all important packages: products, couriers and orders
import os
import products
import couriers
import orders
import validator
#from prettytable import PrettyTable


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
        # result = validator.check_int_input(app_open)
        # print(result)
        
        # if result == True:
        #     print('yes')
        # # except:
        # #     print('\n*******************************************')
        # #     print('* ONLY NUMBERS ARE ALLOWED FOR THIS INPUT *')
        # #     print('*******************************************\n')
            
        
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
       
        elif app_open == 3: # running the orders department
            while True:
                orders.orders_menu()
                user_input = int(input(f'Yes {user}, what would you like to do: '))
                if user_input == 0:
                    print("You have been redirected to the main menu")
                    break
                elif user_input == 1:
                    orders.view_menu()
                elif user_input == 2:
                    products.view_menu()
                    menu_item = input('Enter the number for the Tea you want to buy: ')
                    
                    customer_name = input('Enter Customer Name: ')
                    customer_address = input('Enter Customer Address: ')
                    customer_phone = input('Enter Customer Phone: ')
                    couriers.view_menu()
                    courier_option = int(input('Enter the number for Courier of your choice: ')) 

                    product_order_list = menu_item.split(',')
                    order_product_count = len(product_order_list)
                    product_list_length = products.get_list_length()
                    if order_product_count <= product_list_length:                        
                        orders.make_order(menu_item,customer_name,customer_address,customer_phone,courier_option)                                                                    
                    else:
                        print('\n*******************************************')
                        print(f'* YOUR PRODUCT SELECTION [{menu_item}] IS OUT OF RANGE *')
                        print('*******************************************')
                elif user_input == 3:
                    orders.view_menu()
                    old_order = int(input('Enter the number for the Order you want to update: '))
                    products.view_menu()
                    menu_item = input('Enter the number for the Tea you want to buy for this update: ')
                    customer_name = input('Enter Customer Name: ')
                    customer_address = input('Enter Customer Address: ')
                    customer_phone = input('Enter Customer Phone: ')
                    couriers.view_menu()
                    courier_option = int(input('Enter the number of Courier of your choice: '))                   
                    orders.update_order(old_order,menu_item,customer_name,customer_address,customer_phone,courier_option)
                elif user_input == 4:
                    orders.view_menu()
                    order_id = int(input('Enter the number for the Order to change status: '))                    
                    status_option = input('Enter new status for this order: ')                   
                    orders.update_order_status(order_id,status_option)
                elif user_input == 5:
                    orders.view_menu()
                    order_id = int(input('Enter the number for the Order you want to delete: '))                                       
                    orders.delete_order(order_id)                    


name = input('Please provide your name to login: ')
        
start_app(name)

