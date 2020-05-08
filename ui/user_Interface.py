# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)

handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
logger = getLogger()
logger.addHandler(handler)
logger.setLevel(INFO)

import queue
import time

def ui_main_loop():
    logger.info("ui thread start")
    time.sleep(1)
    queue1.put("check")
    time.sleep(1)
    queue1.put("exit")
    logger.info("ui thread end")
