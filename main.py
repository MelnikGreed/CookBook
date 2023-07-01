def read_recipes(file_name):
    cook_book = {}

    with open('text.txt', 'r', encoding='UTF-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients

    return cook_book
file_name = 'text.txt'
cook_book = read_recipes(file_name)
print(cook_book)

print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity
    return shop_list
dishes = ['Фахитос', 'Утка по-пекински']
person_count = 2
result = get_shop_list_by_dishes(dishes, person_count)
print(result)