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
        return []

    def StaticValiables(self)->list:
        """
        静的変数の一覧を返す
        """
        ret = []
        for ext in self.ast:
            if(hasattr(ext, 'type')):
                if(isinstance(ext.type, (c_ast.ArrayDecl,c_ast.TypeDecl,c_ast.PtrDecl))):
                    if(hasattr(ext, 'storage')):
                        if(ext.storage[0] == 'static'):
                            valiable = Valiable(ext.name, '', ext.coord)
                            ret.append(valiable)
        return ret

    def GlobalVariables(self)->list:
        """
        グローバル変数の一覧を返す
        """
        return []

    def SearchCasesOfNoBreakInSwitch(self)->list:
        """
        Switch構文内の各Case文にbreakがない箇所を検索する
        """
        return []

    def SearchNoDefaultInSwitch(self)->list:
        """
        Switch構文内にdefaultがない箇所を検索する      
        """
        return []

    def SearchReculsiveFunction(self)->list:
        """
        再起呼び出し関数を検索する
        """
        return []

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

# class Switch(object):
#     """
#     Switchクラスは、Switch構文情報を抽象化するデータクラス
#     """
#     def __init__(self,coord):
#         self.coord = coord

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


