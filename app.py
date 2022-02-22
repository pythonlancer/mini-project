# Import all important packages: products, couriers, orders etc.
import start

def start_app(user):
    while True:
        start.boot_main_menu()
        try:
            app_open = int(input(f"{name.capitalize()}, Welcome to Tea Cafe App, What page would you like to visit?: "))        
        except Exception as e:
            print('\n*******************************************')
            print('* -----CAN ONLY USE NUMBERS AS INPUT------ *')
            print('*******************************************\n')
        
        if app_open == 0: # quit the application here
            print('\n*****************************************************************')
            print('* APP SUCCESSFULLY TERMINATED. THANK YOU FOR USING TEA CAFE APP *')
            print('*****************************************************************\n')
            break

        elif app_open == 1: # running the products department            
            start.boot_products(user)

        elif app_open == 2: # running the courier department
            start.boot_couriers(user)
       
        elif app_open == 3: # running the orders department            
            start.boot_orders(user)
        
        elif app_open == 4: # running the customers department
            start.boot_customers(user)

        elif app_open == 5: # running the delivery Mode department
            start.boot_delivery_mode(user)

        elif app_open == 6: # running the Status Type department
            start.boot_status(user)

name = input('Please provide your name to login: ')
        
start_app(name)

