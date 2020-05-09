# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
from cparser import c_parser_wrapper,ast_analyser
from ui import cui_view,presenter
import time 
import os


def code_review_file():

    time.sleep(0.5)
    return "ALL OK."

def get_c_source_list(source_folder):
    found = []
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            found.append(os.path.join(root, filename))   # ファイルのみ再帰でいい場合はここまででOK
        # for dirname in dirs:
        #     found.append(os.path.join(root, dirname))    # サブディレクトリまでリストに含めたい場合はこれも書く
    return found

if __name__ == "__main__":

    print("pycreviewer start")

    myPresenter = presenter.Presenter()
    myView = cui_view.CuiView(myPresenter)
    myView.startup()

    #wait user input sourcefolder in ui thread
    source_folder = None
    while True:
        recvMsg = myPresenter.recieve_request(timeout=0.1)
        if not recvMsg:
            pass
        elif recvMsg.id == "start_request":
            source_folder = recvMsg.data
            break
        else:
            pass

    #create file list
    source_list = get_c_source_list(source_folder)
    print(source_list)
    
    # #for each file
    #     #execute codereview
    #     #output results in ui thread
    #     #if user cancelled process from ui thread, then break for loop
    # #end
    while True:
        recvMsg = myPresenter.recieve_request(timeout=0.1)
        if not recvMsg:
            results = code_review_file()
            myPresenter.send_review_results(results)
        elif recvMsg.id == "cancel_request":
            break
        else:
            pass

    print("pycreviewer end")