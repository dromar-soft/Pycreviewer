# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
from pathlib import Path
import time 
import os

print(__file__)

import pycreviewer
from .source_code import SourceCode
from .source_file_parser import parse
from .check_conditions import CheckConditions
from .cui_view import CuiView
from .view_model_communication import ViewModelCommunicaton
from .coding_rules import CheckResult, CodinfgRules


def execute_code_review(source_path: str) ->list:

    print("Executing: "+source_path)
    ast = parse(filepath=source_path,cpp_args=['-E', r'-Ipycreviewer/utils/fake_libc_include'])
    code = SourceCode(ast)
    rules = CodinfgRules(code, CheckConditions('./default.json'))
    results = rules.check_all()
    return results

def search_csource_abs_paths(source_folder: str) ->list:
    p = Path(source_folder)
    source_path_list = list(p.glob("**/*.c"))
    return [str(path.absolute()) for path in source_path_list]

if __name__ == "__main__":

    print("pycreviewer start")

    communication = ViewModelCommunicaton()
    view = CuiView(communication)
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