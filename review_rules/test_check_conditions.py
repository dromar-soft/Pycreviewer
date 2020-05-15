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

    def test_FunctionBlackList_vaild(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.FunctionBlackList(),["malloc","free"])
    def test_FunctionBlackList_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.FunctionBlackList(),[])
    def test_FunctionBlackList_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.FunctionBlackList(),[])

    def test_NoBreakInSwitch_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.NoBreakInSwitch(), True)
    def test_NoBreakInSwitch_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.NoBreakInSwitch(), False)
    def test_NoBreakInSwitch_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.NoBreakInSwitch(), False)
    
    def test_NoDefaultInSwitch_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.NoDefaultInSwitch(), True)
    def test_NoDefaultInSwitch_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.NoDefaultInSwitch(), False)
    def test_NoDefaultInSwitch_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.NoDefaultInSwitch(), False)
    
    def test_ReculsiveCall_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.ReculsiveCall(), True)
    def test_ReculsiveCall_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.ReculsiveCall(), False)
    def test_ReculsiveCall_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.ReculsiveCall(), False)
    

if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    unittest.main()