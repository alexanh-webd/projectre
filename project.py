from datetime import date
from datetime import datetime
import math

def menu():
    print('You may select one of the following:')
    print('1) List available cars')
    print('2) Rent a car')
    print('3) Return a car')
    print('4) Count the money')
    print('0) Exit')

def choice():
    try:
        choice = int(input('What is your selection?\n'))
        return choice
    except ValueError:
        return None
        
def remaining_car():
    file1 = open("vehicles.txt","r")
    file2 = open("rentedVehicles.txt","r")
    line1 = file1.readlines()
    line2 = file2.readlines()
    data1 = []
    data2 = []

    for i in line1:
        a = i.strip().split(",")
        data1.append(a)

    for i in line2:
        b = i.strip().split(",")
        data2.append(b)
    rented = []

    for e in range(len(data2)):
        rented.append(data2[e][0])
    data3 = []
    for line in data1:
        for el in rented:
            if el == line[0]:
                data3.append(line)
    data4 = []
    for i in data1:
        if i not in data3:
            data4.append(i)
    print('The following cars are available:')
    for r in range(len(data4)):
        print(f"* Reg.nr: {data4[r][0]}, Model: {data4[r][1]}, Price per day: {data4[r][2]}")
        p = data4[r][3:]
        if len(p) == 1:
            print(f"Properties: {p[0]}")
        elif len(p) == 2:
            print(f"Properties: {p[0]}, {p[1]}" )
        elif len(p) == 3:
            print(f"Properties: {p[0]}, {p[1]}, {p[2]}")
        elif len(p) == 4:
            print(f"Properties: {p[0]}, {p[1]}, {p[2]}, {p[3]}")
        elif len(p) == 5:
            print(f"Properties: {p[0]}, {p[1]}, {p[2]}, {p[3]}, {p[4]}")
    file1.close()
    file2.close()
def validate(day_str):
    try:
        day_obj = datetime.strptime(day_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

email_character_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g',
                            'h', 'j', 'k', 'l',
                            'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I',
                            'O', 'P', 'A', 'S',
                            'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '@',
                            '.']
def str_check(e):
    for char in e:
        a4 = e.find('@')
        b4 = e.rfind('.')
        if (char in email_character_list) and 0<a4<b4:
            return True
    else:
        return False
def choice3():
    car = input('Enter the register number:\n')
    fileA = open("vehicles.txt", "r")
    fileB = open("rentedVehicles.txt", "r")
    lineA = fileA.readlines()
    lineB = fileB.readlines()
    rented = []
    all_car = []
    for i1 in lineA:
        b1 = i1.strip().split(",")
        all_car.append(b1[0])
    for i2 in lineB:
        b2 = i2.strip().split(",")
        rented.append(b2[0])
    if car not in all_car:
        print(f"{car} does not exist")
    elif car not in rented and car in all_car:
        print(f"{car} is not rented")
    elif car in rented:
        time = []
        name_car = []
        cost_per_day = []
        for i4 in lineA:
            b4 = i4.strip().split(',')
            if b4[0] == car:
                cost_per_day.append(b4[2])
        for i3 in lineB:
            b3 = i3.strip().split(',')
            if b3[0] == car:
                time.append(b3[2])
        time_str = time[0]
        time_obj = datetime.strptime(time_str,'%d/%m/%Y %H:%M')
        today = datetime.now()
        today_str = today.strftime('%d/%m/%Y %H:%M')
        diff = today - time_obj
        c = diff.total_seconds()
        days = c/60/60/24
        d = math.ceil(days)
        cost = math.floor((int(d)*float(cost_per_day[0]))*100)/100
        cost = str(cost) + "0"
        print(f"The rent lasted {d} days and the cost is {cost} euros")
        fileD = open("transActions.txt","a")
        trans_data = []
        for i25 in lineB:
            b25 = i25.strip().split(",")
            trans_data.append(b25)
        trans_name = []
        cus_id = []
        start_rent = []
        for i67 in trans_data:
            trans_name.append(i67[0])
            cus_id.append(i67[1])
            start_rent.append(i67[2])
        for i9 in range(len(trans_name)):
            if str(car) == str(trans_name[i9]):
                d = trans_name[i9]+','+cus_id[i9]+','+start_rent[i9]+','+today_str+','+str(d)+','+str(cost)+'\n'
                fileD.write(d)      #str(cost_per_day[0])

        new_data = []
        for i3 in lineB:
            b3 = i3.strip().split(',')
            new_data.append(b3)
        for i in new_data:
            for el in i:
                if el == car:
                    new_data.remove(i)
        name = []
        birth = []
        start = []
        for i in new_data:
            name.append(i[0])
            birth.append(i[1])
            start.append(i[2])
        fileC = open("rentedVehicles.txt",'w')
        for i in range(len(name)):
            if i == (len(name)-1):
                c =name[i]+','+birth[i]+','+start[i]
            else:
                c =name[i]+','+birth[i]+','+start[i]+'\n'
            fileC.write(c)
        fileC.close()
        fileD.close()
def choice4():
    file = open('transActions.txt','r')
    line = file.readlines()
    data = []
    money = []
    for i in line:
        a = i.strip().split(',')
        data.append(a)
    for line in data:
        money.append(line[5])
    m = 0
    for i in money:
        m = m + float(i)
    print(f"The total amount of money is {m}0 euros")
    print()
    file.close()


while True:
    print()
    menu()
    start = choice()
    if start == None:
        print('Invalid choice, please enter an integer!')
    elif start > 4 or start < 0:
        print('Invalid choice, please try agian!')
    elif start == 0:
        print('Bye!')
        break
    elif start == 1:
        remaining_car()
    elif start == 2:
        already_rented = []
        car_rented = []
        car = input('Enter the register number:\n')
        fileA = open("vehicles.txt", "r")
        fileB = open("rentedVehicles.txt", "r")
        lineA = fileA.readlines()
        lineB = fileB.readlines()
        rented = []
        all_car = []
        for i1 in lineA:
            b1 = i1.strip().split(",")
            all_car.append(b1[0])
        for i2 in lineB:
            b2 = i2.strip().split(",")
            rented.append(b2[0])
        if car in rented:
            print(f"{car} already rented")
        elif car not in all_car:
            print(f"{car} does not exist")
        else:
            b = input('Please enter your birthday in the form DD/MM/YYYY:\n')
            valid = validate(b)
            while not valid:
                print('There is not such date. Try agian!')
                b = input('Please enter your birthday in the form DD/MM/YYYY:\n')
                valid = validate(b)
            b_obj = datetime.strptime(b, '%d/%m/%Y')
            today = datetime.now()
            diff = today - b_obj
            a12 = diff.days
            if a12 < 6570:
                print('You are too young to rent a car, sorry!')
            elif a12 > 23725:
                print('You are too old to rent a car, sorry!')
            else:
                try:
                    file1 = open('customers.txt','r')
                    line1 = file1.readline().strip()
                    data1 = []
                    n1 = []
                    customer_id= []
                    while line1 != '':
                        data = line1.split(',')
                        data1.append(data)
                        line1 = file1.readline().strip()
                        
                    for i in range(len(data1)):
                        if b == (data1[i][0]):
                            for data in data1[i][1:]:
                                already_rented.append(data)
                    to_day = datetime.now()
                    str_to_day = to_day.strftime("%d/%m/%Y %H:%M")
                    file5 = open('rentedVehicles.txt', 'a')
                    already_rented_info = []
                    already_rented_info.append(car+',')
                    already_rented_info.append(b+',')
                    already_rented_info.append(str_to_day)
                    file5.write('\r')
                    file5.writelines(already_rented_info)
                    file5.close()
                    file1.close()
                    print('Age OK')
                    print(f"Hello {already_rented[0]}")
                    print(f"You have rented the car {car}")
                except IndexError:
                    car_rented.append(car)
                    car_rented.append(str(b))
                    print('Names contain only letters and start with capital letters.')
                    c = input('Enter the first name of the customer:\n')
                    d = input('Enter the last name of the customer:\n')
                    character_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j',
                                  'k', 'l',
                                  'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                                  'A', 'S',
                                  'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
            
                    for i in range(len(c)):
                        if c[0] != c[0].upper() or c[i] not in character_list:
                            print('Names contain only letters and start with capital letters.')
                            c = input('Enter the first name of the customer:\n')
                            d = input('Enter the last name of the customer:\n')
                    for i34 in range(len(d)):
                        if d[0] != d[0].upper() or d[i34] not in character_list:
                            print('Names contain only letters and start with capital letters.')
                            c = input('Enter the first name of the customer:\n')
                            d = input('Enter the last name of the customer:\n')
                    else:
                        car_rented.append(c)
                        car_rented.append(d)
                        c8 = input('Give your email:\n')
                        d8 = str_check(c8)
                        while not d8:
                            print('Give a valid email address')
                            c8 = input('Give your email:\n')
                            d8 = str_check(c8)
                        car_rented.append(c8)
                        print(f"Hello {c}")
                        print(f"You have rented the car {car_rented[0]}")

                        real_car_rented = []
                        rented_info = []
                        to_day = datetime.now()
                        str_to_day = to_day.strftime("%d/%m/%Y %H:%M")
                        file4 = open('customers.txt', "a")
                        #file5 = open('rentedVehicles.txt', 'a')
                        for char in range(1, (len(car_rented) - 1)):
                            a90 = car_rented[char] + ','
                            real_car_rented.append(a90)
                        real_car_rented.append(car_rented[4])
                        file4.write('\r')
                        file4.writelines(real_car_rented)
                        for elements in range(0, 2):
                            b = car_rented[elements] + ','
                            rented_info.append(b)
                        rented_info.append(str_to_day)
                        #file5.write('\r')
                        #file5.writelines(rented_info)
                        file4.close()
                        car_rented = []

    elif start == 3:
        choice3()
    elif start == 4:
        choice4()
        
