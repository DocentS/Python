import random

# 1. Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами значения 
# первого и последнего элемент объекта. Удалите второй элемент. Добавьте в конец ключ 
# «new_key» со значением «new_value». Выведите на печать итоговый словарь. 
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

dict_ = {a: a ** 2 for a in range(5)}
print('Начальный словарь:', dict_)
print('Адрес в пямяти:', id(dict_))
# Comment: "Поменяйте местами значения первого и последнего элемент объекта." 
# - Словари не упорядочнены, нужно знать имя ключа
dict_[0], dict_[4] = dict_[4], dict_[0]
dict_.pop(1)
dict_.update({'new_key': 'new_value'})
print('Изменённый словарь:', dict_)
print('Адрес в пямяти:', id(dict_))
print('\n')

# 2. Как получить значение по ключу "marks" словаря 
# student = {"name": "Emma", "class": 9, "marks": 75}
# Comment: с помощью метода get()
# print(student.get("marks"))

# 3. Что выведет этот код? 
# p = {"name": "Mike", "salary": 8000} 
# print(p.get("age"))
# Comment: вернёт - None

# 4. Как получить "d":sample = {"1":["a","b"], "2":["c","d"]}.
sample = {"1": ["a", "b"], "2": ["c", "d"]}
list_ = sample.get("2")
print(list_[1])
print(list_[-1])
print('\n')

# 5. Дан список стран и городов каждой страны. Затем даны названия городов. 
# Для каждого города укажите, в какой стране он находится. 
# Дано: list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", 
#   "Германия-Мюнхен"], list_2 = ["Киев", "Токио", "Минск"] 
# Получить dict_ = ["Украина": "Киев", "Япония": "Токио", "Беларусь": "Минск"]

list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
dict_ = {}
# Comment: Словари не упорядочнены, поэтому отображаемая поочерёдность может отличаться
# Я бы реализовал так:
# for item in list_1:
#     dict_.update(dict([item.split('-')]))
# for item in list(dict_.keys()):
#     if dict_[item] not in list_2:
#         dict_.pop(item)

for capital in list_2:
    for item in list_1:
        val_ = list(item.split('-'))
        if val_[1] == capital:
            dict_.update(dict([item.split('-')]))

print(dict_)        
print('\n')

# 6. Сгенерировать словарь-шифратор, то есть словарь, где ключ и значение являются символами. 
# Используя словарь, зашифровать/расшифровать введенное сообщение.
# str_ = 'Lorem consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
str_ = input('Введите текст для шифрования:')
print('Начальный текст:\n', str_)
list_ = list(set(list(str_)))
list_copy = list_.copy()
key_ = {}
while len(list_) > 0:
    val_1 = random.choice(list_)
    val_2 = random.choice(list_copy)
    key_.update({val_1: val_2})
    list_.remove(val_1)
    list_copy.remove(val_2)
print('Ключ:\n', key_)

str_encoded = str('')
for i in str_:
    str_encoded = str_encoded + str(key_.get(i))
print('Кодированный текст:\n', str_encoded)

str_decoded = str('')
for i in str_encoded:
    for k, v in key_.items():
        if i == v:
            str_decoded = str_decoded + k
            continue

print('Декодированный текст:\n', str_decoded)
if str_ == str_decoded:
    print('Кодированный и декодированный текст совпадают.')
else:
    print('Кодированный и декодированный текст НЕ СОВПАДАЮТ!')
print('\n')

# 7. Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же 
# числа, возведенные в куб.
dict_ = {a: a ** 3 for a in range(10)}
print(dict_)
print('\n')

# 8. Создайте словарь из строки следующим образом: в качестве ключей возьмите буквы 
# строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
str_ = 'Lorem consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
list_ = list(set(list(str_)))
dict_ = {}
for i in list_:
    count_ = str_.count(i)
    dict_.update({i: count_})
print('Начальный текст:\n', str_)
print('Словарь:', dict_)
