from src.db import db
from prettytable import PrettyTable
import os
from dotenv import load_dotenv

# Load environment variables

load_dotenv()
customers_table = os.environ.get("customers_table")
add_record_to = os.environ.get("add_record")
get_all_records_from = os.environ.get("get_all_records")
update_table = os.environ.get("update_table")
delete_from = os.environ.get('delete_from_table')


def customer_menu():
    customer_menu = '''
------------Customer List Menu----------------
|0:| Return to Main Menu                     |
|1:| View All Customers                      |
|2:| Add New Customer                        |
|3:| Update Custmoer Details                 |
|4:| Delete Customer                         | 
----------------------------------------------
'''
    print(customer_menu)

def view_menu():
    heading = ['#','Customer Name','Address','Phone Number']
    menu = 'CUSTOMER LIST'             
    sql = f'{get_all_records_from} {customers_table}' 
    db.read_record_from_db(sql,heading,menu)    


def add_customer(name, address,phone):
    sql = f'{add_record_to} {customers_table}(full_name,address,phone_number) VALUES (%s,%s,%s)'
    inserts = (name,address,phone)
    db.add_record_to_db(sql,inserts,name)
            

def update_customer(old,name,address,phone):
    
    if old != 0 and name != '' and address !='' and phone != '':

        sql = f'{update_table} {customers_table} SET full_name = %s, address = %s, phone_number = %s WHERE customer_id = %s'
        inserts = (name,address,phone,old) 
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and name != '': 

        sql = f'{update_table} {customers_table} SET full_name = %s WHERE customer_id = %s'
        inserts = (name,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and address != '': 
        
        sql = f'{update_table} {customers_table} SET address = %s WHERE customer_id = %s'
        inserts = (address,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and phone != '': 
        
        sql = f'{update_table} {customers_table} SET phone_number = %s WHERE customer_id = %s'
        inserts = (phone,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and name != '' and phone != '': 
        
        sql = f'{update_table} {customers_table} SET name = %s, phone_number = %s WHERE customer_id = %s'
        inserts = (name,phone,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and name != '' and address != '': 
        
        sql = f'{update_table} {customers_table} SET name = %s, address = %s WHERE customer_id = %s'
        inserts = (name,address,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and phone != '' and address != '': 
        
        sql = f'{update_table} {customers_table} SET phone_number = %s, address = %s WHERE customer_id = %s'
        inserts = (address,phone,old)
        db.update_record_in_db(sql,inserts,name)
    else:
        print('\n*******************************************')
        print('* ----CANNOT UPDATE DUE TO EMPTY INPUT---- *')
        print('*******************************************\n')

    
def delete_customer(customer):
    sql = f'{delete_from} {customers_table} WHERE customer_id = %s'
    inserts = (customer,)
    db.delete_record_from_db(sql,inserts)   
        

