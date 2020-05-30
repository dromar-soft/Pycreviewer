import unittest
from pycreviewer.view_model_communication import ViewModelCommunicaton

class TestViewModelCommunicaton(unittest.TestCase):
    """ViewModelCommunicatonクラスのテストクラス
            正常系のテスト観点：
                send_xxx()したデータが、recieve_xxxx()で正しく受信できることを確認する
            異常系テスト観点:
                recieve_xxxx()のタイムアウト発生時の挙動
    """

    def test_send_recv_start_request(self):
        expect_data = 'test_send_start_request'
        expect_id = 'start_request'
        timeout = 0.1 
        vmc = ViewModelCommunicaton()
        vmc.send_start_request(expect_data)
        recv_msg = vmc.recieve_request_from_view(timeout)
        self.assertEqual(expect_data, recv_msg.data)
        self.assertEqual(expect_id, recv_msg.id)

    def test_send_recv_end_response(self):
        expect_data = 10
        expect_id = 'end_response'
        timeout = 0.1
        vmc = ViewModelCommunicaton()
        vmc.send_end_response(expect_data)
        recv_msg = vmc.recieve_response_from_model(timeout)
        self.assertEqual(expect_data, recv_msg.data)
        self.assertEqual(expect_id, recv_msg.id)

    def test_send_recv_cancel_request(self):
        expect_id = 'cancel_request'
        timeout = 0.1
        vmc = ViewModelCommunicaton()
        vmc.send_cancel_request()
        recv_msg = vmc.recieve_request_from_view(timeout)
        self.assertIsNone(recv_msg.data )
        self.assertEqual(expect_id, recv_msg.id)

    def test_send_recv_cancel_response(self):
        expect_id = 'cancel_response'
        timeout = 0.1
        vmc = ViewModelCommunicaton()
        vmc.send_cancel_response()
        recv_msg = vmc.recieve_response_from_model(timeout)
        self.assertIsNone(recv_msg.data )
        self.assertEqual(expect_id, recv_msg.id)

    def test_send_recv_review_results(self):
        expect_id = 'review_results'
        expect_data = ['t','e','s','t']
        timeout = 0.1
        vmc = ViewModelCommunicaton()
        vmc.send_review_results(expect_data)
        recv_msg = vmc.recieve_response_from_model(timeout)
        self.assertEqual(expect_data, recv_msg.data)
        self.assertEqual(expect_id, recv_msg.id)

    def test_recieve_request_from_view_timeout(self):
        vmc = ViewModelCommunicaton()
        timeout = 0.1
        recv_msg = vmc.recieve_request_from_view(timeout)
        self.assertIsNone(recv_msg)

    def test_recieve_response_from_view_timeout(self):
        vmc = ViewModelCommunicaton()
        timeout = 0.1
        recv_msg = vmc.recieve_response_from_model(timeout)
        self.assertIsNone(recv_msg)