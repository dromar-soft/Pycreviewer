# -*- coding: utf-8 -*-

import unittest
import check_conditions  # テスト対象のモジュールをインポートする

class TestCheckConditions(unittest.TestCase):
    """check_conditionsクラステストを記述するクラス"""

    def test_init(self):
        """__init__テスト"""
        obj = check_conditions.CheckConditions('default.json')
        # 関数の返り値が期待した内容と一致するか確認する
        self.assertEqual(obj.isInvalid(), False)

if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    unittest.main()