from src.db import db
from prettytable import PrettyTable
import os
from dotenv import load_dotenv

# Load environment variables

load_dotenv()
products_table = os.environ.get("products_table")
add_record_to = os.environ.get("add_record")
get_all_records_from = os.environ.get("get_all_records")
update_table = os.environ.get("update_table")
delete_from = os.environ.get('delete_from_table')


def cafe_menu():
    cafe_menu = '''
-----------------Product Menu-----------------
|0:| Return to Main Menu                     |
|1:| View Tea Menu                           |
|2:| Add New Tea                             |
|3:| Update Tea Menu                         |
|4:| Delete Tea Item                         | 
----------------------------------------------
'''
    print(cafe_menu)

def view_menu():
    heading = ['#','Product Name','Price(£)']
    menu = 'TEA MENU'             
    sql = f'{get_all_records_from} {products_table}' 
    db.read_record_from_db(sql,heading,menu)    


def add_product(product, price):
    sql = f'{add_record_to} {products_table}(product,price) VALUES (%s,%s)'
    inserts = (product,price)
    db.add_record_to_db(sql,inserts,product)
            

def update_product(old_product,new_product,price):
    
    if old_product != 0 and new_product != '' and price !='':
        #print('1st: ',old_product,new_product,price)
        sql = f'{update_table} {products_table} SET product = %s, price = %s WHERE product_id = %s'
        inserts = (new_product,price,old_product)
        db.update_record_in_db(sql,inserts,new_product)
    elif old_product != 0 and new_product != '': 
        #print('2nd: ',old_product,new_product,price)
        sql = f'{update_table} {products_table} SET product = %s WHERE product_id = %s'
        inserts = (new_product,old_product)
        db.update_record_in_db(sql,inserts,new_product)
    elif old_product != 0 and price != '': 
        #print('3rd: ',old_product,new_product,price)
        sql = f'{update_table} {products_table} SET price = %s WHERE product_id = %s'
        inserts = (price,old_product)
        db.update_record_in_db(sql,inserts,new_product)
    else:
        print('\n*******************************************')
        print(f'* ----CANNOT UPDATE DUE TO EMPTY INPUT---- *')
        print('*******************************************\n')

    
def delete_product(product):
    sql = f'{delete_from} {products_table} WHERE product_id = %s'
    inserts = (product,)
    db.delete_record_from_db(sql,inserts)   
        

# def get_product(product_id):
#     try:
#         with open('data/products.txt','r') as products:
#             lines = products.readlines()
                
#         for line in lines:
#             if lines.index(line) == product_id:
#                 return line            
                            
#     except Exception as e:
#         print('Failed to open products.txt, this is the error: ', e)

# def get_list_length():
#     menu_number = 1
#     try:
#         with open('data/products.txt','r') as products:
#             lines = products.readlines()
                
#         for line in lines:
#             menu_number+=1                
#     except Exception as e:
#         print('Failed to open products.txt, this is the error: ', e)    

#     return menu_number

# def get_products(product_order_list):
#     new_list =[]
#     product_list = []
    
#     product_order_list = product_order_list.split(',')
#     for item in product_order_list:
#         product = get_product(int(item)-1)
#         new_list.append(product)        

#     order_product_count = len(product_order_list)

#     for number in range(0,order_product_count):
#         x = new_list[number].replace('\n','')
#         x = x.split(',')        
#         product_list.append(x[0])
#     product_list = ' & '.join(product_list)
#     product_list = f'{product_list}'

#     return product_list

# def get_products_price(product_order_list):
#     new_list =[]
#     product_list_price = 0
#     product_order_list = product_order_list.split(',')
#     for item in product_order_list:
#         product = get_product(int(item)-1)
#         new_list.append(product)

#     order_product_count = len(product_order_list)

#     for number in range(0,order_product_count):
#         x = new_list[number].replace('\n','')
#         x = x.split(',')
#         x = x[1]
#         x = x.replace(' ','')
#         y = float(x)
#         product_list_price += y
#     return product_list_price