# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
import queue
import time
from blessed import Terminal
import presenter

handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
logger = getLogger()
logger.addHandler(handler)
logger.setLevel(INFO)

class CuiView(object):

    def __init__(self, presenter):
        self.presenter = presenter

    def ui_main_thread(self):
        
        logger.info("ui thread start")

        sourceFolder = None
        while not sourceFolder:
            print u'input source folder'
            sourceFolder = raw_input('>> ')
        self.presenter.send_start_request(sourceFolder)
        
        t = Terminal()
        with t.cbreak():
            while True:
                k = t.inkey(timeout=0.1)
                if not k :
                    recvMsg = self.presenter.recieve_response(timeout=0.1)
                    if recvMsg is not None:
                        logger.info("id:"+recvMsg.id+ " data:"+recvMsg.data)
                elif k.is_sequence:
                    if k.name == 'KEY_ESCAPE':
                        self.presenter.send_cancel_request()
                        break
                else:
                    pass

        logger.info("ui thread end")

    def startup(self):
        self.thread = Thread(target=self.ui_main_thread)
        self.thread.start()

    