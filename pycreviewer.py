# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
from cparser import c_parser_wrapper,ast_analyser
from ui import cui_view,presenter
import time 

if __name__ == "__main__":

    print("pycreviewer start")

    myPresenter = presenter.Presenter()
    myView = cui_view.CuiView(myPresenter)
    myView.startup()

    #wait user input sourcefolder in ui thread
    recvMsg = None
    while recvMsg == None:
        recvMsg = myPresenter.recieve_request(timeout=0.1)
    print("id:"+recvMsg.id) 
    print("data:"+recvMsg.data) 

    #for each file
        #execute codereview
        #output results in ui thread
        #if user cancelled process from ui thread, then break for loop
    #end
    iscancelled = None
    while iscancelled == None:
        iscancelled = myPresenter.recieve_request(timeout=0.1)
        myPresenter.send_review_results("results")

    print("pycreviewer end")