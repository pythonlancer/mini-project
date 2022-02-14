import csv
import time

from prettytable import PrettyTable

import products
import couriers


def orders_menu():
    order_menu = '''-------------------Order Menu----------------
0: Return to Main Menu
1: View All Orders
2: Make New Order
3: Update An Entire Order
4. Update An Order Status
5: Delete An Order
---------------------------------------------'''
    print(order_menu)

def view_menu():
    table_line = PrettyTable([
                '#',
                'Customer Name',
                'Customer Address',
                'Customer Phone',   
                'Product Order',
                'Price(£)',
                'Courier',
                'Delivery Mode',
                'Delivery Charge(£)',
                'Total Payment(£)',
                'Order Status'])

    number = 1

    try:
        with open("data/temp.txt", 'r') as file:
            csv_file = file.readlines()
            for row in csv_file: 
                
                # row = row.split(',')
                # row_3 = row[3]
                # if '|' in row_3:
                #     row_3.replace('|','\n')
                # row[3] = row_3
                # print(row[3])                                         
                row = str(number) + ',' + row
                row = row.replace('\n','')
                row = row.split(',')
                table_line.add_row(row)
                number += 1
            print(table_line)

    except Exception as e:
        print('Failed to open and read orders.txt, this is the error: ', e)

def make_order(menu_item,customer_name,customer_address,customer_phone,courier_option):                                                    

                product = products.get_products(menu_item)
                product_price = products.get_products_price(menu_item)
                product_price = str(product_price)
                # if menu_item:
                #         print('\n*******************************************')
                #         print(f'* YOUR PRODUCT SELECTION IS {product}:{product_price} *')
                #         print('*******************************************')
                # return 0                
                courier_option -= 1       
                courier_cup = couriers.get_courier(courier_option)
                courier_line = courier_cup.split(',')
                courier = courier_line[0]
                courier_mode = courier_line[1]
                courier_mode = courier_mode.replace('\n','')
                courier_mode = courier_mode.replace(' ','')
                delivery_charge = couriers.get_delivery_cost(courier_mode)
                delivery_charge = str(delivery_charge)
                total_payment = float(product_price) + float (delivery_charge)
                total_payment = str(total_payment)
                order_status = 'preparing'                

                customer_order = [
                     customer_name, 
                     customer_address, 
                     customer_phone,
                     product,
                     product_price,
                     courier,
                     courier_mode,
                     delivery_charge,
                     total_payment,
                     order_status
                ]
                
                try:
                    # open the orders.txt and write row
                    with open('data/temp.txt', 'a') as file:
                        item = ','.join(customer_order)
                        file.write(item + '\n')
                        print('New Order was successfully added')
                        #view_menu()
                        
                except Exception as e:
                     print('Failed to write to orders.txt, this is the error: ', e)


def update_order(old_order,menu_item,customer_name,customer_address,customer_phone,courier_option): #

    # menu_item -= 1
    # courier_option -= 1
    # product_cup = products.get_product(menu_item)
    # product_line = product_cup.split(',')
    # product = product_line[0]
    # product_price = product_line[1]
    # product_price = product_price.replace('\n','')

    product = products.get_products(menu_item)
    product_price = products.get_products_price(menu_item)
    product_price = str(product_price)
    # if menu_item:
    #         print('\n*******************************************')
    #         print(f'* YOUR PRODUCT SELECTION IS {product}:{product_price} *')
    #         print('*******************************************')
    # return 0                
    courier_option -= 1
    courier_cup = couriers.get_courier(courier_option)
    courier_line = courier_cup.split(',')
    courier = courier_line[0]
    courier_mode = courier_line[1]
    courier_mode = courier_mode.replace('\n','') 
    courier_mode = courier_mode.replace(' ','')
    delivery_charge = couriers.get_delivery_cost(courier_mode)
    delivery_charge = str(delivery_charge)
    total_payment = float(product_price) + float (delivery_charge)
    total_payment = str(total_payment)
    order_status = 'preparing'
    
    number = 1
    new_list = []
    try:
        with open("data/temp.txt", 'r') as file:
            csv_file = file.readlines()
            
            for row in csv_file:                                
                row = row.replace('\n','')
                row = row.split(',')
                if number == old_order:
                    row[0] = customer_name
                    row[1] = customer_address
                    row[2] = customer_phone
                    row[3] = product
                    row[4] = product_price
                    row[5] = courier
                    row[6] = courier_mode
                    row[7] = delivery_charge
                    row[8] = total_payment
                    row[9] = order_status
                row = ','.join(row)
                row = row +'\n'
                new_list.append(row)     
                number += 1          
            try:
                # open the orders.txt and write rows
                with open('data/temp.txt', 'w') as  updateOrder:
                    
                    updateOrder.writelines(new_list)
                    print(f'Order [# {old_order}] was successfully updated')
                    
            except Exception as e:
                    print('Failed to write to orders.txt, this is the error: ', e)

    except Exception as e:
        print('Failed to open and read orders.txt, this is the error: ', e)

def update_order_status(order_id,status_option): #
    
    number = 1
    new_list = []
    try:
        with open("data/orders.txt", 'r') as file:
            csv_file = file.readlines()
            
            for row in csv_file:                                
                row = row.replace('\n','')
                row = row.split(',')
                if number == order_id:                    
                    row[9] = status_option
                row = ','.join(row)
                row = row +'\n'
                new_list.append(row)    
                number += 1      
            try:
                # open the orders.txt and write rows
                with open('data/orders.txt', 'w') as  updateOrder:
                    
                    updateOrder.writelines(new_list)
                    print(f'Order Status for [ORDER# {order_id}] was successfully updated')
                    #view_menu()
                    
            except Exception as e:
                    print('Failed to write to orders.txt, this is the error: ', e)

    except Exception as e:
        print('Failed to open and read orders.txt, this is the error: ', e)



def delete_order(order_id):
    number = 1
    new_list = []
    try:
        with open("data/orders.txt", 'r') as file:
            csv_file = file.readlines()
            
            for row in csv_file:                                
                row = row.replace('\n','')
                row = row.split(',')
                if number == order_id:                    
                    #del row[:]
                    continue
                row = ','.join(row)
                row = row +'\n'
                new_list.append(row)    
                number += 1      
            try:
                # open the orders.txt and write rows
                with open('data/temp.txt', 'w') as  deleteOrder:
                    
                    deleteOrder.writelines(new_list)
                    print(f'Order [ORDER# {order_id}] was successfully deleted')
                    #view_menu()
                    
            except Exception as e:
                    print('Failed to write to orders.txt, this is the error: ', e)

    except Exception as e:
        print('Failed to open and read orders.txt, this is the error: ', e)
