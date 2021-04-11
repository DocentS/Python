import random

# 1. Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали 
# количество учащихся в разных классах(1а, 1б, 2б, 6а, 7в и т. п.). 
school = {'1а': 0, '1б': 0, '2б': 0, '6а': 0, '7в': 0}
for k in school.keys():
    school[k] = random.randint(5, 20)
print(school)

# Внесите изменения в словарь согласно следующему: 
# а) в одном из классов изменилось количество учащихся, 
school['6а'] += 1
print(school)

# б) в школе появился новый класс, 
# school.update({'7г',0})
school.setdefault('7г', 0)
print(school)

# с) в школе был расформирован(удален) другой класс. Вычислите общее количество учащихся в школе.
del school['1б']
print(school)

# 2. Создайте словарь, где ключами являются числа, а значениями – строки. 
# Создайте функционал которий вернет новый словарь, "обратный" исходному, т. е. ключами являются строки, 
# а значениями – числа.
dict_ = dict.fromkeys(list(range(10)))
for k, v in dict_.items():
    dict_[k] = str(k)

for k, v in dict_.items():
    dict_[k] = str(k)
print(dict_) 

for k in list(dict_.keys()):
    if isinstance(k, int):
        dict_.setdefault(dict_[k], k)
        del dict_[k]
print(dict_)
