# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# pycreviewer: check_conditions.py
# Dromar [https://github.com/dromar-soft]
# License: MIT
#------------------------------------------------------------------------------
import json

class Condition(object):
    """
    The Condition class is a data class for a single check condition.
    """
    def __init__(self,_id,param,level):
        self.id = _id
        self.param = param
        self.level = level

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

    def __condition_in_conditions__(self, key:str)->Condition:
        if key in self.__conditionsKey__():
            condition_dict = self.__conditionsKey__()[key]
            if 'param' in condition_dict and 'level' in condition_dict and 'id' in condition_dict :
                return Condition(condition_dict['id'], condition_dict['param'], condition_dict['level'])
            else :
                return None
        else:
            return None

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

    def StaticVariablePrefix(self)->Condition:
        return self.__condition_in_conditions__('static_variable_prefix')

    def GlobalVariablePrefix(self)->Condition:
        return self.__condition_in_conditions__('global_variable_prefix')

    def VariableShortName(self)->Condition:
        return self.__condition_in_conditions__('variable_short_name')
    
    def FunctionBlackList(self)->Condition:
        return self.__condition_in_conditions__('function_blacklist')
    
    def NoBreakInSwitch(self)->Condition:
        return self.__condition_in_conditions__('no_break_in_switch')

    def NoDefaultInSwitch(self)->Condition:
        return self.__condition_in_conditions__('no_default_in_switch')

    def RecursiveCall(self)->Condition:
        return self.__condition_in_conditions__('recursive_call')
