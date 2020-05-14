# -*- coding: utf-8 -*-

import unittest
import check_conditions  # テスト対象のモジュールをインポートする

class TestCheckConditions(unittest.TestCase):
    """check_conditionsクラステストを記述するクラス"""

    def test_Version_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.Version(), "0.1.0")

    def test_Version_NoVersionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.Version(), '')

    def test_StaticVariablePrefix_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.StaticVariablePrefix(), 'm_')
    
    def test_StaticVariablePrefix_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.StaticVariablePrefix(), '')

    def test_StaticVariablePrefix_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.StaticVariablePrefix(), '')

    def test_GlobalVariablePrefix_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.GlobalVariablePrefix(), 'g_')

    def test_GlobalVariablePrefix_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.GlobalVariablePrefix(), '')

    def test_GlobalVariablePrefix_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.GlobalVariablePrefix(), '')

    def test_VarialeLengthMin_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.VariableLengthMin(), 2)

    def test_VarialeLengthMin_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.VariableLengthMin(), 0)

    def test_VarialeLengthMin_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.VariableLengthMin(), 0)


if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    unittest.main()