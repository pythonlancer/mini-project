from src.db import db
from prettytable import PrettyTable
import os
from dotenv import load_dotenv

# Load environment variables

load_dotenv()
couriers_table = os.environ.get("couriers_table")
add_record_to = os.environ.get("add_record")
get_all_records_from = os.environ.get("get_all_records")
update_the = os.environ.get("update_table")
delete_from = os.environ.get('delete_from_table')


def courier_menu():
    courier_menu = '''
------------Customer List Menu----------------
|0:| Return to Main Menu                     |
|1:| View All Couriers                       |
|2:| Add New Courier                         |
|3:| Update Courier Details                  |
|4:| Delete Courier                          | 
----------------------------------------------
'''
    print(courier_menu)

def view_menu():
    heading = ['#','Courier','Delivery Mode','Phone Number']
    menu = 'COURIER LIST'             
    sql = f'{get_all_records_from} {couriers_table}' 
    db.read_courier_records_from_db(sql,heading,menu)    


def add_courier(courier,mode,phone):
    sql = f'{add_record_to} {couriers_table}(courier,delivery_id,phone_number) VALUES (%s,%s,%s)'
    inserts = (courier,mode,phone)
    db.add_record_to_db(sql,inserts,courier)
            

def update_courier(old,name,mode,phone):
    
    if old != 0 and name != '' and mode != 0 and phone != '':

        sql = f'{update_the} {couriers_table} SET courier = %s, delivery_id = %s, phone_number = %s WHERE courier_id = %s'
        inserts = (name,mode,phone,old) 
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and name != '': 

        sql = f'{update_the} {couriers_table} SET courier = %s WHERE courier_id = %s'
        inserts = (name,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and mode != 0: 
        
        sql = f'{update_the} {couriers_table} SET delivery_id = %s WHERE courier_id = %s'
        inserts = (mode,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and phone != '': 
        
        sql = f'{update_the} {couriers_table} SET phone_number = %s WHERE courier_id = %s'
        inserts = (phone,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and name != '' and phone != '': 
        
        sql = f'{update_the} {couriers_table} SET courier = %s, phone_number = %s WHERE courier_id = %s'
        inserts = (name,phone,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and name != '' and mode != '': 
        
        sql = f'{update_the} {couriers_table} SET courier = %s, delivery_id = %s WHERE courier_id = %s'
        inserts = (name,mode,old)
        db.update_record_in_db(sql,inserts,name)
    elif old != 0 and phone != '' and mode != '': 
        
        sql = f'{update_the} {couriers_table} SET phone_number = %s, delivery_id = %s WHERE courier_id = %s'
        inserts = (mode,phone,old)
        db.update_record_in_db(sql,inserts,name)
    else:
        print('\n*******************************************')
        print('* ----CANNOT UPDATE DUE TO EMPTY INPUT---- *')
        print('*******************************************\n')

    
def delete_courier(courier):
    sql = f'{delete_from} {couriers_table} WHERE courier_id = %s'
    inserts = (courier,)
    db.delete_record_from_db(sql,inserts)                   



