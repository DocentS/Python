import datetime

 
def decorator_fun(func):
  print("Inside decorator")
 
  def inner(*args, **kwargs):
    print("Inside inner function")
    
    func()
    print("Decorated the function")

  return inner 

def func_to():
    print("Inside actual function")
 
# # another way of using decorators
decorator_fun(func_to)()


# @decorator_fun
# def func_to():
# 	print("Inside actual function")


# func_to()

# def my_shiny_new_decorator(function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута 
#     #  вокруг декорируемой, получая возможность исполнять произвольный код до и после неё.
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#         function_to_decorate() # Сама функция
#         print("А я - код, срабатывающий после")
#     # Вернём эту функцию
#     return the_wrapper_around_the_original_function

# # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# def stand_alone_function():
#     print("Я простая одинокая функция.")

# # stand_alone_function()
# # print('-'*10)
# # # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору, который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую, готовую к использованию функцию:
# # stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# # stand_alone_function_decorated()


# # print('='*50)
# # stand_alone_function = my_shiny_new_decorator(stand_alone_function)
# # stand_alone_function()


# # print('='*50)
# # @my_shiny_new_decorator
# # def stand_alone_function():
# #     print("Я простая одинокая функция.")
# # stand_alone_function()


# # Мультидекоратор
# # print('='*50)
# # def bread(func):
# #     def wrapper():
# #         print()
# #         func()
# #         print("<\______/>")
# #     return wrapper

# # def ingredients(func):
# #     def wrapper():
# #         print("#помидоры#")
# #         func()
# #         print("~салат~")
# #     return wrapper

# # def sandwich(food="--ветчина--"):
# #     print(food)

# sandwich = bread(ingredients(sandwich))
# # # sandwich()

# # @ingredients
# # @bread
# # def sandwich(food="--ветчина--"):
# #     print(food)

# # sandwich()


# # Передача аргументов декорируеммой функции
# print('='*50)
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print("Смотри, что я получил:", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
# # Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции

# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)

# print_full_name("Vasya", "Pupkin")


# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     # Данная "обёртка" принимает любые аргументы
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print("Передали ли мне что-нибудь?:")
#         print(args)
#         print(kwargs)
#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitrary_arguments

# def decorator_name(funct):
#     # Данная "обёртка" принимает любые аргументы
#     def wrapper(*args, **kwargs):
#         # print("Code до")
#         start_time = datetime.datetime.now()
#         funct(*args, **kwargs)
#         print(datetime.datetime.now()-start_time)
#         # print("Code после")
#     return wrapper

# print('-'*50)
# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print("Python is cool, no argument here.")


# print('-'*50)
# @decorator_name
# def function_with_no_argument_():
#     print("Python is cool, no argument here.")

# function_with_no_argument_()

# print('-'*50)
# @decorator_name
# def function_with_arguments(a, b, c):
#     print(a, b, c)

# function_with_arguments(1, 2, 3)

# print('-'*50)
# @decorator_name
# def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
#     print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))

# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")


# # Передача аргументов декорируеммой функции
# # print('='*50)
# # def decorator_maker():
# #     print("Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")
# #     def my_decorator(func):
# #         print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
# #         def wrapped():
# #             print (
# #                 """
# #                     Я - обёртка вокруг декорируемой функции.
# #                     Я буду вызвана каждый раз, когда ты вызываешь декорируемую функцию.
# #                     Я возвращаю результат работы декорируемой функции.
# #                 """
# #             )
# #             return func()
# #         print("Я возвращаю обёрнутую функцию.")
# #         return wrapped
# #     print("Я возвращаю декоратор.")
# #     return my_decorator

# # # Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
# # new_decorator = decorator_maker()
# # # Теперь декорируем функцию
# # def decorated_function():
# #     print("Я - декорируемая функция.")
# # decorated_function = new_decorator(decorated_function)
# # # Теперь наконец вызовем функцию:
# # decorated_function()

# # print('-'*50)
# # @decorator_maker()
# # def decorated_function():
# #     print("Я - декорируемая функция.")

# # decorated_function()


# print('-'*50)
# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
#     print("Я создаю декораторы! И я получил следующие аргументы:", decorator_arg1, decorator_arg2)
#     def my_decorator(func):
#         print("Я - декоратор. И ты всё же смог передать мне эти аргументы:", decorator_arg1, decorator_arg2)
#         # Не перепутайте аргументы декораторов с аргументами функций!
#         def wrapped(function_arg1, function_arg2):
#             print(
#                 """
#                 Я - обёртка вокруг декорируемой функции.
#                 И я имею доступ ко всем аргументам
#                 \t- и декоратора: {0} {1}
#                 \t- и функции: {2} {3}
#                 Теперь я могу передать нужные аргументы дальше
#                 """.format(decorator_arg1, decorator_arg2,function_arg1, function_arg2))
#             return func(function_arg1, function_arg2)
#         return wrapped
#     return my_decorator

# @decorator_maker_with_arguments("Леонард", "Шелдон")
# def decorated_function_with_arguments(function_arg1, function_arg2):
#     print ("Я - декорируемая функция и я знаю только о своих аргументах: {0} {1}".format(function_arg1, function_arg2))


# decorated_function_with_arguments("Раджеш", "Говард")
