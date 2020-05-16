from . import check_conditions
from . import ast_analyser

class CheckResult(object):
    """
    CheckResultクラスは、CodingRulesクラスのコードチェック結果を格納するデータクラスである。
    """
    def __init__(self, id, level, msg, coord):
        self.id = id
        self.level = level
        self.msg = msg
        self.coord = coord

    def output_str(self):
        return vars(self)

class CodinfgRules(object):
    """
    CodingRulesクラスはコーディングルールを抽象化し、コードが各ルールに逸脱していないかをチェックする機能を持つ。
    チェック対象となるコード情報は、AstAnaysisオブジェクトを参照し取得する。
    各種ルールに対する詳細なチェック条件を取得するために、CodgingRulesクラスは、CheckConditionクラスを参照する。
    """
    def __init__(self, code:ast_analyser.AstAnalyser, condtions:check_conditions.CheckConditions):
        self.code = code
        self.condtions = condtions

    def check(self):
        results = []
        results.append(CheckResult("dummy", "WARN", "testtest", "./examples/c_files/xxxx.c::7::12"))
        return results
