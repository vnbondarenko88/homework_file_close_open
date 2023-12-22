# with open('recipes.txt', 'r', encoding='UTF-8') as f:
#     data = f.read()
#     print(repr(data))
import pprint
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
      
pprint.pprint(cook_book, width=100)


# тоже рабочее решение через список some_list

# cook_book = {}
# with open('recipes.txt', 'r', encoding='UTF-8') as f:
#     data = f.read().split('\n\n')
#     for food in data:
#       some_list = []
#       key = food.split('\n')[0]
#       ingridients = food.split('\n')[2:]
#       for ing in ingridients:
#         ing_1 = ing.split('|')
#         ingrigients_dict = {'ingredient_name':ing_1[0], 'quantity':ing_1[1], 'measure':ing_1[2]}
#         some_list.append(ingrigients_dict)    
#       cook_book[key] = some_list

# print(cook_book)