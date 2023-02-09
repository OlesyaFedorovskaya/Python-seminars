# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

import os
os.system('cls')

# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# my_dict1 = set()

# for i in my_dict:
#     for value in i.values():
#         my_dict1.add(value)
# print(*my_dict1)

#####

def unic_values(lst): 
    unic_values = set() # создали пустое множество
    for dict in lst:
        for value in dict.values(): # перебираем 
            unic_values.add(value)  # добавляем значение в пустое множество
    return unic_values

input_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

print(unic_values(input_list))

#####

# list_of_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#                 {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# list_of_values = {tuple(i.values())[0].strip() for i in list_of_dict}
# print(list_of_values)

#####

# input_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}

# unic_values = set() # создали пустое множество
# for d in input_list:
#     for value in d.values(): # перебираем 
#         unic_values.add(value.strip())  # добавляем значение в пустое множество

# print(unic_values)

#####

# input_list = [{"V": " S001"}, {"V": " S002"}, {"VI": "S001 "},
# {"VI": "S005 "}, {"VII": " S005"}, {" V ":"S009"}, {" VIII":"S007 "}]

# unic_values = set()
# for d in input_list:
# print('d это - ',d)
# print('d.values это -', d.values())
# unic_values.add(tuple(d.values())[0].strip())

# print(unic_values)

#####

# input_list = [{"V": " S001"}, {"V": " S002"}, {"VI": "S001 "},
# {"VI": "S005 "}, {"VII": " S005"}, {" V ":"S009"}, {" VIII":"S007 "}]

# unic_values = set()
# for d in input_list:
# print('d это - ',d)
# print('d.values это -', d.values())
# elem = d.values()
# elem = tuple(elem)
# elem = elem[0]
# elem = elem.strip()
# unic_values.add(elem)

# print(unic_values)