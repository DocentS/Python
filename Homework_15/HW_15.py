# Задачу из “Homework 9. Paбота с json обектом.” перевести в формат ООП.

# Класс должен содержать отрибути и методи. Отрибутами будут пути к исходному 
# и результирующему файлам. И как миниму 4 метода:

# конструктор должен на вход принимать возможние альтернативние варианти путей 
# к исходному и результирующему файлам, но и иметь дефолтние значения, которими и будут отрибути класса;
# метод для загрузки исходного json обекта из исходного файла;
# метод для оброботки словаря полученного из исходного json обекта;
# метод для загрузки полученного результата в новий результирующий json файл.
# Если придумаете еще больше методов будет хорошо. Помните о принципе “Единственной ответственности”.

# Екземпляр класса визивать через определенную точку входа python скрипта.

# Весь функционал покрить тестами с применением модуля unittest.

import json
import unittest

class ConvertJson:

    def __init__(self, file_source='HW.json', file_result='HW_result.json', catalog='./', codepage='UTF-8'):
        self.file_source_name = file_source
        self.file_result_name = file_result
        self.source_default_catalog = catalog
        self.default_codepaje_encoding = codepage
        self.origin_json = self.open_json
        self.transformed_json = self.JsonTransform(self.origin_json)
    
    @property
    def GetOriginJson(self):
        return(self.origin_json)

    @property
    def GetTransformedJson(self):
        return(self.transformed_json)
    
    @property
    def open_json(self):
        with open(self.source_default_catalog+self.file_source_name, encoding= self.default_codepaje_encoding) as file:
            data = json.load(file)
        return(data)
    
    def save_json(self):
        with open(self.source_default_catalog+self.file_result_name, 'w', encoding=self.default_codepaje_encoding) as file:
            json.dump(self.transformed_json, file, indent=1)

    def GetFullName(self, dict_):
        full_name = ''
        for key_, value_ in dict_.items():
            if key_ in ('firstName', 'lastName'):
                if len(full_name) > 0:
                    full_name += ' '
                full_name += value_
        return(full_name)

    def JsonTransform(self, data): 
        data_new = {}
        data_result = {}
        for data_key, data_value in data.items():
            
            for item in data_value:
                dict_types = {}    
                for key, value in item.items():

                    if isinstance(value, bool):
                        list_ = dict_types.pop('bool', [])
                        list_.append(key)
                        dict_types.update({'bool': list_})
                    
                    elif isinstance(value, int):
                        list_ = dict_types.pop('int',[])
                        list_.append(key)
                        dict_types.update({'int': list_})
                    
                    elif isinstance(value, float):
                        list_ = dict_types.pop('float', [])
                        list_.append(key)
                        dict_types.update({'float': list_})
                        
                    elif isinstance(value, str):
                        list_ = dict_types.pop('string', [])
                        list_.append(key)
                        dict_types.update({'string': list_})
                                    
                    elif type(value) == None:
                        list_ = dict_types.pop('none_type', [])
                        list_.append(key)
                        dict_types.update({'none_type': list_})
                    
                FullName = self.GetFullName(item)
                data_new.update({FullName: dict_types})
                data_result.update({data_key: data_new})
        return(data_result)


class TestHW(unittest.TestCase):
    
    def setUp(self):
        self.js = ConvertJson()
        
    def test_file_source(self):
        self.assertEqual(self.js.file_source_name, 'HW.json')

    def test_file_result(self):
        self.assertEqual(self.js.file_result_name, 'HW_result.json')
    
    def test_file_catalog(self):
        self.assertEqual(self.js.source_default_catalog, './')
        
    def test_file_codepaje(self):
        self.assertEqual(self.js.default_codepaje_encoding, 'UTF-8')

    def test_origin_json_type(self):
        self.assertTrue(isinstance(self.js.origin_json, dict))

    def test_transformed_json_type(self):
        self.assertTrue(isinstance(self.js.transformed_json, dict))

    def test_GetTransformedJson_type(self):
        self.assertTrue(isinstance(self.js.GetTransformedJson, dict))

if __name__ == "__main__":
    unittest.main()

    # js = ConvertJson()
    # print('OriginJson ', '-'*50)
    # print(js.GetOriginJson)
    # print('TransformedJson ', '-'*50)
    # print(js.GetTransformedJson)
    # js.save_json()
