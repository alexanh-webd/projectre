from datetime import datetime
character_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j',
                'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

data_dict = []
rented = []
file = open('vehicles.txt','r')
file1 = open('rentedVehicles.txt','r')
data = file.readlines()
data1 = file1.readlines()
cr = []
cr1 = []
for i in data:
    cr.append(i.strip())
for l in data1:
    cr1.append(l.strip())
da = []
da1 = []
for e in cr:
    da.append(e.split(','))
for e1 in cr1:
    da1.append(e1.split(','))
key = ['Reg.nr','Model','Price']
key1 = ['Reg.nr', 'daterent', 'return']
for u in da:
    data_dict.append(dict(zip(key,u[0:3])))
for u1 in da1:
    rented.append(dict(zip(key1,u1)))
addi = []
for e in da:
    addi.append(e[3:])
index = 0
while index < len(addi):
    for data in data_dict:
        data['Properties'] = addi[index]
    index = index + 1
def choice1():
    print('Available cars:1')
    for e in range(len(data_dict)):
        print(f"Reg.nr: {data_dict[e]['Reg.nr']}, Model: {data_dict[e]['Model']}, Price per day: {data_dict[e]['Price']}")
        if len(data_dict[e]['Properties']) == 1:
            print(f"Properties: {data_dict[e]['Properties'][0]}")
        elif len(data_dict[e]['Properties']) == 2:
            print(f"Properties: {data_dict[e]['Properties'][0]}, {data_dict[e]['Properties'][1]}")
        elif len(data_dict[e]['Properties']) == 3:
            print(f"Properties: {data_dict[e]['Properties'][0]}, {data_dict[e]['Properties'][1]}, {data_dict[e]['Properties'][2]}")
        elif len(data_dict[e]['Properties']) == 4:
            print(f"Properties: {data_dict[e]['Properties'][0]}, {data_dict[e]['Properties'][1]}, {data_dict[e]['Properties'][2]}, {data_dict[e]['Properties'][3]}")
        elif len(data_dict[e]['Properties']) == 5:
            print(f"Properties: {data_dict[e]['Properties'][0]}, {data_dict[e]['Properties'][1]}, {data_dict[e]['Properties'][2]}, {data_dict[e]['Properties'][3]}, {data_dict[e]['Properties'][4]}")
def menu():
    print('You may select one of the following:')
    print('1) List available cars')
    print('2) Rent a car')
    print('3) Return a car')
    print('4) Count the money')
    print('0) Exit')    
def validate(date):
    try:
        date_obj = datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False
def validname(n):
    for char in n:
        if char not in character_list:
            return False
        else:
            return True
while True:
    menu()
    try:
        choice = int(input('What is your selection?\n'))
        if choice > 4 or choice < 0:
            print('Invalid choice, please try again!')
        elif choice == 0:
            print('Bye!')
            break
        elif choice == 1:
            choice1()
            print()
        elif choice == 2:
            name = input('Give the register number of the car you want to rent:\n')
            rent = []
            for car in rented:
                rent.append(car['Reg.nr'])
            avl_car = []
            for car in data_dict:
                avl_car.append(car['Reg.nr'])
            if name not in avl_car:
                print(f"{name} does not exist!")
                print()
            elif name in avl_car and name in rent:
                print(f"{name} is already rented.")
                print()
            else:
                birth = input('Enter your birthday in the format DD/MM/YYYY:\n')
                res = validate(birth)
                while res == False:
                    birth = input('Please enter a valid date:\n')
                    res = validate(birth)
                date_obj = datetime.strptime(birth,'%d/%m/%Y')
                today = datetime.now()
                diff = today-date_obj
                if diff.days < 18*365:
                    print('You are too young to rent a car.')
                elif diff.days > 65*365:
                    print('You are too old to rent a car.')
                else:
                    firstname = input('Enter your first name:\n')
                    lastname = input('Enter your last name:\n')
                    while validname(firstname) == False:
                        print('Please enter a valid name')
                        firstname = input('Enter your first name:\n')
                    while validname(lastname) == False:
                        print('Please enter a valid name')
                        lastname = input('Enter your last name:\n')
                    while firstname[0] != firstname[0].upper() or lastname[0] != lastname[0].upper():
                        print('Names contains only letters and start with capital letters')
                        firstname = input('Enter your first name:\n')
                        lastname = input('Enter your last name:\n')
    except ValueError:
        print('Please enter a number!')
