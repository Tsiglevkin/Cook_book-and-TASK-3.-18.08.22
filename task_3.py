# from pprint import pprint
import os  # для возможности задать значение переменной name_1(2 or 3).
with open('1.txt', 'r', encoding='utf-8') as file_1:
    file_list_1 = file_1.readlines()  # делаю список
    # pprint(file_list_1)
    name_1 = os.path.basename(r'TASK 3. 18.08.22\1.txt')
    # print(name_1)

with open('2.txt', 'r', encoding='utf-8') as file_2:
    file_list_2 = file_2.readlines()
    name_2 = os.path.basename(r'TASK 3. 18.08.22\2.txt')

with open('3.txt', 'r', encoding='utf-8') as file_3:
    file_list_3 = file_3.readlines()
    name_3 = os.path.basename(r'TASK 3. 18.08.22\3.txt')

temp_dict = {name_1: file_list_1, name_2: file_list_2, name_3: file_list_3}
sorted_tuple = sorted(temp_dict.items(), key=lambda x: len(x[1]))  # создаю кортеж и сортирую при помощи лямбда
# по длине списка(количество строк).

sorted_dict = dict(sorted_tuple)  # создаю обратно словарь.

#
with open('result_text.txt', 'w', encoding='utf-8') as final_file:
    for key, value in sorted_dict.items():
        print(key)
        # final_file.write('\n')
        # final_file.writelines(sorted_dict[key])
        for i in range(len(value)):
            print(f'Строка {i + 1} файла {key}')
            final_file.write(f'Строка {i + 1} файла {key} - {value[i]}')
