# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
from pathlib import Path
from cparser import c_parser_wrapper,ast_analyser
from ui import cui_view,presenter
import time 
import os


def code_review_file(source_path: str):

    print("Executing: "+source_path)
    time.sleep(0.5)
    return "ALL OK."

def search_csource_abs_paths(source_folder: str) ->list:
    p = Path(source_folder)
    source_path_list = list(p.glob("**/*.c"))
    return [str(path.absolute()) for path in source_path_list]

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
    source_file_paths = search_csource_abs_paths(source_folder)
    
    # #for each file
    #     #execute codereview
    #     #output results in ui thread
    #     #if user cancelled process from cui , then break for loop
    # #end
    for source_file_path in source_file_paths:
        recvMsg = myPresenter.recieve_request(timeout=0.1)
        if not recvMsg:
            results = code_review_file(source_file_path)
            myPresenter.send_review_results(results)
        elif recvMsg.id == "cancel_request":
            break
        else:
            pass

    print("pycreviewer end")