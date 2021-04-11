# Проработать встроенние функции множеств. 
# Встроенние функции можно взять на сайте
# (https: // www.programiz.com/python-programming/set), раздел “Built-in Functions with Set”. 
# Но на єтом сайте приведени примери для списков, Задача переделать примери для множеств.


# Built-in Functions with Set
# Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. 
# are commonly used with sets to perform different tasks.

# all()	Returns True if all elements of the set are true ( or if the set is empty).
# any()	Returns True if any element of the set is true. If the set is empty, returns False.

l = set([1, 3, 4, 5])
print(type(l), l, 'all():', all(l))
print(type(l), l, 'any():', any(l))
print(type(l), l, 'len():', len(l))
print(type(enumerate(l)), 'enumerate():', enumerate(l), set(enumerate(l)))

l = set([0, False])
print('\n')

print(type(l), l, 'all():', all(l))
print(type(l), l, 'any():', any(l))
print(type(l), l, 'len():', len(l))
print(type(enumerate(l)), 'enumerate():', enumerate(l), set(enumerate(l)))

l = set([1, 3, 4, 0])
print('\n')
print(type(l), l, 'all():', all(l))
print(type(l), l, 'any():', any(l))
print(type(l), l, 'len():', len(l))
print(type(enumerate(l)), 'enumerate():', enumerate(l), set(enumerate(l)))

l = set([0, False, 5])
print('\n')
print(type(l), l, 'all():', all(l))
print(type(l), l, 'any():', any(l))
print(type(l), l, 'len():', len(l))
print(type(enumerate(l)), 'enumerate():', enumerate(l), set(enumerate(l)))

l = set([])
print('\n')
print(type(l), l, 'all():', all(l))
print(type(l), l, 'any():', any(l))
print(type(l), l, 'len():', len(l))
print(type(enumerate(l)), 'enumerate():', enumerate(l), set(enumerate(l)))

l = {1.0, (1, 2, 3), 'Hello'}
print('\n')
print(type(l), l, 'all():', all(l))
print(type(l), l, 'any():', any(l))
print(type(l), l, 'len():', len(l))
print(type(enumerate(l)), 'enumerate():', enumerate(l), set(enumerate(l)))

# l = enumerate({'bread', 'milk', 'butter'})
# print(type(l), 'enumerate():', l, set(l))
l = {'bread', 'milk', 'butter'}
print(type(enumerate(l)), 'enumerate():', enumerate(l), set(enumerate(l)))


# enumerate()	Returns an enumerate object. It contains the index and value for all the 
# items of the set as a pair.

# l = enumerate({'bread', 'milk', 'butter'})
# print(type(l), 'enumerate():', enumerate(l), list(l))

# len()	Returns the length(the number of items) in the set.
# max()	Returns the largest item in the set.
# min()	Returns the smallest item in the set.
# sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
# sum()	Returns the sum of all elements in the set.
