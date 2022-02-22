from src.db import db
from prettytable import PrettyTable
import os
from dotenv import load_dotenv

# Load environment variables

load_dotenv()
test_table = os.environ.get("test_table")

orders_table = os.environ.get("orders_table")
product_track = os.environ.get("product_track")
products_table = os.environ.get("products_table")
couriers_table = os.environ.get("couriers_table")
status_table = os.environ.get("status_table")
customers_table = os.environ.get("customers_table")
delivery_table = os.environ.get("delivery_table")

get_customer_name_from = os.environ.get("get_customer_name")
get_courier_id_from = os.environ.get("get_courier_id")
get_product_id_from = os.environ.get("get_product_id")
get_status_id_from = os.environ.get("get_status_id")

check_for_product_id = os.environ.get("column_nameP")
check_for_courier_id = os.environ.get("column_nameC")
check_for_customer_id = os.environ.get("column_nameCS")
check_for_status_id = os.environ.get("column_nameS")
check_for_order_id = os.environ.get("column_nameOR")

add_record_to = os.environ.get("add_record")
get_all_records_from = os.environ.get("get_all_records")
update_the = os.environ.get("update_table")
delete_from = os.environ.get('delete_from_table')


def orders_menu():
    order_menu = '''
------------Customer List Menu----------------
|0:| Return to Main Menu                     |
|1:| View All Orders                         |
|2:| Make New Order                          |
|3:| Update An Entire Order                  |
|4:| Update An Order Status                  |
|5:| Orders Reports                          |
|6:| Delete Order                            | 
----------------------------------------------
'''
    print(order_menu)

def report_menu():
    report_menu = '''
----------------Reports  Menu-----------------
|0:| Return to Orders Menu                   |
|1:| Order List by Courier                   |
|2:| Order List by Status                    |
----------------------------------------------
'''
    print(report_menu)

def view_menu():
    heading = [
                'Orders #',
                'Customer Name',
                'Customer Address',
                'Phone Number',  
                'Courier', 
                'Product',                
                'Price',                
                'Delivery mode',
                'Delivery Cost',
                'Status']
    menu = 'ORDER LIST'    
    switch = 0
    sql = f'''
    SELECT {orders_table}.order_id, {customers_table}.full_name, {customers_table}.address, {customers_table}.phone_number, {couriers_table}.courier, 
    {products_table}.product, {products_table}.price, {delivery_table}.mode, {delivery_table}.cost,{status_table}.status 
    FROM {orders_table}
    JOIN {product_track} on {orders_table}.order_id = {product_track}.order_id
    JOIN {products_table} on {product_track}.product_id = {products_table}.product_id
    JOIN {customers_table} on {orders_table}.customer_id = {customers_table}.customer_id
    JOIN {couriers_table} on {orders_table}.courier_id = {couriers_table}.courier_id
    JOIN {delivery_table} on {couriers_table}.delivery_id = {delivery_table}.delivery_id
    JOIN {status_table} on {orders_table}.status_id = {status_table}.status_id
    WHERE switch = {switch}
    ORDER BY {orders_table}.order_id ASC
    '''                 
    db.read_order_records_from_db(sql,heading,menu)

def view_orders_by(field,keyword):
    heading = [
                'Orders #',
                'Customer Name',
                'Customer Address',
                'Phone Number',  
                'Courier', 
                'Product',                
                'Price',                
                'Delivery mode',
                'Delivery Cost',
                'Status']
    menu = 'ORDER LIST'    
    switch = 0
    sql = f'''
    SELECT {orders_table}.order_id, {customers_table}.full_name, {customers_table}.address, {customers_table}.phone_number, {couriers_table}.courier, 
    {products_table}.product, {products_table}.price, {delivery_table}.mode, {delivery_table}.cost,{status_table}.status 
    FROM {orders_table}
    JOIN {product_track} on {orders_table}.order_id = {product_track}.order_id
    JOIN {products_table} on {product_track}.product_id = {products_table}.product_id
    JOIN {customers_table} on {orders_table}.customer_id = {customers_table}.customer_id
    JOIN {couriers_table} on {orders_table}.courier_id = {couriers_table}.courier_id
    JOIN {delivery_table} on {couriers_table}.delivery_id = {delivery_table}.delivery_id
    JOIN {status_table} on {orders_table}.status_id = {status_table}.status_id
    WHERE switch = {switch} AND {orders_table}.{field} = {keyword}
    ORDER BY {orders_table}.order_id ASC
    '''                 
    db.read_order_records_from_db(sql,heading,menu)

def make_order(customer_option,product_options,courier_option,status_option):
        
    product_list = product_options.split(',')
    for product in product_list:
        product = int(product)
        product_check = check_if_id_exists(get_product_id_from,products_table,check_for_product_id,product)
        if product_check == product:
            pass
        else:
            print('\n**********************************************************')
            print(f"PRODUCT WITH [No: {product}] DOESN'T EXIST IN OUR DATABASE.")
            print("-WE DID NOT PROCESS THIS CUSTOMER'S ORDER, PLEASE TRY AGAIN-")
            print('**********************************************************\n')
            break
    
    else:
        customer = check_if_id_exists(get_customer_name_from,customers_table,check_for_customer_id,customer_option)
        status = check_if_id_exists(get_status_id_from,status_table,check_for_status_id,status_option)
        courier = check_if_id_exists(get_courier_id_from,couriers_table,check_for_courier_id,courier_option)
        if customer != None and courier == courier_option and status == status_option:

            sql = f'{add_record_to} {orders_table}(customer_id,courier_id,status_id) VALUES (%s,%s,%s)'
            inserts = (customer_option,courier_option,status_option)
            last_id = db.add_order_record_to_db(sql,inserts,customer)   
            
            if last_id > 0:
                for product in product_list:
                    product = int(product)
                    sql = f'{add_record_to} {product_track}(order_id,product_id) VALUES (%s,%s)'
                    inserts = (last_id,product)
                    db.add_product_on_order_record_to_db(sql,inserts,customer)
                

def update_order(order_id,customer_option,product_options,courier_option):
        
    product_list = product_options.split(',')
    for product in product_list:
        product = int(product)
        product_check = check_if_id_exists(get_product_id_from,products_table,check_for_product_id,product)
        if product_check == product:
            pass
        else:
            print('\n**********************************************************')
            print(f"PRODUCT WITH [No: {product}] DOESN'T EXIST IN OUR DATABASE.")
            print("-WE DID NOT PROCESS THIS CUSTOMER'S ORDER, PLEASE TRY AGAIN-")
            print('**********************************************************\n')
            break
    
    else:
        customer = check_if_id_exists(get_customer_name_from,customers_table,check_for_customer_id,customer_option)
        courier = check_if_id_exists(get_courier_id_from,couriers_table,check_for_courier_id,courier_option)
        if customer != None and courier == courier_option:

            sql = f'{update_the} {orders_table} SET customer_id = %s, courier_id = %s WHERE order_id = %s'
            inserts = (customer_option,courier_option,order_id)
            message = "this order's"
            db.update_record_in_db(sql,inserts,message)   
            #delete products in produsts_on_order first
            sql = f'{delete_from} {product_track} WHERE order_id = %s'
            inserts = (order_id,)
            db.delete_record_from_db(sql,inserts) 
                        
            for product in product_list:
                product = int(product)
                sql = f'{add_record_to} {product_track}(order_id,product_id) VALUES (%s,%s)'
                inserts = (order_id,product)
                placeholder = ''
                db.add_product_on_order_record_to_db(sql,inserts,placeholder)

def delete_order(order_id):
    sql = f'{update_the} {orders_table} SET switch = 1 WHERE order_id = %s'
    inserts = (order_id,)
    db.delete_record_from_db(sql,inserts)

def check_if_id_exists(action,table,column_id,option):
    id = 0
    sql = f'{action} {table} WHERE {column_id} = %s' 
    inserts = (option,)
    id = db.read_specific_record(sql,inserts)
    return id

def update_order_status(status,order):
    sql = f'{update_the} {orders_table} SET status_id = %s WHERE order_id = %s'
    inserts = (status,order)
    message = 'order status'    
    db.update_record_in_db(sql,inserts,message)
