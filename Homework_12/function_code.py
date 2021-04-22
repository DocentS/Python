# import json

# def hello_world():
#     print("Hello World!")


# def empty_function():
#     pass


def add(a, b):
    '''
    Фукнции с позиционними аргументами
    '''
    print('a: ', a)
    print('b: ', b)
    return a + b


def keyword_function(a=1, b=2):
    '''
    Функции с именованными аргументами
    '''
    print('a: ', a)
    print('b: ', b)
    return a + b


# def mixed_function(a, b=2, c=3):
#     '''
#     Функции с позиционними и именованными аргументами
#     '''
#     return a + b + c

# def many(*args, **kwargs):
#     '''
#     *args, **kwargs
#     '''
#     print('args: ', args)
#     print('type(args): ', type(args))
#     print('kwargs: ', kwargs)
#     print('type(kwargs): ', type(kwargs))

# def many(name, job, age, salary):
#     '''
#     *args, **kwargs
#     '''
#     print('name: ', name)
#     print('job: ', job)
#     print('age: ', age)
#     print('salary: ', salary)


# def many(**kwargs):
#     '''
#     *args, **kwargs
#     '''
#     print('kwargs: ', kwargs)
#     name = kwargs['name']
#     print('name: ', name)



# # Особенность работи инструкции return
# # Инструкциия returnпреривает дальнейшуб аботу функции
# def my_max(a, b):
#     print('a: ', a)
#     print('b: ', b)
#     if a > b:
#         print('a: ', a)
#         return a
#     elif b > a:
#         return b
#         print('b: ', b)
#     else:
#         return 'equal'


# def function_return_some_params():
#     a = 1
#     b = 2
#     return a, b


# def function_return_some_input_params(a, b):
#     return a, b


# # Область видимость и глобальные переменные
# def function_a():
#     a = 1
#     b = 2
#     return a + b


# def function_b():
#     c = 3
#     return a + c

# def function_a():
#     global a
#     a = 1
#     b = 2
#     return a + b


# def function_b():
#     c = 3
#     return a + c


def main():
#     hello_world()
#     # Пустая функция
#     empty_function()
#     print(empty_function())

    # # Фукнции с позиционними аргументами
    # print(add(100, 2000))
    # print(add(2, 1))
    # print(add('ASDSD', 'qwew'))

    # # Недостаточно аргументов
    # print(add(1))
    # print(add('ASDSD'))

    # print(add(a=2, b=3))
    # total = add(b=4, a=5)
    # print(total)

    # # Неправильное название аргументов
    # add(c=5, d=2)

    # Фукнции с именованными аргументами
    # print(keyword_function(a=5, b=4))
    # print(keyword_function(b=4, a=5))
    # print(keyword_function(4, b=5))
    print(keyword_function(b=5))

    # Фукнции с позиционними и именованными аргументами
    # mixed_function(b=4, c=5)
    # print(mixed_function(68,  c=5, b=4))
    # print(mixed_function(1))
    # *args, **kwargs
    # many(1, 2, 3, name="Mike", job="programmer")
    # many(name="Mike", job="programmer", age=10, salary=2.5)

    # Особенность работи инструкции return
    # Инструкциия return преривает дальнейшую работу функции
    # a = 1
    # b = 2
    # print(my_max(a, b))
    # qwerty, _ = function_return_some_params()
    # print('_: ', _)
    # print('qwerty: ', qwerty)
    # print(function_return_some_params())
    # print(type(function_return_some_params()))

    # print(function_return_some_input_params(a, b))

    # Область видимость и глобальные переменные
    # print(function_a())
    # print(function_b())

    # # Local область видимости
    # def add_two(a):
    #     x = 2
    #     return a + x
    # print(add_two(3))
    # # print(х)

    # # Local область видимости
    # def add_four(a):
    #     x = 2
    #     def add_some():
    #         print("x = " + str(x))
    #         return a + x
    #     return add_some()
    # print(add_four(5))

    # # Global область видимости
    # x = 4
    # def fun():
    #     print(x+3)
    # print(fun())

    # # Анонимные функции, инструкция lambda
    # import math
    # sin_x_y = lambda x, y: math.sin(x) + y
    # print('sin_x_y: ', sin_x_y(1,2))
    # func_add = lambda x, y: x + y
    # print(func_add(1, 2))
    # # print(func_add('a', 'b'))
    # print((lambda x, y: x + y)(1, 2))
    # print((lambda x, y: x + y)('a', 'b'))
    # func = lambda *args: args
    # print(func(1, 2, 3, 4,6,8,9,4))

# if __name__ == '__main__':
#     main()


list_1 = [
        "Украина-Киев",
        "Россия-Сочи",
        "Беларусь-Минск",
        "Япония-Токио",
        "Германия-Мюнхен"
        ]
list_2 = ["Киев", "Токио", "Минск"]
d = {dict(i.split('-')[::-1] for i in list_1).get(k): k for k in list_2}
print(d)