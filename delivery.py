from src.db import db
from prettytable import PrettyTable
import os
from dotenv import load_dotenv

# Load environment variables

load_dotenv()
delivery_table = os.environ.get("delivery_table")
add_record_to = os.environ.get("add_record")
get_all_records_from = os.environ.get("get_all_records")
update_table = os.environ.get("update_table")
delete_from = os.environ.get('delete_from_table')


def mode_menu():
    delivery_mode_menu = '''
---------Delivery Mode Menu-----------------
|0:| Return to Main Menu                   |
|1:| View All Delivery Modes               |
|2:| Add New Delivery Mode                 |
|3:| Update Delivery Mode                  |   
|4:| Delete Delivery Mode                  |
--------------------------------------------
'''
    print(delivery_mode_menu)

def view_menu():
    heading = ['#','Delivery Mode','Cost(£)']
    delivery_mode = 'DELIVERY MODE MENU'             
    sql = f'{get_all_records_from} {delivery_table}' 
    db.read_record_from_db(sql,heading,delivery_mode)    


def add_delivery_mode(mode, price):
    sql = f'{add_record_to} {delivery_table}(mode,cost) VALUES (%s,%s)'
    inserts = (mode,price)
    db.add_record_to_db(sql,inserts,mode)
            

def update_delivery_mode(old_mode,new_mode,price):
    
    if old_mode != 0 and new_mode != '' and price !='':
        sql = f'{update_table} {delivery_table} SET mode = %s, cost = %s WHERE delivery_id = %s'
        inserts = (new_mode,price,old_mode)
        db.update_record_in_db(sql,inserts,new_mode)
    elif old_mode != 0 and new_mode != '': 
        sql = f'{update_table} {delivery_table} SET mode = %s WHERE delivery_id = %s'
        inserts = (new_mode,old_mode)
        db.update_record_in_db(sql,inserts,new_mode)
    elif old_mode != 0 and price != '': 
        sql = f'{update_table} {delivery_table} SET cost = %s WHERE delivery_id = %s'
        inserts = (price,old_mode)
        db.update_record_in_db(sql,inserts,new_mode)
    else:
        print('\n*******************************************')
        print('* ----CANNOT UPDATE DUE TO EMPTY INPUT---- *')
        print('*******************************************\n')

    
def delete_delivery_mode(mode):
    sql = f'{delete_from} {delivery_table} WHERE delivery_id = %s'
    inserts = (mode,)
    db.delete_record_from_db(sql,inserts)   