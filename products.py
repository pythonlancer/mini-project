def cafe_menu():
    cafe_menu = '''-------------------Product Menu----------------
0: Return to Main Menu
1: View Tea Menu
2: Add New Tea
3: Update Tea Menu
4: Delete Tea Item
---------------------------------------------'''
    print(cafe_menu)

def view_menu():
    menu_number = 1
    print("------------Tea Cafe Menu--------------")  
    try:
        with open('data/products.txt','r') as products:
            lines = products.readlines()
                
        for line in lines:
            line = line.split(',')
            product = line[0]
            price = line[1]
            price = price.replace('\n','')
            
            print(f'{menu_number}. {product} - £{price}')
            menu_number+=1                
    except Exception as e:
        print('Failed to open products.txt, this is the error: ', e)


def add_product(product, price):    
    try:
        with open('data/products.txt','a') as product_list:
            product_list.write(product+', '+price+'\n')                
    except Exception as e:
        print('Failed to write to products.txt: ', e)    
    view_menu()
    print("--------------------------------------------------\n")
    print(f'{product} was added to the Tea Menu')
 

def update_product(old_product,new_product):
    new_product = new_product + '\n'
    try:
        with open('data/products.txt','r') as product_list:
            list_of_lines = product_list.readlines()    
            for line in list_of_lines:
                if old_product in line:
                    index = list_of_lines.index(line)
                    old_product = list_of_lines[index]
                    list_of_lines[index] = new_product
                    try:
                        with open("data/products.txt", "w") as update_product:
                            update_product.writelines(list_of_lines)       
                        
                    except Exception as e:
                        print('Failed to write(update) to products.txt: ') 
                    else:
                        view_menu()       
                        print("--------------------------------------------------\n")
                        old_product = old_product.replace('\n', '')
                        print(f'{old_product} was changed to the {new_product}')
                        break
            else:
                print(f"Sorry update failed, we dont have {old_product} in our database")

    except Exception as e:
        print('Failed to read products.txt: ', e)    
    


def delete_product(product):
    
    try:
        with open('data/products.txt','r') as product_list:
            list_of_lines = product_list.readlines()    
            for line in list_of_lines:
                if product in line:
                    index = list_of_lines.index(line)
                    print(list_of_lines[index])
                    del list_of_lines[index]     
                    try:
                        with open("data/products.txt", "w") as delete_product:
                            delete_product.writelines(list_of_lines)       
                    
                    except Exception as e:
                        print('Failed to write(delete) to products.txt: ')  
                    else:
                        view_menu()
                        print("--------------------------------------------------\n")
                        print(f'{product} was deleted from the Tea Menu')
                        break       
            else:
                print(f"Sorry delete failed, we dont have {product} in our database")
                                          
    except Exception as e:
        print('Failed to read products.txt: ', e)    
        

def get_product(product_id):
    try:
        with open('data/products.txt','r') as products:
            lines = products.readlines()
                
        for line in lines:
            if lines.index(line) == product_id:
                return line            
                            
    except Exception as e:
        print('Failed to open products.txt, this is the error: ', e)

#print(get_product(0))