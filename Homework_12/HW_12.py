# Задан файл HW.json
# Обработать исходний файл таким образом, чтоби получить получить результирующий 
# файл по подобию НW_result.json. Весь код оформить в виде функций.

# Отчет содержит файли:
# HW.json,
# *.py,
# измененний, в соответствии с исходними данними, НW_result.json.

# В задачи Ви примените: python функции, менеджер задач для для 
# сериализации и десериализации данних, работа с json обектом, 
# цикл for, условний оператор проверки типа данних, метод append для списка.

import json

def GetFullName(dict_):
    full_name = ''
    for key_, value_ in dict_.items():
        if key_ in ('firstName', 'lastName'):
            if len(full_name) > 0:
                full_name += ' '
            full_name += value_
    return(full_name)

with open('./HW.json', encoding='UTF-8') as file:
    data = json.load(file)
 
data_new = {}
data_result = {}
for data_key, data_value in data.items():
    # print(data_key)
    
    for item in data_value:
        # Тут интересно: data_value - list, a 'i' - сразу распознаёт как dict
        dict_types = {}    
        for key, value in item.items():

            if isinstance(value, bool):
                list_ = dict_types.pop('bool', [])
                list_.append(key)
                dict_types.update({'bool': list_})
            
            elif isinstance(value, int):
                list_ = dict_types.pop('int',[])
                list_.append(key)
                dict_types.update({'int': list_})
            
            elif isinstance(value, float):
                list_ = dict_types.pop('float', [])
                list_.append(key)
                dict_types.update({'float': list_})
                
            elif isinstance(value, str):
                list_ = dict_types.pop('string', [])
                list_.append(key)
                dict_types.update({'string': list_})
                            
            elif type(value) == None:
                list_ = dict_types.pop('none_type', [])
                list_.append(key)
                dict_types.update({'none_type': list_})
            
        FullName = GetFullName(item)
        data_new.update({FullName: dict_types})
        data_result.update({data_key: data_new})
        print(data_result)
        
with open('./HW_result.json', 'w', encoding='UTF-8') as file:
    json.dump(data_result, file)
