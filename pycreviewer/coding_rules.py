# -*- coding: utf-8 -*-
from .check_conditions import CheckConditions
from .source_code import SourceCode 

class CheckResult(object):
    """
    CheckResultクラスは、CodingRulesクラスのコードチェック結果を格納するデータクラスである。
    """
    def __init__(self, id, level, msg, coord):
        self.id = id
        self.level = level
        self.msg = msg
        self.coord = coord
        print(vars(self))

    def output_str(self):
        return vars(self)

class CodinfgRules(object):
    """
    CodingRulesクラスはコーディングルールを抽象化し、コードが各ルールに逸脱していないかをチェックする機能を持つ。
    チェック対象となるコード情報は、SourceCodeオブジェクトを参照し取得する。
    各種ルールに対する詳細なチェック条件を取得するために、CodgingRulesクラスは、CheckConditionオブジェクトを参照する。
    """
    def __init__(self, code:SourceCode, condtions:CheckConditions):
        self.code = code
        self.condtions = condtions

    def check_all(self):
        results = []
        results.append(CheckResult("dummy", "WARN", "testtest", "./examples/c_files/xxxx.c::7::12"))
        return results

    def check_static_variable_prefix(self)->list:
        """
        静的変数の接頭辞を確認する
        """
        check_results = []
        condition = self.condtions.StaticVariablePrefix()
        if(not condition):
            return check_results
        variables = self.code.StaticValiables()
        prefix = condition.param
        for variable in variables:
            if(not variable.Name().startswith(prefix)):
                check_result = CheckResult(condition.id, condition.level, variable.Name()+' does not have the prefix '+prefix+'.', variable.coord) 
                check_results.append(check_result)
        return check_results
    
    def check_global_variable_prefix(self)->list:
        """
        グローバル変数の接頭辞を確認する
        """
        check_results = []
        condition = self.condtions.GlobalVariablePrefix()
        if(not condition):
            return check_results
        variables = self.code.GlobalValiables()
        prefix = condition.param
        for variable in variables:
            if(not variable.Name().startswith(prefix)):
                check_result = CheckResult(condition.id, condition.level, variable.Name()+' does not have the prefix '+prefix+'.', variable.coord) 
                check_results.append(check_result)
        return check_results

    def check_variable_short_name(self)->list:
        """
        名前が短い変数を確認する
        """
        check_results = []
        condition = self.condtions.VariableShortName()
        if(not condition):
            return check_results
        length_min = condition.param
        variables = self.code.Varialbles()
        for variable in variables:
            if(len(variable.Name()) <= length_min):
                check_result = CheckResult(condition.id, condition.level, variable.Name()+' is too short a variable name.', variable.coord)
                check_results.append(check_result)
        return check_results

    def check_function_blacklist(self)->list:
        """
        使用禁止の関数が利用されているか確認する
        """
        check_results = []
        condition = self.condtions.FunctionBlackList()
        if(not condition):
            return check_results
        for funcname in condition.param:
            funccalls = self.code.SearchFunctionCalls(funcname)
            if(len(funccalls) > 0):
                for funccall in funccalls:
                    check_result = CheckResult(condition.id, condition.level, funcname+' a is one of function blacklist.', funccall.coord) 
                    check_results.append(check_result)
        return check_results