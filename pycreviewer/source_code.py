# -*- coding: utf-8 -*-
from pycparser import c_ast
from pycparser.c_ast import Node
from pycparser.plyparser import Coord
from typing import List


class Token(object):
    """
    TokenクラスはC言語の基本要素を抽象化したデータクラスである。
    Tokenクラスは、name,coordの２つの属性を持つ
    name:
        基本要素の名称を格納する。
        例えば、基本要素が変数名などのSymbolの場合は、そのSymbol名を格納する
        また、基本要素がbreakなどのキーワードの場合は、キーワード名そのものを格納する
    __coord:
        基本要素の記述位置(ファイル名、行、列)を示す。
        coordの実体はplyparser.Coordクラスのインスタンスである。
        plyparser.Coordクラスの利用を隠蔽化するため、ファイル名、行、列へのアクセサを実装する。
    file:
         基本要素の記述されたファイル名を示す
    line:
        基本要素の記述された行位置を示す
    column:
        基本要素の記述された列位置を示す
    """
    def __init__(self, name:str, coord:Coord):
        self.name = name
        self.__coord = coord
        self.file = coord.file
        self.line = coord.line
        self.column = coord.column

Tokens = List[Token]

class SourceCode(object):
    """
    SourceCodeクラスは、ソースコード情報を抽象化し、各要素にアクセスする機能を提供する。
    SouceCodeクラスは、pycparser.parse()によって生成されたc_astオブジェクトを利用する。
    """

    def __init__(self, ast):
        self.ast = ast

    def DefinedFunctions(self)->Tokens:
        """
        定義された関数の一覧を返す
        """
        ret = []
        for ext in self.ast:
            if(isinstance(ext, c_ast.FuncDef)):
                function = Token(ext.decl.name,ext.coord)
                ret.append(function)
        return ret

    def SearchFunctionCalls(self, target_funcname:str)->Tokens:
        """
        特定の関数がコールされているか検索し、検索結果をFunctionCallオブジェクトのリスト形式で取得する
        検索のアルゴリズムはは関数名の文字列比較であり、引数や戻り値は考慮しない
        """
        ret = []
        for ext in self.ast:
            if(isinstance(ext, c_ast.FuncDef)):
                    v = FuncCallVisitor(target_funcname)
                    v.visit(ext)
                    for node in v.visitedList():
                        token = Token(target_funcname, node.name.coord)
                        ret.append(token)
        return ret

    def StaticValiables(self)->Tokens:
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
                                token = Token(ext.name, ext.coord)
                                ret.append(token)
        return ret

    def GlobalValiables(self)->Tokens:
        """
        グローバル変数の一覧を返す
        """
        ret = []
        for ext in self.ast:
            if(hasattr(ext, 'type')):
                if(isinstance(ext.type, (c_ast.ArrayDecl,c_ast.TypeDecl,c_ast.PtrDecl))):
                    if(hasattr(ext, 'storage')):
                        if(ext.storage == []):
                            token = Token(ext.name, ext.coord)
                            ret.append(token)
        return ret

    def __LocalVariables__(self)->Tokens:
        """
        ローカル変数(関数引数と関数定義内で宣言された変数）の一覧を返す
        """
        ret = []
        for ext in self.ast:
            if(isinstance(ext, c_ast.FuncDef)):
                visitor = VariableDeclVisitor()
                """
                main()のように、
                関数引数がnullの場合、argsがNoneになるため、Noneチェックを行う
                """
                if(ext.decl.type.args is not None):
                    visitor.visit(ext.decl.type.args)   #関数引数を探索
                visitor.visit(ext.body)             #関数定義内を探索
                for node in visitor.visitedList():
                    """
                    main(void)のように、
                    引数=void関数の場合、'void'がTypedecl(.declname=None,.coord=None)として探索されてしまうので、チェックではじく
                    """
                    if( node.declname and node.coord ):
                        token = Token(node.declname, node.coord)
                        ret.append(token)
        return ret

    def Varialbles(self)->Tokens:
        """
        変数宣言の一覧を返す
        """
        ret = []
        global_vars = self.GlobalValiables()  
        static_vars = self.StaticValiables()
        local_vars = self.__LocalVariables__()
        ret.extend(global_vars)
        ret.extend(static_vars)
        ret.extend(local_vars)
        return ret

    def SearchNoBreakInCase(self)->Tokens:
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
                token = Token('Case',node.coord)
                ret.append(token) 
        return ret

    def SearchNoDefaultInSwitch(self)->Tokens:
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
                token = Token('Switch',node.coord)
                ret.append(token) 
        return ret

    def SearchRecursiveFunctionCall(self)->Tokens:
        """
        再起呼び出し関数を検索する
        """
        ret = []
        for ext in self.ast:
            if(isinstance(ext, c_ast.FuncDef)):
                    funcname = ext.decl.name
                    v = FuncCallVisitor(funcname)
                    v.visit(ext)
                    for node in v.visitedList():
                        token = Token(funcname, node.name.coord)
                        ret.append(token)
        return ret

class VariableDeclVisitor(c_ast.NodeVisitor):
    """
    VariableDeclクラスはc_astモジュールのNodeVisitorクラスを継承し、
    TypeDeclノード(つまり変数宣言にまつわるノード)を再起的に検索する機能を提供する。
    """
    def __init__(self):
        self.visited = []

    def visit_TypeDecl(self, node):
        self.visited.append(node)
    
    def visitedList(self):
        return self.visited

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


