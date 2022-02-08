import csv
from couriers import get_courier,get_delivery_cost
from products import get_product
from prettytable import PrettyTable

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
    table_line = PrettyTable(['Customer Name',
                'Customer Address',
                'Customer Phone',   
                'Product Order',
                'Price(£)',
                'Courier',
                'Delivery Mode',
                'Delivery Charge(£)',
                'Total Payment(£)',
                'Order Status'])

    #print(' '.join(table_line))

    try:
        with open("data/orders.txt", 'r') as file:
            next(file)
            csv_file = csv.reader(file)
            #print(csv_file)
            for row in csv_file:
                #table_line.add_row(row)
                print(row)
            #print(table_line)

    except Exception as e:
        print('Failed to open and read orders.txt, this is the error: ', e)

view_menu()

def make_order(menu_item,customer_name,customer_address,customer_phone,courier_option):
                
                menu_item -= 1
                courier_option -= 1
                product_cup = get_product(menu_item)
                product_line = product_cup.split(',')
                product = product_line[0]
                product_price = product_line[1]
                product_price = product_price.replace('\n','')

                courier_cup = get_courier(courier_option)
                courier_line = courier_cup.split(',')
                courier = courier_line[0]
                courier_mode = courier_line[1]
                courier_mode = courier_mode.replace('\n','')
                courier_mode = courier_mode.replace(' ','')
                delivery_charge = get_delivery_cost(courier_mode)
                total_payment = float(product_price) + float (delivery_charge)
                order_status = 'preparing'

                customer_order = {
                    'Customer Name': customer_name, 
                    'Customer Address': customer_address, 
                    'Customer Phone': customer_phone,
                    'Product Order': product,
                    'Price': product_price,
                    'Courier': courier,
                    'Delivery Mode': courier_mode,
                    'Delivery Charge': delivery_charge,
                    'Total Payment': total_payment,
                    'Order Status': order_status
                }
            
                try:
                    # open the people.csv and write row from dict
                    with open('data/orders.csv', 'a', newline='') as file:
                        # set the headers for the CSV
                        fieldnames = ['Customer Name', 
                                    'Customer Address', 
                                    'Customer Phone',
                                    'Product Order',
                                    'Price',
                                    'Courier',
                                    'Delivery Mode',
                                    'Delivery Charge',
                                    'Total Payment',
                                    'Order Status'
                                    ]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        # instruct the writer to know to write the headers
                        #writer.writeheader()
                        writer.writerow(customer_order)
                        view_menu()

                except Exception as e:
                     print('Failed to write to orders.txt, this is the error: ', e)

