import queue

class ViewModelCommunicaton(object):
    """
    ViewModelCommunicaton provides thread safe communication between view class and model class.
    """

    def __init__(self):
        self.model_to_view_msg = queue.Queue()
        self.view_to_model_msg = queue.Queue()

    def send_start_request(self, folder_path):
        print("send_start_request:" + folder_path)
        msg = Message("start_request", folder_path)
        self.view_to_model_msg.put(msg)

    def send_start_response(self, file_num):
        print("send_start_response fileNum: + filenum")
        msg = Message("start_response", filenum)
        self.model_to_view_msg.put(msg)

    def send_cancel_request(self):
        print("send_cancel_request")
        msg = Message("cancel_request", None)
        self.view_to_model_msg.put(msg)

    def send_cancel_response(self):
        print("send_cancel_response")
        msg = Message("cancel_response", None)
        self.model_to_view_msg.put(msg)

    def recieve_request_from_view(self, timeout):
        try:
            msg = self.view_to_model_msg.get(timeout=timeout)
            return msg
        except queue.Empty:
            return None
    
    def recieve_response_from_model(self, timeout):
        try:
            msg = self.model_to_view_msg.get(timeout=timeout)
            return msg
        except queue.Empty:
            return None

    def send_review_results(self, results):
            msg = Message("review_results", results)
            self.model_to_view_msg.put(msg)
            #print("send_review_results")

class Message(object):

    def __init__(self, id, data):
        self.id = id
        self.data = data