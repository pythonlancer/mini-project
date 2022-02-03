import csv
from couriers import get_courier
from products import get_product

def order_menu():
    order_menu = '''-------------------Order Menu----------------
0: Return to Main Menu
1: View All Orders
2: Make New Order
3: Update An Entire Order
4. Update An Order Status
4: Delete An Order
---------------------------------------------'''
    print(order_menu)

def view_menu():
    pass

def make_order(menu_item,customer_name,
               customer_address,customer_phone,
               courier_option):
                
                product_cup = get_product(menu_item)
                courier_cup = get_courier(courier_option)

                # open the people.csv and write row from dict
                with open('data/orders.csv', mode='a', newline='') as file:
                    # set the headers for the CSV
                    fieldnames = ['First Name', 'Last Name', 'Age']

