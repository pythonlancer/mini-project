def courier_menu():
    courier_menu = '''-------------------Courier Menu----------------
0: Return to Main Menu
1: View Courier List
2: Add New Courier
3: Update Courier List
4: Delete Courier
5: Delievery Mode Menu
---------------------------------------------'''
    print(courier_menu)

def view_menu():
    menu_number = 1
    print("------------Courier List--------------")  
    try:
        with open('data/couriers.txt','r') as couriers:
            lines = couriers.readlines()
                
        for line in lines:
            line = line.split(',')
            courier = line[0]
            mode = line[1]
            mode = mode.replace('\n','')
            
            print(f'{menu_number}. {courier} - By:[{mode}]')        
            menu_number += 1                
    except Exception as e:
        print('Failed to open couriers.txt, this is the error: ', e)


def add_courier(courier, mode):    
    try:
        with open('data/couriers.txt','a') as courier_list:
            courier_list.write(courier+', '+mode+'\n')                
    except Exception as e:
        print('Failed to write to couriers.txt: ', e)    
    view_menu()
    print("--------------------------------------------------\n")
    print(f'{courier} was added to the Courier List')
 

def update_courier(old_courier,new_courier):
    new_courier = new_courier + '\n'
    try:
        with open('data/couriers.txt','r') as courier_list:
            list_of_lines = courier_list.readlines()    
            for line in list_of_lines:
                if old_courier in line:
                    index = list_of_lines.index(line)
                    old_courier = list_of_lines[index]
                    list_of_lines[index] = new_courier
                    try:
                        with open("data/couriers.txt", "w") as update_courier:
                            update_courier.writelines(list_of_lines)       
                        
                    except Exception as e:
                        print('Failed to write(update) to couriers.txt: ') 
                    else:
                        view_menu()       
                        print("--------------------------------------------------\n")
                        old_courier = old_courier.replace('\n', '')
                        print(f'{old_courier} was changed to the {new_courier}')
                        break
            else:
                print(f"Sorry update failed, we dont have {old_courier} in our database")

    except Exception as e:
        print('Failed to read couriers.txt: ', e)    
    

def delete_courier(courier):
    
    try:
        with open('data/couriers.txt','r') as courier_list:
            list_of_lines = courier_list.readlines()    
            for line in list_of_lines:
                if courier in line:
                    index = list_of_lines.index(line)
                    print(list_of_lines[index])
                    del list_of_lines[index]     
                    try:
                        with open("data/couriers.txt", "w") as delete_courier:
                            delete_courier.writelines(list_of_lines)       
                    
                    except Exception as e:
                        print('Failed to write(delete) to couriers.txt: ')  
                    else:
                        view_menu()
                        print("--------------------------------------------------\n")
                        print(f'{courier} was deleted from the Courier List')
                        break       
            else:
                print(f"Sorry delete failed, we dont have {courier} in our database")
                                          
    except Exception as e:
        print('Failed to read couriers.txt: ', e)    
        
def delivery_menu():
    menu_number = 1
    print("------------Courier Delivery Menu--------------")  
    try:
        with open('data/delivery.txt','r') as modes:
            lines = modes.readlines()
                
        for line in lines:
            line = line.split(',')
            mode = line[0]
            cost = line[1]
            cost = cost.replace('\n','')
            
            print(f'{menu_number}. {mode} - £{cost}')        
            menu_number += 1                
    except Exception as e:
        print('Failed to open couriers.txt, this is the error: ', e)

def get_delivery_cost(delivery_mode):
    result = ''
    try:
        with open('data/delivery.txt','r') as modes:
            lines = modes.readlines()
                
        for line in lines:
            line = line.split(',')            
            mode = line[0]
            cost = line[1]
            cost = cost.replace('\n','')
            if mode == delivery_mode:
                return cost        

    except Exception as e:
        print('Failed to open couriers.txt, this is the error: ', e)
  
#mode = 'scooter' 
#print(get_delivery_cost(mode))

def get_courier(courier_id):
    try:
        with open('data/couriers.txt','r') as couriers:
            lines = couriers.readlines()
                
        for line in lines:
            if lines.index(line) == courier_id:
                return line           
                            
    except Exception as e:
        print('Failed to open couriers.txt, this is the error: ', e)

#print(get_courier(0))
