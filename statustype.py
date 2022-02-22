from src.db import db
from prettytable import PrettyTable
import os
from dotenv import load_dotenv

# Load environment variables

load_dotenv()
status_table = os.environ.get("status_table")
add_record_to = os.environ.get("add_record")
get_all_records_from = os.environ.get("get_all_records")
update_table = os.environ.get("update_table")
delete_from = os.environ.get('delete_from_table')


def status_menu():
    status = '''
---------Order Status List Menu-------------
|0:| Return to Main Menu                   |
|1:| View All Statuses                     |
|2:| Add New Status                        |
|3:| Update Status                         |   
|4:| Delete Status                         |
--------------------------------------------
'''
    print(status)

def view_menu():
    heading = ['#','Status Type']
    status_type = 'STATUS TYPE MENU'             
    sql = f'{get_all_records_from} {status_table}' 
    db.read_record_from_db(sql,heading,status_type)    


def add_status(status):
    sql = f'{add_record_to} {status_table}(status) VALUES (%s)'
    inserts = (status)
    db.add_record_to_db(sql,inserts,status)
            

def update_status(old_status,new_status):
    
    if old_status != 0 and new_status != '':
        sql = f'{update_table} {status_table} SET status = %s WHERE status_id = %s'
        inserts = (new_status,old_status)
        db.update_record_in_db(sql,inserts,new_status)
    
    elif old_status != 0 and new_status == '' or new_status ==' ': 
        print('\n*******************************************')
        print('* ----CANNOT ENTER BLANK NEW STATUS---- *')
        print('*******************************************\n')
    else:
        print('\n*******************************************')
        print('* ----CANNOT UPDATE DUE TO BLANK INPUTS---- *')
        print('*******************************************\n')

    
def delete_status(status):
    sql = f'{delete_from} {status_table} WHERE status_id = %s'
    inserts = (status,)
    db.delete_record_from_db(sql,inserts)   