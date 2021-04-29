
# Классическая записи.
# Создали список из словарей книг
# asoiaf_books = [
#     {'title' : 'Game of Thrones', 'published' : '1996-08-01', 'pages': 694},
#     {'title' : 'Clash of Kings', 'published' : '1998-11-16', 'pages': 761},
#     {'title' : 'Storm of Swords', 'published' : '2000-08-08', 'pages': 973},
#     {'title' : 'Feast for Crows', 'published' : '2005-10-17', 'pages': 753},
#     {'title' : 'Dance with Dragons', 'published' : '2011-07-12', 'pages': 1016}
# ]

# # Функция по получению названия книги
# def get_title(book):
#     return book.get('title')

# # Функция по получению даты публикации книги
# def get_publish_date(book):
#     return book.get('published')

# # Функция по получению количества страниц в книге
# def get_pages(book):
#     return book.get('pages')

# # Сортируем по названию
# asoiaf_books.sort(key=get_title)
# for book in asoiaf_books:
#     print(book)
# print('-------------')

# # Сортируем по датам
# asoiaf_books.sort(key=get_publish_date)
# for book in asoiaf_books:
#     print(book)
# print('-------------')

# # Сортируем по количеству страниц
# asoiaf_books.sort(key=get_pages)
# for book in asoiaf_books:
#     print(book)



# # lambda функцию
# print('='*50)
# asoiaf_books = [
#     {'title' : 'Game of Thrones', 'published' : '1996-08-01', 'pages': 694},
#     {'title' : 'Clash of Kings', 'published' : '1998-11-16', 'pages': 761},
#     {'title' : 'Storm of Swords', 'published' : '2000-08-08', 'pages': 973},
#     {'title' : 'Feast for Crows', 'published' : '2005-10-17', 'pages': 753},
#     {'title' : 'Dance with Dragons', 'published' : '2011-07-12', 'pages': 1016}
# ]

# # Сортируем по названию
# for book in sorted(asoiaf_books, key=lambda book: book.get('title')):
#     print(book)

# print('-------------')
# # Сортируем по датам
# for book in sorted(asoiaf_books, key=lambda book: book.get('published')):
#     print(book)

# print('-------------')
# # Сортируем по количеству страниц
# for book in sorted(asoiaf_books, key=lambda book: book.get('pages')):
#     print(book)


# Функция map
# print('map: ', dir(map))
# name_lengths = map(len, ('Маша', 'Петя', 'Вася'))
# print('name_lengths: ', name_lengths)
# print('list(name_lengths): ', list(name_lengths))
# name_lengths = list(name_lengths)
# print('list(name_lengths): ', tuple(name_lengths))

# squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
# print('squares: ', squares)
# print('list(squares): ', list(squares))
# print(list(map(lambda x: x * x, [0, 1, 2, 3, 4])))
# print([x * x for x in [0, 1, 2, 3, 4]])


# import random
# names = ['Маша', 'Петя', 'Вася']
# print('names: ', names)
# code_names = ['Шпунтик', 'Винтик', 'Фунтик']

# for i in range(len(names)):
#     names[i] = random.choice(code_names)
# print('names: ', names)

names = ['Маша', 'Петя', 'Вася']
secret_names = map(lambda x: random.choice(['Шпунтик', 'Винтик', 'Фунтик']), names)
print('secret_names: ', list(secret_names))


# # Закодируем строки в Хешш
# print(dir(''))
# names = ['Маша', 'Петя', 'Вася']
# for i in range(len(names)):
#     names[i] = hash(names[i])
# print(names)

# names = ['Маша', 'Петя', 'Вася']
# secret_names = map(hash, names)
# print('list(secret_names): ', list(secret_names))


l1 = [1, 2, 3, ]
# print(l1[3])
l2 = [4, 5, 6, 7]
new_list = list(map(lambda x, y: x + y, l1, l2))
print('new_list: ', new_list)


# Функция Reduce
# from functools import reduce
# sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4], 2)
# print('sum: ', sum)
# x – текущий значение,
# а – аккумулятор. Это значение, которое возвращает выполнение lambda на предыдущем пункте.
# reduce() перебирает все значения, и запускает для каждого lambda на текущих значениях а и х, и возвращает результат в а для следующей итерации.

# sentences = [
#     'капитан джек воробей',
#     'капитан дальнего плавания',
#     'ваша лодка готова, капитан'
# ]
# cap_count = 0
# for sentence in sentences:
#     cap_count += sentence.count('капитан')
# print('cap_count: ', cap_count)


# cap_count = reduce(
#     lambda a, x: a + x.count('капитан'), sentences, 0
# )
# print('cap_count: ', cap_count)


# items = [1, 24, 17, 14, 9, 32, 2]
# all_max = reduce(lambda a, b: a if (a > b) else b, items)
# print('all_max: ', all_max)


# # Функция filter
# mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
# zolushka = list(filter(lambda x: x == 'мак', mixed))
# print('zolushka: ', zolushka)
# zolushka = [x for x in mixed if x=='мак']
# print('zolushka: ', zolushka)

# Функция zip
# a = [1,2,3]
# b = "xyz"
# c = (None, True, False)
# res = list(zip(a, b, c))
# print('res: ', res)
