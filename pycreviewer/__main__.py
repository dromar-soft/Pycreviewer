# coding: UTF-8
from logging import (getLogger, StreamHandler, INFO, Formatter)
from threading import (Event, Thread)
from pathlib import Path
import time 
import os

import pycreviewer
from .source_code import SourceCode
from .source_file_parser import parse
from .check_conditions import CheckConditions
from .cui_view import CuiView
from .view_model_communication import ViewModelCommunicaton
from .coding_rules import CheckResult, CodinfgRules


def review_file(filepath: str, cpp_args=['-E', r'-Ipycreviewer/utils/fake_libc_include']) ->list:
    """
    単一のソースファイルに対してコードレビューを実施する。
    コードレビューの結果は、List<CheckResult>形式で返す。
    'filepath'には対象のソースファイルパスを入力する
    'cppargs'にはCコンパイラのプリプロセッサ実行時のコマンドライン引数をリスト形式で入力する。
    通常、'cppargs'には、プリプロセッサ実行オプション'-E'と、インクルードオプション'-Ixxxxx'を指定する
    """

    print("Executing: "+filepath)
    ast = parse(filepath=filepath,cpp_args=cpp_args)
    code = SourceCode(ast)
    rules = CodinfgRules(code, CheckConditions('./default.json'))
    results = rules.check_all()
    return results

def search_csource_abs_paths(source_folder: str) ->list:
    p = Path(source_folder)
    source_path_list = list(p.glob("**/*.c"))
    return [str(path.absolute()) for path in source_path_list]

if __name__ == "__main__":
    """
    pycreviewerライブラリを使用した簡単なCUIアプリケーション機能を提供する
    本アプリケーションは、コンソール上でレビュー対象のソースフォルダパスの入力を受け付ける。
    フォルダパスの入力受付後、フォルダパス内にある'.c'ファイルを再起的に検索し、各ファイルについてreview_file()を実行する。
    ユーザは'esc'キー入力によって実行中のコードレビューを中止することができる
    """

    print("pycreviewer cui application start")

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
        if recvMsg is None:
            #コードレビュー処理を継続
            results = review_file(source_file_path)
            communication.send_review_results(results)
        elif recvMsg.id == "cancel_request":
            break
        else:
            pass

    print("pycreviewer cui application end")