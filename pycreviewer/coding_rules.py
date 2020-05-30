# -*- coding: utf-8 -*-
from .check_conditions import CheckConditions
from .source_code import SourceCode 

class CheckResult(object):
    """
    The CheckResult class is a data class that stores the results of code checks in the CodingRules class.
    """
    def __init__(self, id, level, msg, file, line, column):
        self.id = id
        self.level = level
        self.msg = msg
        self.file = file
        self.line = line
        self.column = column
        #print(vars(self))

    def output_str(self):
        return vars(self)

class CodinfgRules(object):
    """
    The CodingRules class abstracts coding rules and checks whether the code deviates from each rule or not.
    The code information to be checked is obtained by referring to the SourceCode object.
    The BookingRules class refers to the CheckCondition object in order to get detailed check conditions for various rules.
    """
    def __init__(self, code:SourceCode, condtions:CheckConditions):
        self.code = code
        self.condtions = condtions

    def check_all(self):
        """
        Run a check for all coding rules
        """
        check_results = []
        check_results.extend(self.check_static_variable_prefix())
        check_results.extend(self.check_global_variable_prefix())
        check_results.extend(self.check_variable_short_name())
        check_results.extend(self.check_recursive_call())
        check_results.extend(self.check_function_blacklist())
        check_results.extend(self.check_no_break_in_switch())
        check_results.extend(self.check_no_default_in_switch())
        return check_results

    def check_static_variable_prefix(self)->list:
        """
        Checking the prefix of static variables
        """
        check_results = []
        condition = self.condtions.StaticVariablePrefix()
        if(not condition):
            return check_results
        variables = self.code.StaticValiables()
        prefix = condition.param
        for variable in variables:
            if(not variable.name.startswith(prefix)):
                check_result = CheckResult(condition.id, condition.level, variable.name+' does not have the prefix '+prefix+'.', variable.file, variable.line, variable.column) 
                check_results.append(check_result)
        return check_results
    
    def check_global_variable_prefix(self)->list:
        """
        Checking the prefix of global variables
        """
        check_results = []
        condition = self.condtions.GlobalVariablePrefix()
        if(not condition):
            return check_results
        variables = self.code.GlobalValiables()
        prefix = condition.param
        for variable in variables:
            if(not variable.name.startswith(prefix)):
                check_result = CheckResult(condition.id, condition.level, variable.name+' does not have the prefix '+prefix+'.', variable.file, variable.line, variable.column) 
                check_results.append(check_result)
        return check_results

    def check_variable_short_name(self)->list:
        """
        Checking variables with short names
        """
        check_results = []
        condition = self.condtions.VariableShortName()
        if(not condition):
            return check_results
        length_min = condition.param
        variables = self.code.Varialbles()
        for variable in variables:
            if(len(variable.name) <= length_min):
                check_result = CheckResult(condition.id, condition.level, variable.name+' is too short a variable name.', variable.file, variable.line, variable.column)
                check_results.append(check_result)
        return check_results

    def check_recursive_call(self):
        """
        Checking recursive call.
        """
        check_results = []
        condition = self.condtions.RecursiveCall()
        if(not condition):
            return check_results
        isChecked = condition.param
        if(isChecked):
            calls = self.code.SearchRecursiveFunctionCall()
            for call in calls:
                check_result = CheckResult(condition.id, condition.level, call.name+' is a recursive call of the function.', call.file, call.line, call.column)
                check_results.append(check_result)            
        return check_results

    def check_function_blacklist(self)->list:
        """
        Check if an off-limits function is being used.
        """
        check_results = []
        condition = self.condtions.FunctionBlackList()
        if(not condition):
            return check_results
        for funcname in condition.param:
            calls = self.code.SearchFunctionCalls(funcname)
            if(len(calls) > 0):
                for call in calls:
                    check_result = CheckResult(condition.id, condition.level, funcname+' a is one of function blacklist.', call.file, call.line, call.column) 
                    check_results.append(check_result)
        return check_results
    
    def check_no_break_in_switch(self)->list:
        """
        Verify that there is no break statement in the Switch-Case statement.
        """
        check_results = []
        condition = self.condtions.NoBreakInSwitch()
        if(not condition):
            return check_results
        isChecked = condition.param
        if(isChecked):
            cases = self.code.SearchNoBreakInCase()
            for case in cases:
                check_result = CheckResult(condition.id, condition.level, 'No break statement in switch-case statement.', case.file, case.line, case.column)
                check_results.append(check_result)
        return check_results

    def check_no_default_in_switch(self)->list:
        """
        Checking the absence of the default statement in the Switch statement.
        """
        check_results = []
        condition = self.condtions.NoDefaultInSwitch()
        if(not condition):
            return check_results
        isChecked = condition.param
        if(isChecked):
            switches = self.code.SearchNoDefaultInSwitch()
            for switch in switches:
                check_result = CheckResult(condition.id, condition.level, 'No default statement in switch-case statement.', switch.file, switch.line, switch.column)
                check_results.append(check_result)
        return check_results
