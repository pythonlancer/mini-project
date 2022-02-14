import products
from prettytable import PrettyTable
from textwrap import fill


def get_products(product_order_list):
    new_list = []
    product_list = []
    
    product_order_list = product_order_list.split(',')   
    
    for item in product_order_list:
        product = products.get_product(int(item)-1)
        new_list.append(product)

    order_product_count = len(product_order_list)     
    
    for number in range(0,order_product_count):
        x = new_list[number]
        x = x.replace('\n','')
        x = x.split(',')
        product_list.append(x[0])
    product_list = ' & '.join(product_list)
    # product_list = f"'''\n{product_list}\n'''"
    product_list = f'{product_list}'

    return product_list

def get_products_price(product_order_list):
    new_list = []
    product_list_price = 0
    product_order_list = product_order_list.split(',')
    #print(product_order_list)
    for item in product_order_list:
        product = products.get_product(int(item)-1)
        new_list.append(product)

    order_product_count = len(product_order_list)

    for number in range(0,order_product_count):
        x = new_list[number].replace('\n','')
        x = x.split(',')
        x = x[1]
        x = x.replace(' ','')
        y = float(x)
        product_list_price += y
    return product_list_price

# products.view_menu()
# product_order_list = input('enter number(s) for the Tea you wantto buy: ')

# x = product_order_list.split(',')
# y = len(x)
# z = products.get_list_length()
# if y <= z:
#     p = get_products(product_order_list)
#     c = get_products_price(product_order_list)
#     print(f'You ordered for [{p}] and the cost is £{c}')
# else:
#     print('\n*******************************************')
#     print('* YOUR PRODUCT SELECTION IS OUT OF RANGE *')
#     print('*******************************************\n')



# def view_menu():
#     table_line = PrettyTable([
#                 '#',
#                 'Customer Name',
#                 'Customer Address',
#                 'Customer Phone',   
#                 'Product Order',
#                 'Price(£)',
#                 'Courier',
#                 'Delivery Mode',
#                 'Delivery Charge(£)',
#                 'Total Payment(£)',
#                 'Order Status'])

#     number = 1

#     try:
#         with open("data/temp.txt", 'r') as file:
#             csv_file = file.readlines()
#             for row in csv_file: 
                
#                # row = row.split(',')
#                 # row_3 = row[3]
#                 # if '|' in row_3:
#                 #     row_3.replace('|','\n')
                
#                 # print(row[3])                                         
#                 #row = str(number) + ',' + row
#                 #row = row.replace('|','')
#                 row = row.split(',')
#                 row[3] = fill(row[3], width=20)
#                 #table_line.add_row(row)
#                 number += 1
#             #print(table_line)
#             print(row)

#     except Exception as e:
#         print('Failed to open and read orders.txt, this is the error: ', e)

# view_menu()