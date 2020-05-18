# -*- coding: utf-8 -*-

import unittest
from pycreviewer.source_code import SourceCode
from pycreviewer.source_file_parser import parse

class TestSourceCode(unittest.TestCase):
    """SourceCodeクラステストを記述するクラス"""

    def setUp(self):

        self.cpp_args = ['-E', r'-Ipycreviewer/utils/fake_libc_include']

        self.valid_source = "./test_data/c_files/valid.c"
        self.valid_ast = parse(self.valid_source,self.cpp_args)

        self.none_source = "./test_data/c_files/none.c"
        self.none_ast = parse(self.none_source,self.cpp_args)

    def test_StaticValiables_valid(self):
        target = SourceCode(self.valid_ast)
        valiables = target.StaticValiables()
        self.assertEqual(valiables[0].Name(), 'm_int_val1')
        self.assertEqual(valiables[1].Name(), 'm_const_long_val2')
        self.assertEqual(valiables[2].Name(),'m_volatile_char_val3')
        self.assertEqual(len(valiables), 3)
    def test_StaticValiables_None(self):
        target = SourceCode(self.none_ast)
        valiables = target.StaticValiables()
        self.assertEqual(valiables, [])
    
    def test_GlobalValiables_valid(self):
        target = SourceCode(self.valid_ast)
        valiables = target.GlobalValiables()
        self.assertEqual(valiables[0].Name(), 'g_int_val1')
        self.assertEqual(valiables[1].Name(), 'g_const_long_val2')
        self.assertEqual(valiables[2].Name(), 'g_volatile_char_val3')
        self.assertEqual(len(valiables), 3)
    def test_GlobalValiables_None(self):
        target = SourceCode(self.none_ast)
        valiables = target.GlobalValiables()
        self.assertEqual(valiables, [])

    def test_DefinedFunctions_valid(self):
        target = SourceCode(self.valid_ast)
        functions = target.DefinedFunctions()
        self.assertEqual(functions[0].Name(), 'g_function_def1')
        self.assertEqual(functions[1].Name(), 'm_function_def2')
        self.assertEqual(len(functions), 2)
    def test_DefinedFunctions_None(self):
        target = SourceCode(self.none_ast)
        functions = target.DefinedFunctions()
        self.assertEqual(functions, [])

    def test_SearchReculsiveFunctionCall_valid(self):
        target = SourceCode(self.valid_ast)
        funccall = target.SearchReculsiveFunctionCall()
        self.assertEqual(funccall[0].Name(), 'g_function_def1')
        self.assertEqual(funccall[1].Name(), 'g_function_def1')
        self.assertEqual(funccall[2].Name(), 'g_function_def1')
        self.assertEqual(funccall[3].Name(), 'g_function_def1')
        self.assertEqual(funccall[4].Name(), 'g_function_def1')
        self.assertEqual(funccall[5].Name(), 'g_function_def1')
        self.assertEqual(len(funccall), 6)
    
    def test_SearchReculsiveFunctionCall_None(self):
        target = SourceCode(self.none_ast)
        steps = target.SearchReculsiveFunctionCall()
        self.assertEqual(steps, [])