# Проработать встроенние функции множеств. 
# Встроенние функции можно взять на сайте
# (https: // www.programiz.com/python-programming/set), раздел “Built-in Functions with Set”. 
# Но на єтом сайте приведени примери для списков, Задача переделать примери для множеств.


# Built-in Functions with Set
# Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. 
# are commonly used with sets to perform different tasks.

l = set([1, 5, 4, 3])
print(type(l), l)
print('all():', all(l))
print('any():', any(l))
print('len():', len(l))
print('enumerate():', enumerate(l), set(enumerate(l)))
print('min():', min(l))
print('max():', max(l))
print('sum():', sum(l))
print('sorted():', sorted(l))

l = set([0, False])
print('\n')
print(type(l), l)
print('all():', all(l))
print('any():', any(l))
print('len():', len(l))
print('enumerate():', enumerate(l), set(enumerate(l)))
print('min():', min(l))
print('max():', max(l))
print('sum():', sum(l))
print('sorted():', sorted(l))

l = set([1, 3, 4, 0])
print('\n')
print(type(l), l)
print('all():', all(l))
print('any():', any(l))
print('len():', len(l))
print('enumerate():', enumerate(l), set(enumerate(l)))
print('min():', min(l))
print('max():', max(l))
print('sum():', sum(l))
print('sorted():', sorted(l))

l = set([0, False, 5])
print('\n')
print(type(l), l)
print('all():', all(l))
print('any():', any(l))
print('len():', len(l))
print('enumerate():', enumerate(l), set(enumerate(l)))
print('min():', min(l))
print('max():', max(l))
print('sum():', sum(l))
print('sorted():', sorted(l))

l = set([])
print('\n')
print(type(l), l)
print('all():', all(l))
print('any():', any(l))
print('len():', len(l))
print('enumerate():', enumerate(l), set(enumerate(l)))
# ValueError: min() arg is an empty sequence
# print('min():', min(l))
# print('max():', max(l))
print('sum():', sum(l))
print('sorted():', sorted(l))

l = {1.0, (1, 2, 3), 'Hello'}
print('\n')
print(type(l), l)
print('all():', all(l))
print('any():', any(l))
print('len():', len(l))
print('enumerate():', enumerate(l), set(enumerate(l)))
# TypeError: '<' not supported between instances of 'float' and 'str'
# print('min():', min(l))
# print('max():', max(l))
# TypeError: unsupported operand type(s) for +: 'float' and 'tuple'
# print('sum():', sum(l))
# print('sorted():', sorted(l))

# l = enumerate({'bread', 'milk', 'butter'})
# print(type(l), 'enumerate():', l, set(l))
l = {'bread', 'milk', 'butter'}
print('\n')
print(type(l), l)
print('all():', all(l))
print('any():', any(l))
print('len():', len(l))
print('enumerate():', enumerate(l), set(enumerate(l)))
print('min():', min(l))
print('max():', max(l))
# TypeError: unsupported operand type(s) for +: 'float' and 'tuple'
# print('sum():', sum(l))
# print('sorted():', sorted(l))
