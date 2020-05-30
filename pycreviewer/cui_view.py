# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
import queue
import time
from blessed import Terminal

handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
logger = getLogger()
logger.addHandler(handler)
logger.setLevel(INFO)

class CuiView(object):
    """
    The CuiView class provides user interface functionality with CUI.
    """

    def __init__(self, presenter):
        self.presenter = presenter

    def ui_main_thread(self):
        
        logger.debug("ui thread start")

        sourceFolder = None
        while not sourceFolder:
            sourceFolder = input('input source folder >> ')
        self.presenter.send_start_request(sourceFolder)
        
        t = Terminal()
        with t.cbreak():
            while True:
                k = t.inkey(timeout=0.1)
                if not k :
                    recvMsg = self.presenter.recieve_response_from_model(timeout=0.1)
                    if recvMsg is not None:
                        if(recvMsg.id == 'review_results'):
                            self.__output_review_results(recvMsg.data)
                        elif(recvMsg.id == 'end_response'):
                            print( str(recvMsg.data)+' files codereview completed. Please enter esc key.')
                elif k.is_sequence:
                    if k.name == 'KEY_ESCAPE':
                        self.presenter.send_cancel_request()
                        break
                else:
                    pass

        logger.debug("ui thread end")

    def startup(self):
        self.thread = Thread(target=self.ui_main_thread)
        self.thread.start()

    def __output_review_results(self,results):
        for result in results:
             print(vars(result))