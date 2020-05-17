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
        self.assertEqual(valiables[0].Name(), 'm_var_1')
        self.assertEqual(valiables[1].Name(), 'm_var_2')
    def test_StaticValiables_None(self):
        target = SourceCode(self.none_ast)
        valiables = target.StaticValiables()
        self.assertEqual(valiables, [])
        