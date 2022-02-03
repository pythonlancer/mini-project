menu_items = '''---------- Calculator Menu ----------
0: Exit
1: Add
2: Subtract
3: Divide
4: Multiply
5: Perform Power of
6: Find the root of numbers
7: Find the area of objects
-------------------------------------'''
def add_numbers(args):
    
    # print(args)
    total = 0
    for number in args:
        total+=number
        text = f'{total} + {number}'
    print(total)

def subtract_numbers(number1,number2):
    # print(args)
    total = 0
    for number in args:
        total+=number
    print(f'{number1} - {number2} =',number1-number2)

def divide_numbers():
    pass

def multiply_numbers():
    pass

def power_numbers():
    pass

def root_numbers():
    pass

def area_of_objects():
    pass

def calc_menu():
    print(menu_items)
    # return ''

def check_type(number):
    def_number = 1
    a_number = type(def_number)
    if type(number) == a_number:
        return 1
    else:
        return 0

def basic_calculator():
    calc_menu()
    user_choice = int(input('What would like to do: '))
    check_user_choice = check_type(user_choice)
    if user_choice == 0 and check_user_choice == 1:
        print('Thank you using my Basic Calculator')
    elif user_choice == 1 and check_user_choice == 1:
        qn = int(input('How many numbers do you want to add?: '))
        count = 1
        numbers_to_add = []
        while count <= qn:
            number = int(input(f'Entry {count}:=> '))
            numbers_to_add.append(number)
            count += 1

        add_numbers(numbers_to_add)


    elif user_choice == 2 and check_user_choice == 1:
        number1 = int(input('Entry 1:=> '))
        number2 = int(input('Entry 2:=> '))

        add_numbers(number1, number2)
    elif user_choice == 3 and check_user_choice == 1:
        pass
    elif user_choice == 4 and check_user_choice == 1:
        pass
    elif user_choice == 5 and check_user_choice == 1:
        pass
    elif user_choice == 6 and check_user_choice == 1:
        pass
    elif user_choice == 7 and check_user_choice == 1:
        pass
    else:
        print('What you want to do is outof range/scope')

basic_calculator()
