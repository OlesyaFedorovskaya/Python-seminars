# Задача №49.
# Создать телефонный справочник с возможностью импорта 
# и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, 
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик 
# для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. 
# Ваша программа не должна быть линейной

import os, sys

def main_import_contacts(): # открывается файл
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'r', encoding='utf-8') as data:
    # with open('phonebook.txt', 'r' ,encoding='utf-8') as data:
        s = data.readlines() # список куда мы записали выгруженные контакты
        for i in range(len(s)): # пробегаемся по всем элементам
            phonebook[i] = s[i].split() # разбиваем на подсписок, добавляем в наш словарь
        # print(phonebook)

def import_contacts(some_string):
    found_contacts = list()
    for i in phonebook:
        if some_string in phonebook[i]:
            found_contacts.append(phonebook[i])
    return found_contacts

def export_contacts(new_line):
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'a+',encoding='utf-8') as data:
    # with open('phonebook.txt', 'a+' ,encoding='utf-8') as data:
        # s = ' '.join(new_line)
        data.writelines(' '.join(new_line)+'\n')

def input_contact():
    # new_contact = list()
    # new_contact.append(input('Фамилия: '))
    new_contact = [input('Фамилия: ')]
    new_contact.append(input('Имя: '))
    new_contact.append(input('Отчество: '))
    new_contact.append(input('Номер телефона: '))
    export_contacts(new_contact)

def found_contact():
    s = import_contacts(input('Введите значение для поиска: '))
    print(*s)

def change_contact():
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'r', encoding='utf-8') as data:
        some_elem = input('Введите данные контакта: ')
        lines = data.readlines()
    with open(os.path.join(sys.path[0],'phonebook.tdxt'), 'w', encoding='utf-8') as data:
        for line in lines:
            if some_elem in line:
                line = line.split()
                for part in line:
                    new_note = part.replace(part, input(f'Введите новую информацию {part} => '))
                    data.writelines(new_note + ' ')
                    print('Готово')
            else:
                data.write(str(line))
        

def delete_contact():
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'r', encoding='utf-8') as data:
        some_elem = input('Введите данные контакта: ')
        lines = data.readlines()
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'w', encoding='utf-8') as data:
            for line in lines:
                if some_elem in line:
                    print('Удалено')  
                else:
                    print(line)
                    data.write(line)
        
                

def user_interface():
    main_import_contacts() # запускаем импорт всех контактов в словарь "телефонная книга"
    print('Phonebook\nЧто вы хотите?\n'
            '1 - добавить контакт\n'
            '2 - найти контакт\n'
            '3 - print whole book\n'
            '4 - изменить данные контакта\n'
            '5 - удалить контакт\n'
            'any other input - конец программы')
    user_input = input('Ваш выбор: ')
    while user_input in ('1','2','3','4','5'):
        if user_input == '1':
            input_contact()
        elif user_input == '2':
            found_contact()
        elif user_input == '3':
            print()
            for i in phonebook:
                print(*phonebook[i])
        elif user_input == '4':
            change_contact()
        elif user_input == '5':
            delete_contact()
        user_input = input('\nВаш выбор: ')

    print('До свидания')

phonebook = dict() # создаем словарь "телефонная книжка"
user_interface() # запускаем функцию user_interface
