
str_ = 'Добро пожаловать на курс: "Introduction Python"!'
fruits = 'apple, banana, cherry, plum'
fruits_list = ('apple, banana, cherry, plum')
msg = '\nНажмите ENTER..'
print(f'\nИсходная строка - {str_}')
input(msg)

print('\n  Function capitalize() - Converts the first character to upper case')
print('Result:', str_.capitalize())
input(msg)

print('\n  Function swapcase() - Swaps cases, lower case becomes upper case and vice versa')
print('Result:', str_.swapcase())
input(msg)

print('\n  Function lower() - Converts a string into lower case')
print('Result:', str_.lower())
input(msg)

print('\n  Function title() - Converts the first character of each word to upper case')
print('Result:', str_.title())
input(msg)

print('\n  Function upper() - Converts a string into upper case')
print('Result:', str_.upper())
input(msg)

print('\n  Function casefold() - Converts string into lower case')
print('Result:', str_.casefold())
input(msg)

print('\n  Function center(len(str_)+5, "#")) - Returns a centered string')
print('Result:', str_.center(len(str_)+5, '#'))
input(msg)

# ---

print('\n  Function count("Introduction") - Returns the number of times a specified value occurs in a string')
print('Result:', str_.count('Introduction'))
input(msg)

print('\n  Function encode("utf-8") - Returns an encoded version of the string')
print('Result:', str_.encode('utf-8'))

print('\n  Function decode("utf-8") - Returns an decoded version of the string')
str_tmp = str_.encode('utf-8')
print('Result:', str_tmp.decode('utf-8'))
input(msg)

print('\n  Function endswith("Python"!") - Returns true if the string ends with the specified value')
print('Result:', str_.endswith('Python"!'))
print('\n  Function endswith("Python") - Returns true if the string ends with the specified value')
print('Result:', str_.endswith('Python'))
input(msg)

str_tmp = 'Добро пожаловать на курс:\t"Introduction Python"!'
print('\n  Function expandtabs(20) - Sets the tab size of the string')
print('Result:', str_tmp.expandtabs(20))
input(msg)

print('''\n  find("Introduction") - Searches the string for a specified value and returns the position of 
      where it was found''')
print('Result:', str_.find("Introduction"))
input(msg)

print('''\n  replace('"', "'") - Returns a string where a specified value is replaced with a 
    specified value''')
print('Result:', str_.replace('"', "'"))
input(msg)

print('\n  Function format({:,}) - Formats specified values in a string')
str_tmp = str_ + ' У вас возникнет {:,} вопросов.'
print('Result:', str_tmp.format(1000000))
input(msg)

print('''\n  Function format_map({'str1': 'Добро', 'str2': 'курс', 'str3': 
      'Python'}) - Formats specified values in a string''')
map_ = {'str1': 'Добро', 'str2': 'курс', 'str3': 'Python'}
print('Result:', '{str1} пожаловать на {str2}: "Introduction {str3}"!'.format_map(map_))
input(msg)

print('\n  Function ljust(len(str_)+5, "$") - Returns a left justified version of the string')
print('Result:', str_.ljust(len(str_)+5, '$'))

print('\n  Function rjust(len(str_)+5, "$") - Returns a right justified version of the string')
print('Result:', str_.rjust(len(str_)+5, '$'))
input(msg)

print('\n  Function startswith("Добро") - Returns true if the string starts with the specified value')
print('Result:', str_.startswith("Добро"))
input(msg)

print("\n  Function maketrans() - Returns a translation table to be used in translations")
trans = str_.maketrans('P', 'S', '"!')
print("maketrans('P', 'S'):", trans)
print("\n  Function translate() - Returns a translated string")
print('Result:', str_.translate(trans))
input(msg)

str_tmp = '***' + fruits + '***'
str_tmp = '***' + str_ + '***'
print('\nString:', str_tmp)
print("  Function lstrip('*') - Returns a left trim version of the string")
print('Result:', str_tmp.lstrip('*'))

print('\nString:', str_tmp)
print("  Function rstrip('*') - Returns a right trim version of the string")
print('Result:', str_tmp.rstrip('*'))

print('\nString:', str_tmp)
print("\n  Function strip('*') - Returns a trimmed version of the string")
print('Result:', str_tmp.strip('*'))
input(msg)

print('\n  Function join() - Joins the elements of an iterable to the end of the string')
print('Result:', ' '.join(fruits))
print('Result:', ''.join(fruits))
print('Result:', '*'.join(fruits))
input(msg)

print('\nString:', fruits)
print('''\n  index(",") - Searches the string for a specified value and returns the position 
      of where it was found''')
print('Result:', fruits.index(","))

print('''\n  rindex(",") - Searches the string for a specified value and returns the last 
      position of where it was found''')
print('Result:', fruits.rindex(","))
input(msg)

print('\n  Function split() - Splits the string at the specified separator, and returns a list')
print('Result:', fruits.split())
print('\n  Function rsplit(", ") - Splits the string at the specified separator, and returns a list')
print('Result:', fruits.rsplit(", "))
str_tmp = "apple, \nbanana, \ncherry, \nplum"
print('''\n  Function splitlines("apple, \nbanana, \ncherry, \nplum") - Splits the string at line breaks and returns a list''')
print('Result:', str_tmp.splitlines())
input(msg)

print('\n  Function partition() - Returns a tuple where the string is parted into three parts')
print('Result:', fruits.partition(' '))
input(msg)

print('\n  Function rpartition() - Returns a tuple where the string is parted into three parts')
print('Result:', fruits.rpartition(' '))
input(msg)

print('''\n  Function rfind('banana') - Searches the string for a specified value and returns the last 
    position of where it was found''')
print('Result:', fruits.find('banana'))
input(msg)

print('\n  Function zfill() - Fills the string with a specified number of 0 values at the beginning')
print('Result:', fruits.zfill(len(fruits) + 5))
input(msg)

str_list = ('ABC', '123ABC', '_123abc', 'ABC_123',
      '123456', '123.456', ' ', 'Abc', 'ABC-123', 'ABC.123')
fmt = '%-15s%-10s%-10s%-10s%-15s%-15s%-10s%-10s%-15s%-10s%-10s%-10s'
print(fmt % ('string', 'isalpha', 'isalnum', 'isdigit', 'isdecimal', 'isidentifier', 'islower',
             'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper'))
for s in str_list:
    print(fmt % (s, s.isalpha(), s.isalnum(), s.isdigit(), s.isdecimal(), s.isidentifier(), s.islower(),
                 s.isnumeric(), s.isprintable(), s.isspace(), s.istitle(), s.isupper()))
