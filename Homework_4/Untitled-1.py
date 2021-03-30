str_list = ('ABC', '123ABC', '_123abc', 'ABC_123',
      '123456', '123.456', ' ', 'Abc', 'ABC-123', 'ABC.123')
fmt = '%-15s%-10s%-10s%-10s%-15s%-15s%-10s%-10s%-15s%-10s%-10s%-10s'
print(fmt % ('string', 'isalpha', 'isalnum', 'isdigit', 'isdecimal', 'isidentifier', 'islower',
             'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper'))
for s in str_list:
    print(fmt % (s, s.isalpha(), s.isalnum(), s.isdigit(), s.isdecimal(), s.isidentifier(), s.islower(),
                 s.isnumeric(), s.isprintable(), s.isspace(), s.istitle(), s.isupper()))
