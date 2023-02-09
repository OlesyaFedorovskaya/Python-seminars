# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {"V":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# my_dict1 = set()

# for i in my_dict:
#     for value in i.values():
#         my_dict1.add(value)
# print(*my_dict1)

def unic_values(lst):
    unic_values = set()
    for dict in lst:
        for value in dict.values():
            unic_values.add(value)
    return unic_values

input_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

print(unic_values(input_list))