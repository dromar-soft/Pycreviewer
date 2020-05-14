import json

class CheckConditions():
    """
    CheckConditions class provide functions to decode JSON file 
    and refer to the setting conditions of various check rules.
    """
    def __load__(self, file_path:str):
        io = open(file_path, 'r')
        self.json_dict= json.load(io)
        io.close()

    def __init__(self, file_path:str):
        self.__load__(file_path)

    def __StrValueInCondtions__(self, key:str)->str:
        if key in self.__conditionsKey__():
            return self.__conditionsKey__()[key]
        else:
            return ''

    def __IntValueInCondtions__(self, key:str)->int:
        if key in self.__conditionsKey__():
            return self.__conditionsKey__()[key]
        else:
            return 0

    def __conditionsKey__(self):
        if 'conditions' in self.json_dict:
            return self.json_dict['conditions']
        else:
            return []

    def Version(self):
        if 'version' in self.json_dict:
            return self.json_dict['version']
        else:
            return ''

    def StaticVariablePrefix(self)->str:
        return self.__StrValueInCondtions__('static_variable_prefix')

    def GlobalVariablePrefix(self)->str:
        return self.__StrValueInCondtions__('global_variable_prefix')

    def VariableLengthMin(self)->int:
        return self.__IntValueInCondtions__('variable_length_min')
        