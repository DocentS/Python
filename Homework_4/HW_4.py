# print('\n  isalpha() - Returns True if all characters in the string are in the alphabet')
# print('\n  isalnum() - Returns True if all characters in the string are alphanumeric')
# print('\n  isdigit() - Returns True if all characters in the string are digits')
# print('\n  isdecimal() - Returns True if all characters in the string are decimals
# print('\n  isidentifier() - Returns True if the string is an identifier'
# print('\n  Function islower() - Returns True if all characters in the string are lower case')
# print('\n  Function isnumeric() - Returns True if all characters in the string are numeric')
# print('\n  Function isprintable() - Returns True if all characters in the string are printable')
# print('\n  Function isspace() - Returns True if all characters in the string are whitespaces')
# print('\n  Function istitle() 	Returns True if the string follows the rules of a title')
# print('\n  Function isupper() - Returns True if all characters in the string are upper case')
     


ss=('ABC', '123ABC', '_123abc', 'ABC_123',
      '123456', '123.456', ' ', 'Abc', 'ABC-123', 'ABC.123')
fmt = '%-15s%-10s%-10s%-10s%-15s%-15s%-10s%-10s%-15s%-10s%-10s%-10s'
print(fmt % ('string', 'isalpha', 'isalnum', 'isdigit', 'isdecimal', 'isidentifier', 'islower',
             'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper'))
for s in ss: 
    print(fmt % (s, s.isalpha(), s.isalnum(), s.isdigit(), s.isdecimal(),s.isidentifier(), s.islower(),
                 s.isnumeric(), s.isprintable(), s.isspace(), s.istitle(), s.isupper()))
    
    # print(s)

# _isalpha   isalnum   isdigit   isidentifier
# _ isalpha   isalnum   isdigit   isidentifier
