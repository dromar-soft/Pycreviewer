# -*- coding: utf-8 -*-

import unittest
from pycreviewer.source_code import SourceCode
from pycreviewer.source_file_parser import parse

class TestSourceCode(unittest.TestCase):
    """SourceCodeクラステストを記述するクラス
            正常系のテスト観点：
                期待する箇所で検索できていること->件数で判断->len(戻り値)
                検索値が正しいこと->代表例１件で判定
                coordについてはテストデータの管理が難しいため、ここではチェックしない。専用のテストケースを用意する
    """

    def setUp(self):

        self.cpp_args = ['-E', r'-Ipycreviewer/utils/fake_libc_include']

        self.valid_source = "./test_data/c_files/valid.c"
        self.valid_ast = parse(self.valid_source,self.cpp_args)

        self.none_source = "./test_data/c_files/none.c"
        self.none_ast = parse(self.none_source,self.cpp_args)

    def test_StaticValiables_valid(self):
        target = SourceCode(self.valid_ast)
        valiables = target.StaticValiables()
        self.assertEqual(len(valiables), 3)
        example = valiables[0]
        self.assertEqual(example.Name(), 'm_int_val1')
    def test_StaticValiables_None(self):
        target = SourceCode(self.none_ast)
        valiables = target.StaticValiables()
        self.assertEqual(valiables, [])
    
    def test_GlobalValiables_valid(self):
        target = SourceCode(self.valid_ast)
        valiables = target.GlobalValiables()
        self.assertEqual(len(valiables), 3)
        example = valiables[0]
        self.assertEqual(example.Name(), 'g_int_val1')
    def test_GlobalValiables_None(self):
        target = SourceCode(self.none_ast)
        valiables = target.GlobalValiables()
        self.assertEqual(valiables, [])

    def test_DefinedFunctions_valid(self):
        target = SourceCode(self.valid_ast)
        functions = target.DefinedFunctions()
        self.assertEqual(len(functions), 2)
        example = functions[0]
        self.assertEqual(example.Name(), 'g_function_def1')
    def test_DefinedFunctions_None(self):
        target = SourceCode(self.none_ast)
        functions = target.DefinedFunctions()
        self.assertEqual(functions, [])

    def test_SearchFunctionCalls_valid(self):
        target = SourceCode(self.valid_ast)
        funccalls = target.SearchFunctionCalls('free')
        self.assertEqual(len(funccalls), 1)
        funccalls = target.SearchFunctionCalls('freeeee')
        self.assertEqual(len(funccalls), 0)
    def test_SearchFunctionCalls_none(self):
        target = SourceCode(self.none_ast)
        funccalls = target.SearchFunctionCalls('free')
        self.assertEqual(len(funccalls), 0)

    def test_SearchReculsiveFunctionCall_valid(self):
        target = SourceCode(self.valid_ast)
        funccalls = target.SearchReculsiveFunctionCall()
        self.assertEqual(len(funccalls), 6)
        example = funccalls[0]
        self.assertEqual(example.Name(), 'g_function_def1')
    def test_SearchReculsiveFunctionCall_None(self):
        target = SourceCode(self.none_ast)
        steps = target.SearchReculsiveFunctionCall()
        self.assertEqual(steps, [])

    def test_SearchNoBreakInCase_valid(self):
        target = SourceCode(self.valid_ast)
        cases = target.SearchNoBreakInCase()
        self.assertEqual(len(cases), 1)
    def test_SearchNoBreakInCase_none(self):
        target = SourceCode(self.none_ast)
        cases = target.SearchNoBreakInCase()
        self.assertEqual(cases, [])

    def test_SearchNoDefaultInSwitch_valid(self):
        target = SourceCode(self.valid_ast)
        cases = target.SearchNoDefaultInSwitch()
        self.assertEqual(len(cases), 1)
    def test_SearchNoDefaultInSwitch_none(self):
        target = SourceCode(self.none_ast)
        cases = target.SearchNoDefaultInSwitch()
        self.assertEqual(cases, [])