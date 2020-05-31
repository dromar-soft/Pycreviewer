import unittest
import pycreviewer

class TestPyCReviewer(unittest.TestCase):
    """TestPyCReviewerモジュールのテストクラス
            正常系テスト観点：
                全チェック項目が必ず１つ以上該当する、代表的なソースコードをレビューし、
                戻り値に各チェック項目IDが一つ以上含まれていることを確認する。
            異常系テスト観点:
                空のソースコードをレビューしたときに指摘事項がないことを確認する
    """

    def test_pycreviewer_review_file_valid(self):
        expect_id_set = {'R001','R002','R003','R004','R005','R006','R007'}
        review_file_path = './test_data/c_files/valid.c'
        check_results = pycreviewer.review_file(sourcefile=review_file_path)
        check_id_list = []
        for check_result in check_results:
            check_id_list.append(check_result.id)
        check_id_set = set(check_id_list)
        self.assertEqual(expect_id_set, check_id_set)

    def test_pycreviewer_review_file_none(self):
        review_file_path = './test_data/c_files/none.c'
        check_results = pycreviewer.review_file(sourcefile=review_file_path)
        self.assertEqual(len(check_results), 0)