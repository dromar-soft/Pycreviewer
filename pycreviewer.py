# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
from pathlib import Path
from cparser import c_parser_wrapper,ast_analyser
from review_rules import review_rules
from ui import cui_view,view_model_communication
import time 
import os


def execute_code_review(source_path: str) ->list:

    print("Executing: "+source_path)
    ast = c_parser_wrapper.parse(filepath=source_path,cpp_args=['-E', r'-Icparser/utils/fake_libc_include'])
    analyser = ast_analyser.AstAnalyser(ast)
    rules = review_rules.ReviewRules(analyser)
    results = rules.check()
    return results

def search_csource_abs_paths(source_folder: str) ->list:
    p = Path(source_folder)
    source_path_list = list(p.glob("**/*.c"))
    return [str(path.absolute()) for path in source_path_list]

if __name__ == "__main__":

    print("pycreviewer start")

    communication = view_model_communication.ViewModelCommunicaton()
    view = cui_view.CuiView(communication)
    view.startup()

    #wait user input sourcefolder in ui thread
    source_folder = None
    while True:
        recvMsg = communication.recieve_request_from_view(timeout=0.1)
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
        recvMsg = communication.recieve_request_from_view(timeout=0.1)
        if not recvMsg:
            results = execute_code_review(source_file_path)
            communication.send_review_results(results)
        elif recvMsg.id == "cancel_request":
            break
        else:
            pass

    print("pycreviewer end")