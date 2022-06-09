from cgitb import text


def exit(text):
    while True:
        menu=Number(text)
        if menu==1:
            return True
        elif menu==2:
            return False


def Number(string = 'Enter the number: '):
    while True:
        number = input(string)
        if number.isdigit():
            return int(number)

def ad_human():
    global path
    path=r'sem_8\bd\fio.txt'
    a=True
    text='\nВыберите действие: \n1-Добавить человека \n2-Выйти\n '
    while a:
        with open(path, 'a') as data:
            data.write(f"'Name': {(input('Имя: ')).capitalize()} 'SurName': {(input('Фамилия: ')).capitalize()} 'Position': {(input('Должность: ')).capitalize()} 'Salary': {(input('Зарплата: ')).capitalize()} \n")
        a=exit(text)
#ad_human()

def user_input(string = 'Enter' ):
        enter = (input(string)).capitalize()
        if isinstance(enter,str):
            return enter
        

def search(string='text'):
     
    if user_input(text) in string.split():
        return " ".join(string)
    elif string.split().count(user_input(text))==0:
        return 'Не найдено'
        

def search_human():
    text=('\nВыбирите действие: \n1-Ввести запрос для поиска \n2-Выйти\n')
    path=r'sem_8\bd\fio.txt'
    b=True
    while b:
        with open(path,'r') as data:
            for line in data:
                if line==search(line):
                    print(line)
        b=exit(text)    


search_human()


