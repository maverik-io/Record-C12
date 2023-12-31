import csv 

def display():
    with open('Employee.csv','r') as f:
        data = csv.reader(f)
        for i in data:
            print(f'{i[0]}: {i[1]}, {i[2]}')

def create():
    def create_for(f):
        data = []
        while True:
            data.append([input('NAME: '),input('DEPARTMENT: '),input('SALARY: ')])
            if input('Continue? (y/n): ') == 'n':break
        csv.writer(f).writerows(data)
    try:
        f = open('Employee.csv','r')
        f.close()
        confirm = True if input('ARE YOU SURE YOU WANT TO OVERWRITE? (y/n): ') == 'y' else False
        if confirm:
            f = open('Employee.csv','w')
            create_for(f)
            f.close()
        
    except FileNotFoundError:
        f = open('Employee.csv','w')
        create_for(f)
        f.close()

while True:
    print('''
    1. CREATE
    2. DISPLAY
    3. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        create()
    elif ch == 2:
        display()
    elif ch == 3:
        break