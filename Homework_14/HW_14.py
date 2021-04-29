# 1.Создать функцию для генерирования списка словорей вида
# [{0: 0, }, {0: 0, 1: 1}, {0: 0, 1: 1, 2: 4}, {0: 0, 1: 1, 2: 4, 3: 9}, {0: 0, 1: 1, 2: 4, 3: 9, ... n: n**2}, ]
# где n – поименованний аргумент функции
# Функция будет использовать цикл for, внутри которой при помощи Dict Comprahansion будут
# генерироваться вложенние словари. Запись в результирующий список производиться при помощи метода append.
# Создать дикоратор для вичисления времени виполнения функци. Для создания дикоратора использовать модуль datetime
# Результатом визова функции должен бить вивод самого списка и продолжительности виполнения генерирования списка.
# 2.Дани списки
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# Используя методи функционального програмирования:
# 1. С первого и третьего списков оставить все четний числа
# 2. Со второго оставить все нечетние
# 3. Обеденить списки в один список кортежей пар(значение первого списка, значение второго списка, значение третьего списка)
# 4. По каждому кортежу определить сумму его значений, получите список сумм кортежей
# 5. После получения списка п.4 оставить в нем только нечетние значения
# Весь повторяющийся и не только код оформить в виде функций.
# Код должен бить максимально автоматизирован!

import datetime as dt


def create_dict():
    print('\nУкажите к-во элементов для построения списка словарей вида n: n**2')
    capacity = input()
    while capacity.isdigit() == False:
        print('Укажите целое число!')
        capacity = input()
    print('Словарь будет построен на ' + capacity + ' элемента(ов).')
    capacity = int(capacity)

    list_ = []
    dict_ = {}
    for i in range(capacity + 1):
        for item in range(i + 1):
            dict_.update({item: item})
        list_.append({k: v**2 for (k, v) in dict_.items()})
    return(list_)


def decorator_func(func):
    def wrapper(*args, **kwargs):
        start_time = dt.datetime.now()
        result = func(*args, **kwargs)
        print(result)
        print('Время выполнения: {} секунд.'.format(
            dt.datetime.now()-start_time))
        print('\n')
    return(wrapper)


def leave_even_numbers(list_):
    return(list(filter(lambda x: x % 2 == 0, map(int, list_))))


def leave_odd_numbers(list_):
    return(list(filter(lambda x: x % 2 == 1, map(int, list_))))


def create_list_of_tuples(*args, **kwargs):
    list_ = []
    for i in range(len(args)):
        list_.append(tuple(args[i]))
    return(list_)


def get_sum_each_tupl_in_list(list_of_tuples):
    list_ = []
    for i in range(len(list_of_tuples)):
        list_.append(sum(list_of_tuples[i]))
    return(list_)


def main():
    decorator_func(create_dict)()

    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    print('list_1:', list_1)
    print('list_2:', list_2)
    print('list_3:', list_3)
    print('\n')
    
    # 1. С первого и третьего списков оставить все четний числа
    # 2. Со второго оставить все нечетние
    list_1 = leave_even_numbers(list_1)
    print('list_1 even_numbers', list_1)
    list_2 = leave_odd_numbers(list_2)
    print('list_2 odd_numbers', list_2)
    list_3 = leave_even_numbers(list_3)
    print('list_3 even_numbers', list_3)    
    print('\n')

    # 3. Обеденить списки в один список кортежей пар(значение первого списка,
    # значение второго списка, значение третьего списка)
    list_of_tuples = create_list_of_tuples(list_1, list_2, list_3)
    print('list_of_tuples:', list_of_tuples)

    # 4. По каждому кортежу определить сумму его значений, получите список сумм кортежей
    list_of_sum = get_sum_each_tupl_in_list(list_of_tuples)
    print('list_of_sum:', list_of_sum)

    # 5. После получения списка п.4 оставить в нем только нечетние значения
    list_of_sum = leave_odd_numbers(list_of_sum)
    print('list_of_odd_numbers:', list_of_sum)

    # Весь повторяющийся и не только код оформить в виде функций.

if __name__ == "__main__":
    main()
