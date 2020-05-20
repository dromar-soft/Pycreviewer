# -*- coding: utf-8 -*-

import unittest
from pycreviewer import check_conditions  # テスト対象のモジュールをインポートする

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
        self.assertEqual(obj.StaticVariablePrefix().id, 'R001')
        self.assertEqual(obj.StaticVariablePrefix().param, 'm_')
        self.assertEqual(obj.StaticVariablePrefix().level, 'SHOULD')
    def test_StaticVariablePrefix_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.StaticVariablePrefix(), None)
    def test_StaticVariablePrefix_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.StaticVariablePrefix(), None)

    def test_GlobalVariablePrefix_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.GlobalVariablePrefix().id, 'R002')
        self.assertEqual(obj.GlobalVariablePrefix().param, 'g_')
        self.assertEqual(obj.StaticVariablePrefix().level, 'SHOULD')
    def test_GlobalVariablePrefix_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.GlobalVariablePrefix(), None)
    def test_GlobalVariablePrefix_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.GlobalVariablePrefix(), None)

    def test_VarialeLengthMin_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.VariableLengthMin().id, 'R003')
        self.assertEqual(obj.VariableLengthMin().param, 2)
        self.assertEqual(obj.VariableLengthMin().level, 'MUST')
    def test_VarialeLengthMin_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.VariableLengthMin(), None)
    def test_VarialeLengthMin_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.VariableLengthMin(), None)

    def test_ReculsiveCall_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.ReculsiveCall().id, 'R004')
        self.assertEqual(obj.ReculsiveCall().param, True)
        self.assertEqual(obj.ReculsiveCall().level, 'MUST')
    def test_ReculsiveCall_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.ReculsiveCall(), None)
    def test_ReculsiveCall_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.ReculsiveCall(), None)

    def test_FunctionBlackList_vaild(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.FunctionBlackList().id,'R005')
        self.assertEqual(obj.FunctionBlackList().param,["malloc","free"])
        self.assertEqual(obj.FunctionBlackList().level,'WANT')
    def test_FunctionBlackList_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.FunctionBlackList(),None)
    def test_FunctionBlackList_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.FunctionBlackList(),None)

    def test_NoBreakInSwitch_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.NoBreakInSwitch().id, 'R006')
        self.assertEqual(obj.NoBreakInSwitch().param, True)
        self.assertEqual(obj.NoBreakInSwitch().level,'SHOULD')
    def test_NoBreakInSwitch_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.NoBreakInSwitch(), None)
    def test_NoBreakInSwitch_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.NoBreakInSwitch(), None)
    
    def test_NoDefaultInSwitch_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.NoDefaultInSwitch().id, 'R007')
        self.assertEqual(obj.NoDefaultInSwitch().param, True)
        self.assertEqual(obj.NoDefaultInSwitch().level, 'SHOULD')
    def test_NoDefaultInSwitch_NoAllKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_all_key.json")
        self.assertEqual(obj.NoDefaultInSwitch(), None)
    def test_NoDefaultInSwitch_NoConditionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_conditions_key.json")
        self.assertEqual(obj.NoDefaultInSwitch(), None)
    

if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    unittest.main()