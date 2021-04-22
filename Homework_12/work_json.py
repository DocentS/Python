import json

# dict_data = {
#     'ID': 210450,
#     'login': 'admin',
#     'name': 'John Smith',
#     'password': None,
#     'phone': 5550505,
#     'email': 'smith@mail.com',
#     'online': True,
#     'salary': 1000.3,
#     'friends':[123,456,789],
# }
# print('dict_data: ', dict_data)
# print('type(dict_data): ', type(dict_data))
# json_data = json.dumps(
#     dict_data
# )
# print('json_data: ', json_data)
# print('type(json_data): ', type(json_data))
# with open('./Lecture-8/data_dumps.json', 'w') as file:
#     file.write(json_data)


# dict_data = {
#     'ID': 210450,
#     'login': 'admin',
#     'name': 'John Smith',
#     'password': None,
#     'phone': 5550505,
#     'email': 'smith@mail.com',
#     'online': True,
#     'salary': 1000.3,
#     'friends':[123,456,789],
# }
# with open('./Lecture-8/data_dumps.json', 'w') as file:
#     json.dump(dict_data, file)


json_data = '''{
    "ID": 210450,
    "login": "admin",
    "name": "John Smith",
    "password": null,
    "phone": 5550505,
    "email": "smith@mail.com",
    "online": true,
    "salary": 1000.3,
    "friends": [123, 456, 789]
} '''
print('json_data: ', json_data)
print('type(json_data): ', type(json_data))
dict_data = json.loads(json_data)
print('dict_data: ', dict_data)
print('type(dict_data): ', type(dict_data))
print(dict_data['name'])
print(dict_data['phone'])


# with open('./Lecture-8/data_dumps.json', 'r') as json_data:
#     print('json_data: ', json_data)
#     print('type(json_data): ', type(json_data))
#     dict_data = json.load(json_data)
#     print('type(dict_data): ', type(dict_data))
# print('dict_data: ', dict_data)
# print(dict_data['name'])
# print(dict_data['phone'])