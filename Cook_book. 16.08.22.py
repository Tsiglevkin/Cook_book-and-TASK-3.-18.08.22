from pprint import pprint

with open('food_list.txt', encoding='utf-8') as file:  # открываем файл, используя кодировку.
    cook_book = {}  # создаем пустой словарь.

    for line in file:  # построчно читаем открытый файл.
        recipe = []
        dish_name = file.readline().strip()  # читаем первую строку - название файла.
        num = int(file.readline().strip())  # читаем вторую строку - кол-во ингредиентов.
        for _ in range(num):  # проходимся циклом по остатку файла.
            ingr_list = file.readline().split(' | ')  # читаем строку и делаем из нее список по разделителю " | "
            recipe.append({'ingredient_name': ingr_list[0], # наполняем список ингредиентов recipe
                           'quantity': int(ingr_list[1]),
                           'measure': ingr_list[2].rstrip()})
        cook_book[dish_name] = recipe  # складываем все в финальный словарь.
        # Ключ - название блюда, значение - список ингредиентов.


def get_shop_list_by_dishes(dishes_list, person_count):
    """This function get a list (!) with one or more dish and quantity of guests and return quantity of ingredients"""
    final_dict = {}
    for dish in dishes_list:  # проходимся по введенному списку.
        if dish in cook_book:  # если блюдо в списке
            for el in cook_book[dish]:  # перебираем список конкретного блюда (обращение к значению словаря по ключу)
                # first variant
                middle_dict = {'quantity': el['quantity'] * person_count, 'measure': el['measure']}
                # создаем новый словарь с нужным количеством ингр.
                final_dict[el['ingredient_name']] = middle_dict  # Добавляем в финальный словарь.
                # second variant
                # final_dict[el['ingredient_name']] = {'quantity': el['quantity'] * person_count,
                #                                      'measure': el['measure']}
        else:
            print(f'Блюдо {dish} не в списке.')
    return final_dict

# Testing
# res = get_shop_list_by_dishes(['Омлет'], 2)
# print(res)
