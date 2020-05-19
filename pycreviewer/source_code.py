# -*- coding: utf-8 -*-
from pycparser import c_ast
from pycparser.c_ast import Node

class SourceCode(object):
    """
    SourceCodeクラスは、ソースコード情報を抽象化し、各要素にアクセスする機能を提供する。
    SouceCodeクラスは、pycparser.parse()によって生成されたc_astオブジェクトを利用する。
    """

    def __init__(self, ast):
        print("SourceCode Obj Created.")
        self.ast = ast

    def __Switches__(self)->list:
        """
        Switch構文の一覧を返す
        """
        return []

    def __Cases__(self)->list:
        """
        Switch構文に対するCase文(defaultを含む)の一覧を返す
        """
        return []

    def DefinedFunctions(self)->list:
        """
        定義された関数の一覧を返す
        """
        ret = []
        for ext in self.ast:
            if(isinstance(ext, c_ast.FuncDef)):
                function = DefinedFunction(ext.decl.name, '', '', ext.coord)
                ret.append(function)
        return ret

    def StaticValiables(self)->list:
        """
        静的変数の一覧を返す
        """
        ret = []
        for ext in self.ast:
            if(hasattr(ext, 'type')):
                if(isinstance(ext.type, (c_ast.ArrayDecl,c_ast.TypeDecl,c_ast.PtrDecl))):
                    if(hasattr(ext, 'storage')):
                        if(ext.storage != []):
                            if(ext.storage[0] == 'static'):
                                valiable = Valiable(ext.name, '', ext.coord)
                                ret.append(valiable)
        return ret

    def GlobalValiables(self)->list:
        """
        グローバル変数の一覧を返す
        """
        ret = []
        for ext in self.ast:
            if(hasattr(ext, 'type')):
                if(isinstance(ext.type, (c_ast.ArrayDecl,c_ast.TypeDecl,c_ast.PtrDecl))):
                    if(hasattr(ext, 'storage')):
                        if(ext.storage == []):
                            valiable = Valiable(ext.name, '', ext.coord)
                            ret.append(valiable)
        return ret

    def SearchNoBreakInCase(self)->list:
        """
        Case文にbreakがない箇所を検索する
        """
        ret = []
        caseVisitor = CaseVisitor()
        caseVisitor.visit(self.ast)
        for node in caseVisitor.visitedList():
            breakVisitor = BreakVisitor()
            breakVisitor.visit(node)
            if(len(breakVisitor.visitedList()) == 0):
                case = Case(node.coord)
                ret.append(case) 
        return ret

    def SearchNoDefaultInSwitch(self)->list:
        """
        Switch構文内にdefaultがない箇所を検索する      
        """
        ret = []
        switchVistor = SwitchVisitor()
        switchVistor.visit(self.ast)
        for node in switchVistor.visitedList():
            defaultVisitor = DefaultVisitor()
            defaultVisitor.visit(node)
            if(len(defaultVisitor.visitedList()) == 0):
                swt = Switch(node.coord)
                ret.append(swt) 
        return ret

    def SearchReculsiveFunctionCall(self)->list:
        """
        再起呼び出し関数を検索する
        """
        ret = []
        for ext in self.ast:
            if(isinstance(ext, c_ast.FuncDef)):
                    funcname = ext.decl.name
                    v = FuncCallVisitor(funcname)
                    v.visit(self.ast)
                    for node in v.visitedList():
                        funccall = FunctionCall(funcname, node.name.coord)
                        ret.append(funccall)
        return ret
class Coord(object):
    """
    Coordクラスは、ソースコードの座標情報を抽象化したデータクラス
    """
    def __init__(self, line, col):
        self.line = line
        self.col = col

class DefinedFunction(object):
    """
    Functionクラスは、定義された関数情報を抽象化するデータクラス
    """
    def __init__(self, name:str, param, ret, coord):
        self.name = name
        self.param = param
        self.ret = ret
        self.coord = coord
    def Name(self)->str:
        return self.name
    def Param(self)->list:
        return self.param
    def Return(self):
        return self.ret
    def Coord(self):
        return self.coord

class FunctionCall(object):
    """
    FunctionCallクラスは、関数呼び出し情報を抽象化するデータクラス
    """
    def __init__(self, name:str,coord):
        self.name = name
        self.coord = coord
    def Name(self)->str:
        return self.name
    def Coord(self):
        return self.coord

class Case(object):
    """
    Caseクラスは、Case構文情報を抽象化するデータクラス
    """
    def __init__(self,coord):
        self.coord = coord

class Switch(object):
    """
    Switchクラスは、Switch構文情報を抽象化するデータクラス
    """
    def __init__(self,coord):
        self.coord = coord

class Valiable(object):
    """
    Valiableクラスは、変数情報を抽象化するデータクラス
    """
    def __init__(self, name:str,type:str, coord):
        self.name = name
        self.type = type
        self.coord = coord
    def Name(self)->str:
        return self.name
    def Coord(self):
        return self.coord


class FuncCallVisitor(c_ast.NodeVisitor):
    """
    FuncCallVisitorクラスはc_astモジュールのNodeVisitorクラスを継承し、
    指定した関数名のFuncCallノードを再起的に検索する機能を提供する。
    """
    def __init__(self, funcname):
        self.funcname = funcname
        self.visited = []

    def visit_FuncCall(self, node):
        if node.name.name == self.funcname:
            self.visited.append(node)
        # Visit args in case they contain more func calls.
        if node.args:
            self.visit(node.args)
    
    def visitedList(self):
        return self.visited

class CaseVisitor(c_ast.NodeVisitor):
    """
    CaseVisitorクラスはc_astモジュールのNodeVisitorクラスを継承し、
    Caseノードを再起的に検索する機能を提供する。
    """
    def __init__(self):
        self.visited = []

    def visit_Case(self, node):
        self.visited.append(node)
    
    def visitedList(self):
        return self.visited

class BreakVisitor(c_ast.NodeVisitor):
    """
    BreakVisitorクラスはc_astモジュールのNodeVisitorクラスを継承し、
    Breakノードを再起的に検索する機能を提供する。
    """
    def __init__(self):
        self.visited = []

    def visit_Break(self, node):
        self.visited.append(node)
    
    def visitedList(self):
        return self.visited

class SwitchVisitor(c_ast.NodeVisitor):
    """
    SwitchVisitorクラスはc_astモジュールのNodeVisitorクラスを継承し、
    Switchノードを再起的に検索する機能を提供する。
    """
    def __init__(self):
        self.visited = []

    def visit_Switch(self, node):
        self.visited.append(node)
    
    def visitedList(self):
        return self.visited

class DefaultVisitor(c_ast.NodeVisitor):
    """
    DefaultVisitorクラスはc_astモジュールのNodeVisitorクラスを継承し、
    Defaultノードを再起的に検索する機能を提供する。
    """
    def __init__(self):
        self.visited = []

    def visit_Default(self, node):
        self.visited.append(node)
    
    def visitedList(self):
        return self.visited

    # def print_ext_class_name(filename):
    #     ast = parse_file(filename, use_cpp=True,
    #         cpp_path='gcc',
    #         cpp_args=['-E', r'-Iutils/fake_libc_include'])
    #     for ext in ast:
    #         if(hasattr(ext, 'type')):
    #             print(ext.type.__class__.__name__)
    #         else:
    #             print(ext.__class__.__name__)

    # def print_func_def_names(filename):
    #     ast = parse_file(filename, use_cpp=True,
    #         cpp_path='gcc',
    #         cpp_args=['-E', r'-Iutils/fake_libc_include'])
    #     for ext in ast:
    #         if(isinstance(ext, c_ast.FuncDef)):
    #             print(ext.decl.name)

    # def print_static_valiable_names(filename):
    #     ast = parse_file(filename, use_cpp=True,
    #         cpp_path='gcc',
    #         cpp_args=['-E', r'-Iutils/fake_libc_include'])
    #     for ext in ast:
    #         if(hasattr(ext, 'type')):
    #             if(isinstance(ext.type, (c_ast.ArrayDecl,c_ast.TypeDecl,c_ast.PtrDecl))):
    #                 if(hasattr(ext, 'storage')):
    #                     if(ext.storage[0] == 'static'):
    #                         print("Static valiable: " + ext.name)


