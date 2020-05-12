# -*- coding: utf-8 -*-

import unittest
import check_conditions  # テスト対象のモジュールをインポートする

class TestCheckConditions(unittest.TestCase):
    """check_conditionsクラステストを記述するクラス"""

    def test_Version_valid(self):
        obj = check_conditions.CheckConditions("./test_data/default.json")
        self.assertEqual(obj.Version(), "0.1.0")

    def test_Version_noVersionKey(self):
        obj = check_conditions.CheckConditions("./test_data/no_version_key.json")
        self.assertEqual(obj.Version(), '')


if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    unittest.main()