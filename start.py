import products
import couriers
import orders
import customers
import delivery
import statustype

# store the runtime scripts here for all the pages
# i.e products, couriers, orders, customers etc.

# This functions defines our Cafe Main Menu
def boot_main_menu():
    main_menu = '''
----------------Main App Menu-----------------
|0:| Exit                                    |
|1:| Products                                |
|2:| Couriers                                |
|3:| Orders                                  |
|4:| Customers                               |        
|5:| Delivery                                |
|6:| Status                                  |
----------------------------------------------
'''
    print(main_menu)

def boot_products(user): #1 Products Page
    while True:
        products.cafe_menu()
        user_input = int(input(f'Yes {user}, what would you like to do: '))
        if user_input == 0:
            print('\n*******************************************')
            print('* YOU HAVE BEEN REDIRECTED TO THE MAIN MENU *')
            print('*******************************************\n')
            break
        elif user_input == 1:
            products.view_menu()
        elif user_input == 2:                    
            product = input('Enter the new product name: ')   
            price = input(f'Enter the price for {product} : ') 
            products.add_product(product,price)
        elif user_input == 3:
            products.view_menu()
            try:
                old_product = int(input('From the menu above, select the number for the Tea you want to update: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                new_product = input(f'Enter the new Tea name to replace the option above: ')   
                new_price = input(f'Enter the price for {new_product} : ')               
                products.update_product(old_product,new_product,new_price)                    
        elif user_input == 4:
            products.view_menu()
            try:
                delete_product = int(input('From the menu above, select the number for the Tea you want to delete: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                products.delete_product(delete_product)

def boot_couriers(user): #4 Couriers Page ----> working on this <-----
    while True:
        couriers.courier_menu()
        user_input = int(input(f'Yes {user}, what would you like to do: '))
        if user_input == 0:
            print('\n*******************************************')
            print('* YOU HAVE BEEN REDIRECTED TO THE MAIN MENU *')
            print('*******************************************\n')
            break
        elif user_input == 1:
            couriers.view_menu()
        elif user_input == 2:                    
            name = input("Enter the new courier's name: ")
            delivery.view_menu() 
            mode = int(input(f"From the above list, enter the number for {name}'s mode of delivery: "))
            phone = input(f'Enter the phone number for {name}: ') 
            couriers.add_courier(name,mode,phone)
        elif user_input == 3:
            couriers.view_menu()
            try:
                old = int(input('From the menu above, select the number for the Courier you want to update: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS FOR INPUT------ *')
                print('*******************************************\n')
            else:
                name = input('Enter the new courier name to update the record above: ')
                delivery.view_menu()
                try:
                    mode = int(input(f"From the above list, enter the number for {name}'s mode of delivery: "))   
                except Exception as e:
                    print('\n*******************************************')
                    print('* -----CAN ONLY USE NUMBERS FOR INPUT------ *')
                    print('*******************************************\n')
                else:
                    phone = input(f'Enter the phone number for {name}: ')               
                    couriers.update_courier(old,name,mode,phone)                    
        elif user_input == 4:
            couriers.view_menu()
            try:
                delete_customer = int(input('From the menu above, select the number for the Courier you want to delete: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS FOR INPUT------ *')
                print('*******************************************\n')
            else:
                couriers.delete_courier(delete_customer)

def boot_orders(user):#3 Orders Page ------ yet to be done ------
    while True:
        orders.orders_menu()
        user_input = int(input(f'Yes {user}, what would you like to do: '))
        if user_input == 0:
            print('\n*******************************************')
            print('* YOU HAVE BEEN REDIRECTED TO THE MAIN MENU *')
            print('*******************************************\n')
            break
        elif user_input == 1:
            orders.view_menu()
        elif user_input == 2:
            products.view_menu()
            print('-----------------------------------------------------------------------------------')
            print('|If you want to order more than one product, please enter comma separated numbers.|')
            print('|For example you want to order 4 Teas, enter a list like: 1,2,3,4 or 7,10,2,1     |')
            print('-----------------------------------------------------------------------------------')
            menu_item = input('Enter the number(s) for the Tea you want to buy: ')            
            customers.view_menu()
            try:
                customer_name = int(input('Enter the number for the Customer Name: '))
            except Exception as e:
                print('\n***********************************************')
                print('* --CAN ONLY USE A NUMBER FOR CUSTOMER INPUT-- *')
                print('***********************************************\n')
                break
            couriers.view_menu()
            try:
                courier_option = int(input('Enter the number for Courier of your choice: ')) 
            except Exception as e:   
                print('\n*********************************************')
                print('* --CAN ONLY USE A NUMBER FOR COURIER INPUT-- *')
                print('*********************************************\n')   
                break  
            status_option = 1                  
            orders.make_order(customer_name,menu_item,courier_option,status_option)                                                                    
            
        elif user_input == 3:
            orders.view_menu()
            try:
                order_id = int(input('Enter the number for the Order you want to change: '))
            except Exception as e:
                print('\n***********************************************')
                print('* --CAN ONLY USE A NUMBER FOR ORDER INPUT-- *')
                print('***********************************************\n')
                break
            products.view_menu()
            print('-----------------------------------------------------------------------------------')
            print('|If you want to order more than one product, please enter comma separated numbers.|')
            print('|For example you want to order 4 Teas, enter a list like: 1,2,3,4 or 7,10,2,1     |')
            print('-----------------------------------------------------------------------------------')
            menu_item = input('Enter the number(s) for the Tea you want to buy: ')            
            customers.view_menu()
            try:
                customer_name = int(input('Enter the number for the Customer Name you want to update: '))
            except Exception as e:
                print('\n***********************************************')
                print('* --CAN ONLY USE A NUMBER FOR CUSTOMER INPUT-- *')
                print('***********************************************\n')
                break
            couriers.view_menu()
            try:
                courier_option = int(input('Enter the number for Courier of your choice in this update: ')) 
            except Exception as e:   
                print('\n*********************************************')
                print('* --CAN ONLY USE A NUMBER FOR COURIER INPUT-- *')
                print('*********************************************\n')   
                break                                 
            orders.update_order(order_id,customer_name,menu_item,courier_option)
        elif user_input == 4:
            orders.view_menu()
            try:
                order_id = int(input('Enter the number for the Order to change status: '))  
            except Exception as e:
                print('\n***********************************************')
                print('* --CAN ONLY USE A NUMBER FOR ORDER INPUT-- *')
                print('***********************************************\n')
                break            
            statustype.view_menu()   
            try:
                status_option = int(input('Enter new status for this order: ') )
            except Exception as e:
                print('\n***********************************************')
                print('* --CAN ONLY USE A NUMBER FOR STATUS INPUT-- *')
                print('***********************************************\n')
                break                              
            orders.update_order_status(status_option,order_id)                                   
        elif user_input == 5:
            orders.report_menu()
            try:
                report_input = int(input('Choose a report you would like to see: '))
            except Exception as e:
                print('\n***********************************************')
                print('* --CAN ONLY USE A NUMBER FOR THIS INPUT-- *')
                print('***********************************************\n')                            
            if report_input == 0:
                print('\n*********************************************')
                print('* YOU HAVE BEEN REDIRECTED TO THE ORDERS MENU *')
                print('*********************************************\n')
                
            elif report_input == 1:
                couriers.view_menu()
                try:
                    courier_option = int(input('Which courier would you like to use to list the orders?: '))
                except Exception as e:
                    print('\n***********************************************')
                    print('* --CAN ONLY USE A NUMBER FOR COURIER INPUT-- *')
                    print('***********************************************\n')                    
                else:
                    field = 'courier_id'
                    orders.view_orders_by(field,courier_option)
            elif report_input == 2:
                statustype.view_menu()
                try:
                    status_option = int(input('Which status would you like to use to list the orders?: '))
                except Exception as e:
                    print('\n***********************************************')
                    print('* --CAN ONLY USE A NUMBER FOR STATUS INPUT-- *')
                    print('***********************************************\n')                    
                else:
                    field = 'status_id'
                    orders.view_orders_by(field,status_option)
        elif user_input == 6:
            orders.view_menu()
            order_id = int(input('Enter the number for the Order you want to delete: '))                                       
            orders.delete_order(order_id)                    

def boot_customers(user): #4 Customers Page
    while True:
        customers.customer_menu()
        user_input = int(input(f'Yes {user}, what would you like to do: '))
        if user_input == 0:
            print('\n*******************************************')
            print('* YOU HAVE BEEN REDIRECTED TO THE MAIN MENU *')
            print('*******************************************\n')
            break
        elif user_input == 1:
            customers.view_menu()
        elif user_input == 2:                    
            name = input('Enter the new customer name: ')
            address = input(f'Enter the address for {name}: ')   
            phone = input(f'Enter the phone number for {name}: ') 
            customers.add_customer(name,address,phone)
        elif user_input == 3:
            customers.view_menu()
            try:
                old = int(input('From the menu above, select the number for the Customer you want to update: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                name = input('Enter the new customer name to update the record above: ')
                address = input(f'Enter the address for {name}: ')   
                phone = input(f'Enter the phone number for {name}: ')               
                customers.update_customer(old,name,address,phone)                    
        elif user_input == 4:
            customers.view_menu()
            try:
                delete_customer = int(input('From the menu above, select the number for the Customer you want to delete: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                customers.delete_customer(delete_customer)

def boot_delivery_mode(user):#5 Delivery Page
    while True:
        delivery.mode_menu()
        user_input = int(input(f'Yes {user}, what would you like to do: '))
        if user_input == 0:
            print('\n*******************************************')
            print('* YOU HAVE BEEN REDIRECTED TO THE MAIN MENU *')
            print('*******************************************\n')
            break
        elif user_input == 1:
            delivery.view_menu()
        elif user_input == 2:                    
            mode = input('Enter the new delivery mode: ')   
            price = input(f'Enter the price for {mode} delivery: ') 
            delivery.add_delivery_mode(mode,price)
        elif user_input == 3:
            delivery.view_menu()
            try:
                old_mode = int(input('From the menu above, select the number for the Delivery mode you want to update: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                new_mode = input(f'Enter the new Delivery mode to replace the option above: ')   
                new_price = input(f'Enter the price for {new_mode} delivery: ')               
                delivery.update_delivery_mode(old_mode,new_mode,new_price)                    
        elif user_input == 4:
            delivery.view_menu()
            try:
                delete_mode = int(input('From the menu above, select the number for the Delivery mode you want to delete: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                delivery.delete_delivery_mode(delete_mode)

def boot_status(user):#6 Status Page
    while True:
        statustype.status_menu()
        user_input = int(input(f'Yes {user}, what would you like to do: '))
        if user_input == 0:
            print('\n*******************************************')
            print('* YOU HAVE BEEN REDIRECTED TO THE MAIN MENU *')
            print('*******************************************\n')
            break
        elif user_input == 1:
            statustype.view_menu()
        elif user_input == 2:                    
            status = input('Enter the new status type: ')   
            statustype.add_status(status)
        elif user_input == 3:
            statustype.view_menu()
            try:
                old_status = int(input('From the menu above, select the number for the Status type you want to update: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                new_status = input('Enter the new Status type to replace the option above: ')             
                statustype.update_status(old_status,new_status)                    
        elif user_input == 4:
            statustype.view_menu()
            try:
                delete_status = int(input('From the menu above, select the number for the Status type you want to delete: '))
            except Exception as e:
                print('\n*******************************************')
                print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
                print('*******************************************\n')
            else:
                statustype.delete_status(delete_status)
