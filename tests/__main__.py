# -*- coding: utf-8 -*-

import unittest
from .test_check_conditions import TestCheckConditions 
from .test_source_code import TestSourceCode
from .test_coding_rules import TestCodingRules

if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    print('unittest_main')
    unittest.main()