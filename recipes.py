def recipes(txt_file: str):
    with open(txt_file, encoding = 'utf-8') as file:
        cook_book = {}
        for line in file:
            if ''.join(''.join(line.split('-')).split()).isalpha():         #очень мне это не нравится, но что-то по-другому не придумалось....
                key = line.strip()
                cook_book[key] = []
            elif line.strip().isdigit():
                continue
            elif line.isspace():
                continue    
            else:
                s = line.strip().split('|')
                cook_book[key].append({'ingredient_name': s[0].strip(), 'quantity': s[1].strip(), 'measure': s[2].strip()})
                
        return(cook_book)   

from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipes('recipes.txt') 
    cook_dish = {}
    for dish in dishes:
        if dish in cook_book:
            for id, ingr in enumerate(cook_book[dish]):
                if cook_book[dish][id]['ingredient_name'] in cook_dish:
                    cook_dish[cook_book[dish][id]['ingredient_name']]['quantity'] += int(cook_book[dish][id]['quantity']) * person_count           
                else:
                    cook_dish[cook_book[dish][id]['ingredient_name']] = {}
                    cook_dish[cook_book[dish][id]['ingredient_name']]['measure'] = cook_book[dish][id]['measure']
                    cook_dish[cook_book[dish][id]['ingredient_name']]['quantity'] = int(cook_book[dish][id]['quantity']) * person_count
        else:
            print('Такого блюда в словаре нет!')  
            return          
            
    pprint(cook_dish)

# get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)    