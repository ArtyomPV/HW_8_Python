def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data


def save_line_to_file(line, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(line)


def savefile(data, filename):
    line = ''
    with open(filename, 'w', encoding='utf-8') as file:
        for i in data:
            for value in i:
                file.write(value)
                file.write(' ')
            file.write('\n')


def printinfo(data):
    for i in data:
        print(i)


def export(data):
    savefile(data, 'tel.txt')


def getdata(text):
    return input(text)


def find_max_index(data):
    max_index = 0
    for i in data:
        if max_index < int(i[0]):
            max_index = int(i[0])
    return str(max_index + 1)


def inputuser(data):
    # new_data = data
    line = find_max_index(data) + ' ' + getdata("Введите имя: ") + ' ' + getdata("Введите номер телефона: ") + '\n'
    save_line_to_file(line, 'tel.txt')


def delete_user(data):
    new_data = []
    user = getdata("Введите имя контакта: ")
    if is_has_contact(user, data):
        for i in data:
            if user != i[1]:
                new_data.append(i)
            else:
                print("Удален контакт: ")
                print(i)
    else:
        print("указанный контакт не найден")
    savefile(new_data, 'tel.txt')


def is_has_contact(user, data):
    for i in data:
        if user == i[1]:
            return True
    return False


def update_user(data):
    new_data = []
    user = getdata("Введите имя контакта: ")
    if is_has_contact(user, data):
        for i in data:
            if user == i[1]:
                i[2] = getdata("Введите номер телефона: ")
                line = i[0] + ' ' + i[1] + ' ' + i[2]
                print(line)
                # new_data.append(line)
            new_data.append(i)
    else:
        print("Контакт не найден")
    savefile(new_data, 'tel.txt')


def main():
    my_choice = -1
    data = readfile('tel.txt')
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - вывести инфо на экран')
        print('2 - произвести экспорт данных')
        print('3 - произвести ввод данных')
        print('4 - удаление пользователя')
        print('5 - обновить пользователя')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {1: printinfo, 2: export, 3: inputuser, 4: delete_user, 5: update_user}
        operations[my_choice](data)
        data = readfile('tel.txt')

    print('До свидания')


if __name__ == '__main__':
    main()
