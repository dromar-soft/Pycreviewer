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

    def __ListValueInCondtions__(self, key:str)->list:
        if key in self.__conditionsKey__():
            return self.__conditionsKey__()[key]
        else:
            return []
    
    def __BoolValueInCondtions__(self, key:str)->bool:
        if key in self.__conditionsKey__():
            return self.__conditionsKey__()[key]
        else:
            return False


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
    
    def FunctionBlackList(self)->list:
        return self.__ListValueInCondtions__('function_black_list')
    
    def NoBreakInSwitch(self)->bool:
        return self.__BoolValueInCondtions__('no_break_in_switch')

    def NoDefaultInSwitch(self)->bool:
        return self.__BoolValueInCondtions__('no_default_in_switch')

    def ReculsiveCall(self)->bool:
        return self.__BoolValueInCondtions__('reculsive_call')
