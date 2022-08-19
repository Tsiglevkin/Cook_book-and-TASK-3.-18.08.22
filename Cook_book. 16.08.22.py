from pprint import pprint

with open('food_list.txt', encoding='utf-8') as file:
    cook_book = {}

    for line in file:
        recipe = []
        dish_name = file.readline().strip()
        num = int(file.readline().strip())
        for _ in range(num):
            ingr_list = file.readline().split(' | ')
            recipe.append({'ingredient_name': ingr_list[0],
                           'quantity': int(ingr_list[1]),
                           'measure': ingr_list[2].rstrip()})
        cook_book[dish_name] = recipe


def get_shop_list_by_dishes(dishes_list, person_count):
    final_dict = {}
    for dish in dishes_list:
        if dish in cook_book:
            for el in cook_book[dish]:
                # first variant
                middle_dict = {'quantity': el['quantity'] * person_count, 'measure': el['measure']}
                final_dict[el['ingredient_name']] = middle_dict
                # second variant
                # final_dict[el['ingredient_name']] = {'quantity': el['quantity'] * person_count,
                #                                      'measure': el['measure']}
        else:
            print(f'Блюдо {dish} не в списке.')
    return final_dict

# два задания из 3 готовы. Осталось только прочитать файлы и расположить их в нужной последовательности.

