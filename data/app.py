main_menu = '''-------------------main menu ----------------
0:exit
1:food menu
2:add product
3:update/delete product
4:orders 
---------------------------------------------'''

print(main_menu)
menu = ["Coffee", "Bread", "Biscuits", "Tea", "English Breakfast"] 

def add_product(product):
    menu.append(product)
    print(f'{product} was added to the Menu')

def update_product(old,new):
    menu[old] = new
    print(f'{old} was updated to {new}')

def delete_product(product):
    menu.remove(product)
    print(f'{product} was removed from the Menu')

    
def start_app(app_open):
    menu_number = 1  
    type_of_input = type(app_open)  
    if app_open == 0:
        print("App successfully terminated. Thank you for using Cafe App 3.0")
    elif app_open == 1:     
        print("------------Coffee Cafe Menu--------------")  
        for item in menu:
            
            print(f"{menu_number}: {item}") 
            
            menu_number+=1
        print("------------------------------------------") 
    elif app_open == 2:
        new_item = input('Enter the new product name: ')   
        add_product(new_item)
        print("\n------------New Coffee Cafe Menu--------------")  
        for item in menu:
            
            print(f"{menu_number}: {item}") 
            
            menu_number+=1
        print("--------------------------------------------------")
    elif app_open == 3:
        modify_menu = '''
        -------------------------
        0:delete product
        1:update product
        2:main menu
        -------------------------'''
        print(modify_menu)
        choice = int(input('What would you like to do?: '))  
        if choice == 0:
            item_to_delete = input('Enter the product to delete: ')   
            delete_product(item_to_delete)
            print("\n------------Updated Coffee Cafe Menu--------------")  
            for item in menu:
                
                print(f"{menu_number}: {item}") 
                
                menu_number+=1
            print("--------------------------------------------------")
        
        elif choice == 1:
            item_to_update = input('Enter the product to update: ')
            update = input("Enter it's new name: ") 
            index = menu.index(item_to_update)  
            update_product(index, update)
            print("\n------------Updated Coffee Cafe Menu--------------")  
            for item in menu:
                
                print(f"{menu_number}: {item}") 
                
                menu_number+=1
            print("--------------------------------------------------")  
    else:
        print("Program terminated,Command not recognized")
    
        
app_open = int(input("Welcome to Coffee Cafe App, what would you like to do: "))    
start_app(app_open)
           