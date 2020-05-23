# -*- coding: utf-8 -*-

import unittest
from pycreviewer.source_code import SourceCode
from pycreviewer.source_file_parser import parse
from pycreviewer.check_conditions import CheckConditions
from pycreviewer.coding_rules import CodinfgRules,CheckResult

class TestCodingRules(unittest.TestCase):
    """CodinfgRulesクラステストを記述するクラス
            正常系のテスト観点：
                期待する箇所でチェック検出できていること->件数で判断->len(戻り値)
                msgが正しいこと->固定メッセージ部の部分一致判定
                idが正しいこと->代表例１件で判定
                levelが正しいこと->代表例１件で判定
                coordについてはテストデータの管理が難しいため、ここではチェックしない。専用のテストケースを用意する
    """

    def setUp(self):

        ast = parse('./test_data/c_files/valid.c', ['-E', r'-Ipycreviewer/utils/fake_libc_include'])
        sourcecode_valid = SourceCode(ast)
        ast = parse('./test_data/c_files/none.c', ['-E', r'-Ipycreviewer/utils/fake_libc_include'])
        sourcecode_none = SourceCode(ast)
        conditions = CheckConditions('./test_data/default.json')
        self.rules_valid = CodinfgRules(sourcecode_valid, conditions)
        self.rules_none = CodinfgRules(sourcecode_none, conditions)

    def test_check_static_variable_prefix_valid(self):
        expect_id = 'R001'
        expect_level = 'SHOULD'
        expect_msg_part = 'does not have the prefix'
        check_results = self.rules_valid.check_static_variable_prefix() 
        self.assertEqual(len(check_results), 1)
        check_result = check_results[0]
        self.assertTrue(expect_msg_part in check_result.msg)
        self.assertEqual(check_result.id, expect_id)
        self.assertEqual(check_result.level, expect_level)
    def test_check_static_variable_prefix_none(self):
        check_results = self.rules_none.check_static_variable_prefix() 
        self.assertEqual(len(check_results), 0)        
    
    def test_check_global_variale_prefix_valid(self):
        expect_id = 'R002'
        expect_level = 'SHOULD'
        expect_msg_part = 'does not have the prefix'
        check_results = self.rules_valid.check_global_variable_prefix() 
        self.assertEqual(len(check_results), 1)
        check_result = check_results[0]
        self.assertTrue(expect_msg_part in check_result.msg)
        self.assertEqual(check_result.id, expect_id)
        self.assertEqual(check_result.level, expect_level) 
    def test_check_global_variable_prefix_none(self):
        check_results = self.rules_none.check_global_variable_prefix() 
        self.assertEqual(len(check_results), 0)

    def test_check_variable_short_name_valid(self):
        expect_id = 'R003'
        expect_level = 'MUST'
        expect_msg_part = 'is too short a variable name.'
        check_results = self.rules_valid.check_variable_short_name()
        self.assertEqual(len(check_results), 4)
        check_result_example = check_results[0]
        self.assertTrue(expect_msg_part in check_result_example.msg)
        self.assertEqual(check_result_example.id, expect_id)
        self.assertEqual(check_result_example.level, expect_level)    
    def test_check_variable_short_name_none(self):
        check_results = self.rules_none.check_variable_short_name()
        self.assertEqual(len(check_results), 0)

    def test_check_reculsive_call_valid(self):
        expect_id = 'R004'
        expect_level = 'MUST'
        expect_msg_part = 'is a recursive call of the function.'
        check_results = self.rules_valid.check_reculsive_call()
        self.assertEqual(len(check_results), 6)
        check_result_example = check_results[0]
        self.assertTrue(expect_msg_part in check_result_example.msg)
        self.assertEqual(check_result_example.id, expect_id)
        self.assertEqual(check_result_example.level, expect_level)
    def test_check_reculsive_call_none(self):
        check_results = self.rules_none.check_reculsive_call()
        self.assertEqual(len(check_results), 0)

    def test_check_function_blacklist_valid(self):
        expect_id = 'R005'
        expect_level = 'WANT'
        expect_msg = 'malloc a is one of function blacklist.'
        check_results = self.rules_valid.check_function_blacklist() 
        self.assertEqual(len(check_results), 2)
        check_result = check_results[0]
        self.assertTrue(expect_msg in check_result.msg)
        self.assertEqual(check_result.id, expect_id)
        self.assertEqual(check_result.level, expect_level) 
    def test_check_function_blacklist_none(self):
        check_results = self.rules_none.check_function_blacklist() 
        self.assertEqual(len(check_results), 0)
        
            