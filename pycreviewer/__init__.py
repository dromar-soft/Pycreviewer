print("pycreviewer imported")

from .source_file_parser import parse
from .source_code import SourceCode
from .check_conditions import CheckConditions
from .coding_rules import CodinfgRules

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