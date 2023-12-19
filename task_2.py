cook_book = {}
with open('recipes.txt', 'r', encoding='UTF-8') as f:
  data = f.read().split('\n\n')
  for food in data:
    key = food.split('\n')[0]
    ingridients = food.split('\n')[2:]
    for ing in ingridients:
      ing_1 = ing.split('|')
      ingrigients_dict = {'ingredient_name':ing_1[0], 'quantity':ing_1[1], 'measure':ing_1[2]}
      if key in cook_book:
        cook_book[key].append(ingrigients_dict)
      else:
        cook_book[key] = [ingrigients_dict]


def get_shop_list_by_dishes(dishes, person_count):
    new_book = {}
    for dish in dishes:
    # print(dish)
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                # print(ingredient)
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                if ingredient_name not in new_book:
                    new_book[ingredient_name] = {
                    "measure": measure,
                    "quantity": quantity
                    }
                else:
                    new_book[ingredient_name]['quantity'] += quantity

    return new_book
print(get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 4))