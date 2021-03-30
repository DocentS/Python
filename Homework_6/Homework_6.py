import copy
import pprint

# Дан список:
# [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3,9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, 
# '4+5.7j', '6']]

list_ = [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3, 9,
                                    4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]

# 1.1 Исключить из внутренних вложенних списков "мусор" - обекти у которих тип данних в 
# меньшенстве по сравнению с превалирующим типом.
type_counter = []
type_count = 0
type_name = ''
print('Список до очистки:')
print('\n'.join(map(str, list_)))

for item in list_:
    type_counter.clear()
    type_count = 0
    type_name = ''
    if isinstance(item, list):
        for i in item:
            type_counter.append(type(i))
        for i in set(type_counter):
            if type_name == '' or type_count < type_counter.count(i):
                type_name = i
                type_count = type_counter.count(i)
        i = 0
        while i < len(item):
            if type(item[i]) != type_name:
                del item[i]
            else:
                i += 1

print('Список после очистки:')
print('\n'.join(map(str, list_)))
print('\n')

# 1.2 Сделать три копии основного списка.
# 1.3 Приобразовать єти копии таким образом, чтоби каждая копия:
# не имела "мусора" (п.2.1);

# Comment: Чтобы не выполнять несколько раз одно и то же действие - достаточно использовать 
# то что выполнили в п.1.1

list_1 = copy.deepcopy(list_)
list_2 = copy.deepcopy(list_)
list_3 = copy.deepcopy(list_)
print('ID list_  :', id(list_))
print('ID list_1 :', id(list_1))
print('ID list_2 :',id(list_2))
print('ID list_3 :',id(list_3))
print('\n')

# не содержала вложености: внутренние списки должни бить расскрити;
# каждая из копий имела єлементи списка только определенного типа данних - [int], [float], [str].
list_tmp = list()
for item in list_1:
    for i in item:
        try:
            list_tmp = [*list_tmp, int(i)]
        except:
            print('Ошибка конвертации в int:',i)
list_1 = list_tmp

list_tmp = list()
for item in list_2:
    for i in item:
        try:
            list_tmp = [*list_tmp, float(i)]
        except:
            print('Ошибка конвертации в float:', i)
list_2 = list_tmp

list_tmp = list()
for item in list_3:
    for i in item:
        try:
            list_tmp = [*list_tmp, str(i)]
        except:
            print('Ошибка конвертации в str:', i)
list_3 = list_tmp

del(list_tmp)

print('\n')
print('list_1', list_1)
print('list_2', list_2)
print('list_3', list_3)
    
# 1.4 Решение Задачи 2 должно бить полностью автоматизировано - не иметь hardcode. Єто позволит при каких-либо модификациях исходного списка, 
# не меняю кода программи каждий раз получать привильное решение.

# 1.5 Задача 2 содержит такие єлементи Python програмирования:

# цикли (возможно вложеность циклов)
# проверка типа данних;
# определение длини списка;
# условний оператор, чтоби исключить "мусор";
# копирование списка;
# "спред" оператор;
# приведение типа данних к нужному;
# вивод результата в виде принта.
